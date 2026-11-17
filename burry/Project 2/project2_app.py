
"""
FIN 43900 — Project 2
Meridian Foundation Reserve
Investment Management Dashboard

AI-assisted implementation: ChatGPT/Codex.

Educational analysis only — not investment advice.
"""

from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st

from project2_portfolio import (
    ASSETS,
    EXPECTED_RETURNS,
    VOLATILITIES,
    CORRELATIONS,
    OBJECTIVE_RETURN,
    RESERVE_MINIMUM,
    MINIMUM_LIQUID_SHARE,
    ISSUER_LIMIT,
    LOSS_RULE_STATUS,
    build_covariance_matrix,
    benchmark_weights,
    equal_weights,
    inverse_volatility_weights,
    search_lowest_risk,
    portfolio_return,
    portfolio_volatility,
    check_mandate,
)

from project2_signals import build_signal

from project2_validation import (
    independent_checks,
    run_stress_tests,
    stop_condition,
)


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Meridian Reserve | Project 2",
    page_icon="📊",
    layout="wide",
)

st.title("Meridian Foundation Reserve")
st.subheader("Investment Management Decision Dashboard")

st.caption(
    "FIN 43900 — Project 2 | "
    "Portfolio Analysis and Investment Committee Review"
)

st.info(
    "AI disclosure: Developed with assistance from "
    "ChatGPT/Codex.""Educational use only — not investment advice."
)


# ==================================================
# SIDEBAR — INVESTMENT MANDATE
# ==================================================

st.sidebar.header("Investment Mandate")

st.sidebar.metric(
    "Reserve Portfolio",
    "$100 million",
)

st.sidebar.metric(
    "Annual Return Objective",
    f"{OBJECTIVE_RETURN:.1%}",
)

st.sidebar.metric(
    "Minimum Reserve",
    f"{RESERVE_MINIMUM:.1%}",
)

st.sidebar.metric(
    "Minimum 5-Day Liquidity",
    f"{MINIMUM_LIQUID_SHARE:.0%}",
)

st.sidebar.metric(
    "Single-Company Issuer Limit",
    f"{ISSUER_LIMIT:.0%}",
)

st.sidebar.warning(
    "Calendar-year loss rule: " + LOSS_RULE_STATUS
)

st.sidebar.divider()
st.sidebar.header("Scenario Settings")

return_adjustment = st.sidebar.slider(
    "Expected Return Adjustment (percentage points)",
    min_value=-3.0,
    max_value=3.0,
    value=0.0,
    step=0.25,
)

volatility_multiplier = st.sidebar.slider(
    "Volatility Multiplier",
    min_value=0.5,
    max_value=2.0,
    value=1.0,
    step=0.1,
)


# ==================================================
# HELPER FUNCTIONS
# ==================================================

def historical_estimates(monthly_returns):
    """
    Lab 15 estimation method:
    Annual return = mean monthly return * 12
    Annual volatility = monthly std * sqrt(12)
    Correlation = monthly return correlation
    """
    annual_returns = (
        monthly_returns.mean() * 12
    ).to_numpy(dtype=float)

    annual_vols = (
        monthly_returns.std(ddof=1) * np.sqrt(12)
    ).to_numpy(dtype=float)

    correlations = (
        monthly_returns.corr()
    ).to_numpy(dtype=float)

    return annual_returns, annual_vols, correlations


def evaluate_allocation(weights, returns, vols, corr):
    covariance = build_covariance_matrix(corr, vols)

    expected_return = portfolio_return(
        weights, returns
    )

    volatility = portfolio_volatility(
        weights, covariance
    )

    mandate = check_mandate(
        weights,
        expected_return,
        volatility=volatility,
    )

    return expected_return, volatility, mandate


def format_weights(weights):
    return ", ".join(
        f"{asset}: {weight:.0%}"
        for asset, weight in zip(ASSETS, weights)
    )


@st.cache_data(ttl=3600)
def cached_signal(as_of_date, window):
    return build_signal(as_of_date, window)


# ==================================================
# 1. INVESTMENT UNIVERSE
# ==================================================

st.header("1. Investment Universe")

universe = pd.DataFrame({
    "Asset": ASSETS,
    "Expected Return (%)": EXPECTED_RETURNS * 100,
    "Annual Volatility (%)": VOLATILITIES * 100,
})

st.dataframe(
    universe.round(2),
    use_container_width=True,
    hide_index=True,
)

st.caption(
    "Original inputs are the illustrative "
    "Lab 14 assumptions, not forecasts "
    "derived from the historical ETF dataset."
)


# ==================================================
# 2. PORTFOLIO CONSTRUCTION
# ==================================================

st.header("2. Portfolio Construction")

adjusted_returns = (
    EXPECTED_RETURNS + return_adjustment / 100
)

adjusted_vols = (
    VOLATILITIES * volatility_multiplier
)

covariance = build_covariance_matrix(
    CORRELATIONS,
    adjusted_vols,
)

portfolios = {
    "Benchmark": benchmark_weights(),
    "Equal Weight": equal_weights(),
    "Inverse Volatility": inverse_volatility_weights(
        adjusted_vols
    ),
}

constrained = search_lowest_risk(
    returns=adjusted_returns,
    vols=adjusted_vols,
    corr=CORRELATIONS,
)

if constrained is not None:
    portfolios["Constrained Portfolio"] = np.asarray(
        constrained["weights"], dtype=float
    )
else:
    st.error(
        "No feasible constrained portfolio was found "
        "under the current sidebar assumptions."
    )

allocation_df = pd.DataFrame(
    {
        name: np.asarray(weights) * 100
        for name, weights in portfolios.items()
    },
    index=ASSETS,
)

st.subheader("Portfolio Allocations (%)")

st.dataframe(
    allocation_df.round(1),
    use_container_width=True,
)

st.subheader("Allocation Comparison")

st.bar_chart(
    allocation_df.T,
    stack=False,
)


# ==================================================
# 3. PORTFOLIO PERFORMANCE
# ==================================================

st.header("3. Portfolio Performance")

results = []

for name, weights in portfolios.items():

    expected_return, volatility, mandate = (
        evaluate_allocation(
            weights,
            adjusted_returns,
            adjusted_vols,
            CORRELATIONS,
        )
    )

    results.append({
        "Portfolio": name,
        "Expected Return (%)": expected_return * 100,
        "Volatility (%)": volatility * 100,
        "Reserve (%)": (
            mandate["reserve_weight"] * 100
        ),
        "5-Day Liquidity (%)": (
            mandate["liquid_weight"] * 100
        ),
        "Largest Company (%)": (
            mandate["largest_company_weight"] * 100
        ),
        "Mandate Verdict": mandate["mandate_verdict"],
        "Failed Rules": (
            ", ".join(mandate["failed_rules"])
            if mandate["failed_rules"]
            else "None"
        ),
    })

results_df = pd.DataFrame(results)

st.dataframe(
    results_df.round(2),
    use_container_width=True,
    hide_index=True,
)

st.caption(
    "PASS CHECKABLE RULES is not final approval. "
    "The calendar-year loss rule remains unresolved."
)


# ==================================================
# 4. RISK AND RETURN
# ==================================================

st.header("4. Risk and Return")

risk_chart = results_df.set_index("Portfolio")[
    ["Expected Return (%)", "Volatility (%)"]
]

st.bar_chart(
    risk_chart,
    stack=False,
)

st.write(
    "The investment committee should evaluate "
    "expected return, volatility, reserve coverage, "
    "liquidity, and mandate compliance together."
)


# ==================================================
# 5. POINT-IN-TIME INVESTMENT SIGNAL
# ==================================================

st.header("5. Point-in-Time Investment Signal")

st.write(
    "The signal monitors the 10-year Treasury yield "
    "using historical FRED/ALFRED observations."
)

decision_date = st.date_input(
    "Investment Decision Date",
    value=date(2026, 3, 31),
    max_value=date.today(),
)

lookback = st.slider(
    "Signal Lookback (observations)",
    min_value=10,
    max_value=60,
    value=20,
    step=5,
)

try:
    signal = cached_signal(
        decision_date,
        lookback,
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Last Available Yield",
        f"{signal['latest_yield']:.2f}%",
    )

    col2.metric(
        "Lookback Average",
        f"{signal['average_yield']:.2f}%",
    )

    col3.metric(
        "Difference",
        f"{signal['spread_bps']:+.1f} bps",
    )

    st.subheader("Historical Yield Observations")

    st.line_chart(signal["history"])

    st.subheader("Signal Interpretation")

    st.info(
        f"Signal status: {signal['status']}. "
        "This is a monitoring indicator, "
        "not a return forecast."
    )

    st.subheader("Point-in-Time Data Card")

    data_card = pd.DataFrame({
        "Field": [
            "Series",
            "Source",
            "Decision date",
            "Latest observation date",
            "Latest available value",
            "Transformation",
            "Availability rule",
            "Exclusion rule",
        ],
        "Value": [
            signal["series_id"],
            signal["source"],
            signal["decision_date"],
            signal["observation_date"],
            f"{signal['latest_yield']:.3f}%",
            (
                f"Last yield minus {lookback}-observation "
                "average; converted to basis points"
            ),
            signal["availability_rule"],
            (
                "Exclude missing values and observations "
                "after the decision date."
            ),
        ],
    })

    st.dataframe(
        data_card,
        use_container_width=True,
        hide_index=True,
    )

    st.caption(
        "FRED/ALFRED historical vintages help reduce "
        "look-ahead bias. Actual release and "
        "availability timing require verification."
    )

except Exception as error:
    st.error(
        "Unable to load the point-in-time signal: "
        + str(error)
    )


# ==================================================
# 6. VALIDATION AND STRESS TESTING
# ==================================================

st.header("6. Validation and Stress Testing")

st.subheader("Fixed-Allocation Stress Tests")

st.write(
    "These scenarios hold the original constrained "
    "portfolio weights constant, rather than "
    "re-optimizing after every shock."
)

stress_results = run_stress_tests()

st.dataframe(
    stress_results.round(2),
    use_container_width=True,
    hide_index=True,
)

st.subheader("Independent Calculation Checks")

checks = independent_checks()

check_table = pd.DataFrame([
    {
        "Check": name,
        "Result": "PASS" if passed else "FAIL",
    }
    for name, passed in checks.items()
])

st.dataframe(
    check_table,
    use_container_width=True,
    hide_index=True,
)

st.subheader("Process Stop Condition")

decision = stop_condition(stress_results)

if decision["stop"]:
    st.error(
        "STOP / DEFER: " + decision["reason"]
    )

    st.write(
        "**Failed scenarios:** "
        + ", ".join(decision["failed_scenarios"])
    )
else:
    st.success(
        "All defined stress scenarios passed."
    )

st.caption(
    "The stop condition is a proposed conservative "
    "validation gate, not an approved CIO mandate. "
    "Transaction costs are simplified one-time "
    "portfolio-wide deductions. A volatility increase "
    "does not automatically constitute a mandate "
    "failure unless a volatility limit is specified."
)


# ==================================================
# 6A. HISTORICAL ESTIMATION-WINDOW SENSITIVITY
# ==================================================

st.subheader("Historical Estimation-Window Sensitivity")

st.write(
    "This test compares the original Lab 14 "
    "assumptions against two estimation windows "
    "using historical ETF proxy prices."
)

st.write(
    "The fixed-allocation test measures robustness. "
    "The re-optimized test evaluates whether a "
    "different allocation can meet the modeled rules."
)

price_file = (
    Path(__file__).resolve().parent
    / "monthly_prices.csv"
)

historical_window_failure = None

if not price_file.exists():

    st.warning(
        "monthly_prices.csv was not found. "
        "Run create_price_data.py first."
    )

else:

    try:
        # ------------------------------------------
        # LOAD AND VALIDATE MONTHLY PRICE DATA
        # ------------------------------------------

        prices = pd.read_csv(
            price_file,
            parse_dates=[0],
        )

        date_column = prices.columns[0]

        prices = prices.sort_values(
            date_column
        ).copy()

        cutoff = pd.Timestamp("2026-03-31")

        prices = prices.loc[
            prices[date_column] <= cutoff
        ].copy()

        if prices.empty:
            raise ValueError(
                "No price observations before cutoff."
            )

        if list(prices.columns[1:]) != list(ASSETS):
            raise ValueError(
                "CSV asset names or order do not "
                "match project2_portfolio.ASSETS."
            )

        if prices[date_column].duplicated().any():
            raise ValueError(
                "Duplicate dates found."
            )

        if (
            prices[date_column]
            .dt.to_period("M")
            .duplicated()
            .any()
        ):
            raise ValueError(
                "More than one observation per month."
            )

        numeric_prices = prices.set_index(
            date_column
        )[list(ASSETS)]

        numeric_prices = numeric_prices.apply(
            pd.to_numeric,
            errors="raise",
        )

        if not np.isfinite(
            numeric_prices.to_numpy()
        ).all():
            raise ValueError(
                "Missing or non-finite prices detected."
            )

        if (numeric_prices <= 0).any().any():
            raise ValueError(
                "Prices must be positive."
            )

        monthly_returns = (
            numeric_prices
            .pct_change(fill_method=None)
            .dropna()
        )

        if len(monthly_returns) < 36:
            raise ValueError(
                "At least 36 monthly returns required."
            )

        # ------------------------------------------
        # ESTIMATE TWO HISTORICAL WINDOWS
        # ------------------------------------------

        full_returns, full_vols, full_corr = (
            historical_estimates(monthly_returns)
        )

        recent_returns, recent_vols, recent_corr = (
            historical_estimates(
                monthly_returns.tail(36)
            )
        )

        windows = [
            (
                "Lab 14 assumptions",
                EXPECTED_RETURNS,
                VOLATILITIES,
                CORRELATIONS,
            ),
            (
                "Full history",
                full_returns,
                full_vols,
                full_corr,
            ),
            (
                "Last 36 months",
                recent_returns,
                recent_vols,
                recent_corr,
            ),
        ]

        # Use the original Lab 14 constrained weights.
        # Do not use the sidebar-adjusted allocation.

        baseline_constrained = search_lowest_risk(
            returns=EXPECTED_RETURNS,
            vols=VOLATILITIES,
            corr=CORRELATIONS,
        )

        if baseline_constrained is None:
            raise ValueError(
                "Original constrained allocation "
                "was not feasible."
            )

        fixed_weights = np.asarray(
            baseline_constrained["weights"],
            dtype=float,
        )

        estimate_rows = []
        comparison_rows = []

        for (
            window_name,
            window_returns,
            window_vols,
            window_corr,
        ) in windows:

            # --------------------------------------
            # ASSET-LEVEL ESTIMATES
            # --------------------------------------

            for asset, ret, vol in zip(
                ASSETS,
                window_returns,
                window_vols,
            ):

                estimate_rows.append({
                    "Window": window_name,
                    "Asset": asset,
                    "Return (%)": float(ret) * 100,
                    "Volatility (%)": float(vol) * 100,
                })

            # --------------------------------------
            # FIXED ORIGINAL ALLOCATION
            # --------------------------------------

            fixed_return, fixed_vol, fixed_mandate = (
                evaluate_allocation(
                    fixed_weights,
                    window_returns,
                    window_vols,
                    window_corr,
                )
            )

            comparison_rows.append({
                "Window": window_name,
                "Method": "Fixed Lab 14 allocation",
                "Return (%)": fixed_return * 100,
                "Volatility (%)": fixed_vol * 100,
                "Reserve (%)": (
                    fixed_mandate["reserve_weight"] * 100
                ),
                "Verdict": (
                    fixed_mandate["mandate_verdict"]
                ),
                "Failed Rules": (
                    ", ".join(
                        fixed_mandate["failed_rules"]
                    ) or "None"
                ),
                "Weights": format_weights(
                    fixed_weights
                ),
            })

            # --------------------------------------
            # RE-OPTIMIZED ALLOCATION
            # --------------------------------------

            optimized = search_lowest_risk(
                returns=window_returns,
                vols=window_vols,
                corr=window_corr,
            )

            if optimized is None:

                comparison_rows.append({
                    "Window": window_name,
                    "Method": "Re-optimized (5% grid)",
                    "Return (%)": np.nan,
                    "Volatility (%)": np.nan,
                    "Reserve (%)": np.nan,
                    "Verdict": "NO FEASIBLE PORTFOLIO",
                    "Failed Rules": (
                        "No feasible grid allocation"
                    ),
                    "Weights": "—",
                })

            else:

                new_weights = np.asarray(
                    optimized["weights"],
                    dtype=float,
                )

                new_return, new_vol, new_mandate = (
                    evaluate_allocation(
                        new_weights,
                        window_returns,
                        window_vols,
                        window_corr,
                    )
                )

                comparison_rows.append({
                    "Window": window_name,
                    "Method": "Re-optimized (5% grid)",
                    "Return (%)": new_return * 100,
                    "Volatility (%)": new_vol * 100,
                    "Reserve (%)": (
                        new_mandate["reserve_weight"] * 100
                    ),
                    "Verdict": (
                        new_mandate["mandate_verdict"]
                    ),
                    "Failed Rules": (
                        ", ".join(
                            new_mandate["failed_rules"]
                        ) or "None"
                    ),
                    "Weights": format_weights(
                        new_weights
                    ),
                })

        # ------------------------------------------
        # DISPLAY RESULTS
        # ------------------------------------------

        st.caption(
            f"Monthly price rows: {len(prices)} | "
            f"Monthly returns: {len(monthly_returns)} | "
            f"First price: "
            f"{prices[date_column].min().date()} | "
            f"Last price: "
            f"{prices[date_column].max().date()}"
        )

        st.markdown(
            "**Annualized Asset Estimates**"
        )

        estimates_df = pd.DataFrame(
            estimate_rows
        )

        st.dataframe(
            estimates_df.round(2),
            use_container_width=True,
            hide_index=True,
        )

        st.markdown(
            "**Portfolio Outcomes by Estimation Window**"
        )

        window_results = pd.DataFrame(
            comparison_rows
        )

        st.dataframe(
            window_results.round(2),
            use_container_width=True,
            hide_index=True,
        )

        # ------------------------------------------
        # ROBUSTNESS VERDICT
        # ------------------------------------------

        fixed_history = window_results.loc[
            (
                window_results["Method"]
                == "Fixed Lab 14 allocation"
            )
            &
            (
                window_results["Window"]
                != "Lab 14 assumptions"
            )
        ]

        historical_window_failure = (
            fixed_history["Verdict"]
            != "PASS CHECKABLE RULES"
        ).any()

        if historical_window_failure:

            st.error(
                "ESTIMATION-WINDOW WARNING: "
                "The original constrained allocation "
                "fails at least one checkable rule "
                "under a historical estimation window. "
                "This supports deferring full adoption."
            )

        else:

            st.info(
                "The original allocation passes "
                "the checkable rules under both "
                "historical estimation windows. "
                "This does not eliminate model risk."
            )

        st.caption(
            "ETF proxies: SGOV = Treasury bills; "
            "IEF = 10-year Treasury; "
            "LQD = investment-grade bonds; "
            "VT = global equities. "
            "Annualized arithmetic returns use "
            "monthly mean × 12; volatility uses "
            "monthly sample standard deviation "
            "× sqrt(12). "
            "Prices were downloaded using yfinance "
            "with auto_adjust=True. "
            "These are proxy estimates, not identical "
            "to the original mandate assets. "
            "Current adjusted-price histories are "
            "not independently verified "
            "point-in-time vintages. "
            "The optimizer uses a discrete 5% grid."
        )

    except Exception as error:

        st.error(
            "Historical-window analysis failed: "
            + str(error)
        )


# ==================================================
# 7. INVESTMENT COMMITTEE DECISION
# ==================================================

st.header("7. Investment Committee Decision")

selected_portfolio = st.selectbox(
    "Select Portfolio",
    results_df["Portfolio"].tolist(),
    index=len(results_df) - 1,
)

selected = results_df.loc[
    results_df["Portfolio"] == selected_portfolio
].iloc[0]

col1, col2, col3 = st.columns(3)

col1.metric(
    "Expected Return",
    f"{selected['Expected Return (%)']:.2f}%",
)

col2.metric(
    "Annual Volatility",
    f"{selected['Volatility (%)']:.2f}%",
)

col3.metric(
    "Mandate Status",
    selected["Mandate Verdict"],
)

if selected["Mandate Verdict"] == "PASS CHECKABLE RULES":

    st.success(
        "The selected portfolio meets "
        "currently checkable mandate rules."
    )

else:

    st.error(
        "Mandate failures: "
        + selected["Failed Rules"]
    )


# ==================================================
# COMMITTEE RECOMMENDATION
# ==================================================

st.subheader("Preliminary Recommendation")

if constrained is None:

    st.error(
        "REJECT under the selected sidebar assumptions: "
        "no feasible constrained portfolio was found."
    )

else:

    st.info(
        "DEFER FULL ADOPTION / VALIDATE BEFORE PILOT. "
        "The constrained strategy meets the baseline "
        "modeled checks, but the return margin is narrow "
        "and robustness must be evaluated."
    )

if decision["stop"]:

    st.error(
        "The proposed stress-test gate recommends "
        "STOP / DEFER because one or more stress "
        "scenarios failed."
    )

if historical_window_failure is True:

    st.error(
        "The historical-window analysis also "
        "identifies a robustness failure."
    )

elif historical_window_failure is None:

    st.warning(
        "Historical-window validation has not "
        "been completed successfully."
    )

st.write(
    "**Committee ask:** Authorize additional validation "
    "before approving implementation of the strategy."
)

st.write(
    "**Provisional allocation:** 0% new capital "
    "until the unresolved calendar-year loss rule "
    "and robustness concerns are addressed. "
    "This is a proposed recommendation, "
    "not an approved committee decision."
)

st.write(
    "**Proposed monitoring triggers:** "
    "Expected return below 6.5%, "
    "reserve coverage below the mandate minimum, "
    "5-day liquidity below 90%, "
    "issuer concentration above 8%, "
    "or a material change in estimated risk."
)

st.write(
    "**Reversal condition:** Reconsider adoption "
    "only after updated estimates, costs, "
    "and stress testing support the strategy "
    "and the CIO clarifies the loss rule."
)

st.warning(
    "The final committee recommendation, "
    "allocation range, and monitoring policy "
    "must be reviewed and approved by the student."
)

st.divider()

st.caption(
    "Meridian Foundation Reserve | "
    "FIN 43900 Project 2"
)