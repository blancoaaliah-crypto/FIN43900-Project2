
"""
FIN 43900 — Project 2
Meridian Foundation Reserve
Portfolio calculations, mandate checks, and optimization.

Based on the student's Lab 13, Lab 14, and Lab 15 work.

AI-assisted implementation:  Codex/ChatGPT,
November 13, 2026.

Educational analysis only — not investment advice.
"""

import math
from itertools import product

import numpy as np
import pandas as pd


# ==================================================
# 1. INVESTMENT MANDATE — LAB 13
# ==================================================

RESERVE_SIZE = 100.0  # USD millions
QUARTERLY_DISTRIBUTION = 0.75
QUARTERS_TO_COVER = 4

LIQUIDITY_WINDOW = 5
MINIMUM_LIQUID_SHARE = 0.90
ISSUER_LIMIT = 0.08

OBJECTIVE_RETURN = 0.065

RESERVE_MINIMUM = (
    QUARTERLY_DISTRIBUTION
    * QUARTERS_TO_COVER
    / RESERVE_SIZE
)

# Calendar-year loss rule remains unresolved.
LOSS_RULE_STATUS = "Requires CIO clarification"


# ==================================================
# 2. INVESTMENT UNIVERSE — LAB 14
# ==================================================

ASSETS = [
    "Treasury bills",
    "Treasury 10-year note",
    "Investment-grade bond fund",
    "Global equity index fund",
]

EXPECTED_RETURNS = np.array([
    0.035,
    0.043,
    0.050,
    0.080,
])

VOLATILITIES = np.array([
    0.005,
    0.070,
    0.060,
    0.160,
])

CORRELATIONS = np.array([
    [1.00, 0.10, 0.05, 0.00],
    [0.10, 1.00, 0.80, -0.10],
    [0.05, 0.80, 1.00, 0.25],
    [0.00, -0.10, 0.25, 1.00],
])

# (Issuer, business days to redeem, reserve eligible)
HOLDINGS = {
    "Treasury bills": ("U.S. Treasury", 1, True),
    "Treasury 10-year note": ("U.S. Treasury", 1, True),
    "Investment-grade bond fund": (
        "diversified fund", 3, False
    ),
    "Global equity index fund": (
        "diversified fund", 2, False
    ),
}

EXEMPT_ISSUERS = {
    "none",
    "U.S. Treasury",
    "diversified fund",
}


# ==================================================
# 3. INPUT VALIDATION
# ==================================================

def validate_inputs(returns, vols, corr):
    returns = np.asarray(returns, dtype=float)
    vols = np.asarray(vols, dtype=float)
    corr = np.asarray(corr, dtype=float)

    n = len(returns)

    if len(vols) != n or corr.shape != (n, n):
        raise ValueError("Input dimensions do not match.")

    if not np.all(np.isfinite(returns)):
        raise ValueError("Returns contain invalid values.")

    if not np.all(np.isfinite(vols)) or np.any(vols <= 0):
        raise ValueError("Volatilities must be positive.")

    if not np.all(np.isfinite(corr)):
        raise ValueError("Correlations contain invalid values.")

    if np.any(corr < -1) or np.any(corr > 1):
        raise ValueError("Correlations must be between -1 and 1.")

    if not np.allclose(corr, corr.T):
        raise ValueError("Correlation matrix must be symmetric.")

    if not np.allclose(np.diag(corr), 1.0):
        raise ValueError("Diagonal correlations must equal 1.")

    eigenvalues = np.linalg.eigvalsh(corr)

    if np.min(eigenvalues) < -1e-8:
        raise ValueError(
            "Correlation matrix is not positive semidefinite."
        )


def validate_weights(weights):
    weights = np.asarray(weights, dtype=float)

    if weights.shape != (len(ASSETS),):
        raise ValueError("Weights must match the asset universe.")

    if not np.all(np.isfinite(weights)):
        raise ValueError("Weights contain invalid values.")

    if np.any(weights < -1e-10):
        raise ValueError("Negative weights are not permitted.")

    if not np.isclose(weights.sum(), 1.0, atol=1e-8):
        raise ValueError("Weights must sum to 100%.")

    return weights


# ==================================================
# 4. PORTFOLIO CALCULATIONS
# ==================================================

def build_covariance_matrix(corr, vols):
    corr = np.asarray(corr, dtype=float)
    vols = np.asarray(vols, dtype=float)

    validate_inputs(
        np.zeros(len(vols)),
        vols,
        corr
    )

    return np.outer(vols, vols) * corr


def portfolio_return(weights, returns):
    return float(
        np.dot(
            np.asarray(weights, dtype=float),
            np.asarray(returns, dtype=float)
        )
    )


def portfolio_volatility(weights, covariance):
    weights = np.asarray(weights, dtype=float)
    covariance = np.asarray(covariance, dtype=float)

    variance = float(weights @ covariance @ weights)

    if variance < -1e-10:
        raise ValueError("Portfolio variance is negative.")

    return math.sqrt(max(variance, 0.0))


def reserve_weight(weights):
    return sum(
        float(weight)
        for asset, weight in zip(ASSETS, weights)
        if HOLDINGS[asset][2]
    )


def liquid_weight(weights):
    return sum(
        float(weight)
        for asset, weight in zip(ASSETS, weights)
        if HOLDINGS[asset][1] <= LIQUIDITY_WINDOW
    )


def largest_company_weight(weights):
    issuer_weights = {}

    for asset, weight in zip(ASSETS, weights):
        issuer = HOLDINGS[asset][0]

        if issuer not in EXEMPT_ISSUERS:
            issuer_weights[issuer] = (
                issuer_weights.get(issuer, 0.0)
                + float(weight)
            )

    return max(issuer_weights.values(), default=0.0)


# ==================================================
# 5. BASELINES — LAB 14
# ==================================================

def benchmark_weights():
    return np.array([0.0, 0.0, 0.40, 0.60])


def equal_weights():
    return np.ones(len(ASSETS)) / len(ASSETS)


def inverse_volatility_weights(vols=VOLATILITIES):
    vols = np.asarray(vols, dtype=float)

    if np.any(vols <= 0):
        raise ValueError(
            "Inverse volatility requires positive volatility."
        )

    inverse = 1.0 / vols

    return inverse / inverse.sum()


# ==================================================
# 6. MANDATE CHECKER — LAB 13
# ==================================================

def check_mandate(
    weights,
    expected_return,
    max_volatility=None,
    volatility=None,
    objective=OBJECTIVE_RETURN,
    reserve_minimum=RESERVE_MINIMUM,
    minimum_liquid_share=MINIMUM_LIQUID_SHARE,
    issuer_limit=ISSUER_LIMIT,
):
    weights = validate_weights(weights)

    reserve = reserve_weight(weights)
    liquid = liquid_weight(weights)
    largest_issuer = largest_company_weight(weights)

    failures = []

    if reserve < reserve_minimum - 1e-10:
        failures.append("Reserve minimum")

    if liquid < minimum_liquid_share - 1e-10:
        failures.append("Five-day liquidity")

    if largest_issuer > issuer_limit + 1e-10:
        failures.append("Issuer concentration")

    if expected_return < objective - 1e-10:
        failures.append("Return objective")

    if max_volatility is not None:
        if volatility is None:
            raise ValueError(
                "Volatility required when a limit is supplied."
            )

        if volatility > max_volatility + 1e-10:
            failures.append("Volatility limit")

    return {
        "mandate_verdict": (
            "PASS CHECKABLE RULES"
            if not failures else "FAIL"
        ),
        "failed_rules": failures,
        "reserve_weight": reserve,
        "liquid_weight": liquid,
        "largest_company_weight": largest_issuer,
        "loss_rule_status": LOSS_RULE_STATUS,
    }


# ==================================================
# 7. PORTFOLIO EVALUATION
# ==================================================

def evaluate_portfolio(
    name,
    weights,
    returns=EXPECTED_RETURNS,
    covariance=None,
    max_volatility=None,
):
    weights = validate_weights(weights)

    if covariance is None:
        covariance = build_covariance_matrix(
            CORRELATIONS,
            VOLATILITIES
        )

    expected_return = portfolio_return(weights, returns)
    volatility = portfolio_volatility(weights, covariance)

    mandate = check_mandate(
        weights,
        expected_return,
        max_volatility=max_volatility,
        volatility=volatility,
    )

    return {
        "portfolio": name,
        "weights": weights.tolist(),
        "expected_return": expected_return,
        "volatility": volatility,
        **mandate,
    }


# ==================================================
# 8. CONSTRAINED PORTFOLIO SEARCH — LAB 15
# ==================================================

def search_lowest_risk(
    returns=EXPECTED_RETURNS,
    vols=VOLATILITIES,
    corr=CORRELATIONS,
    objective=OBJECTIVE_RETURN,
    reserve_minimum=RESERVE_MINIMUM,
    minimum_liquid_share=MINIMUM_LIQUID_SHARE,
    issuer_limit=ISSUER_LIMIT,
    max_volatility=None,
):
    """
    Lowest-volatility feasible portfolio on a 5% grid.

    This is a discrete search, not a continuous optimizer.
    """

    returns = np.asarray(returns, dtype=float)
    vols = np.asarray(vols, dtype=float)
    corr = np.asarray(corr, dtype=float)

    validate_inputs(returns, vols, corr)

    if len(returns) != len(ASSETS):
        raise ValueError(
            "This mandate search requires the four-asset universe."
        )

    covariance = build_covariance_matrix(corr, vols)

    best = None
    lowest_vol = float("inf")

    for steps in product(range(21), repeat=len(ASSETS)):
        if sum(steps) != 20:
            continue

        weights = np.array(steps, dtype=float) / 20

        ret = portfolio_return(weights, returns)
        vol = portfolio_volatility(weights, covariance)

        if ret < objective - 1e-10:
            continue

        if reserve_weight(weights) < reserve_minimum - 1e-10:
            continue

        if liquid_weight(weights) < minimum_liquid_share - 1e-10:
            continue

        if largest_company_weight(weights) > issuer_limit + 1e-10:
            continue

        if max_volatility is not None:
            if vol > max_volatility + 1e-10:
                continue

        if vol < lowest_vol:
            lowest_vol = vol

            best = {
                "weights": weights.tolist(),
                "expected_return": ret,
                "volatility": vol,
                "reserve_weight": reserve_weight(weights),
                "liquid_weight": liquid_weight(weights),
            }

    return best


# ==================================================
# 9. HISTORICAL ESTIMATION — LAB 15
# ==================================================

def estimate_from_csv(
    file,
    last36=False,
    as_of_date=None,
):
    """
    Estimate annualized moments from monthly price data.

    Important: as_of_date limits observations, but the
    caller must separately verify actual publication
    and availability dates to prevent look-ahead bias.
    """

    df = pd.read_csv(file)

    date_column = df.columns[0]
    df[date_column] = pd.to_datetime(
        df[date_column],
        errors="raise"
    )

    df = df.sort_values(date_column)

    if as_of_date is not None:
        cutoff = pd.Timestamp(as_of_date)
        df = df[df[date_column] <= cutoff]

    prices = df.drop(columns=[date_column])
    prices = prices.apply(pd.to_numeric, errors="raise")

    if prices.isna().any().any():
        raise ValueError("Missing price observations.")

    if (prices <= 0).any().any():
        raise ValueError("Prices must be positive.")

    monthly_returns = prices.pct_change(
        fill_method=None
    ).dropna()

    if last36:
        monthly_returns = monthly_returns.tail(36)

    if len(monthly_returns) < 2:
        raise ValueError(
            "Insufficient monthly observations."
        )

    returns = (
        monthly_returns.mean() * 12
    ).to_numpy()

    vols = (
        monthly_returns.std() * math.sqrt(12)
    ).to_numpy()

    corr = monthly_returns.corr().to_numpy()

    validate_inputs(returns, vols, corr)

    return returns, vols, corr, prices.columns.tolist()


# ==================================================
# 10. BASELINE COMPARISON
# ==================================================

def compare_portfolios():
    covariance = build_covariance_matrix(
        CORRELATIONS,
        VOLATILITIES
    )

    portfolios = {
        "Benchmark": benchmark_weights(),
        "Equal Weight": equal_weights(),
        "Inverse Volatility": inverse_volatility_weights(),
    }

    results = []

    for name, weights in portfolios.items():
        results.append(
            evaluate_portfolio(
                name,
                weights,
                covariance=covariance,
            )
        )

    constrained = search_lowest_risk()

    if constrained is not None:
        results.append(
            evaluate_portfolio(
                "Constrained Portfolio",
                constrained["weights"],
                covariance=covariance,
            )
        )

    return results


# ==================================================
# 11. RUN DIRECTLY FOR TESTING
# ==================================================

if __name__ == "__main__":
    results = compare_portfolios()

    print("\nMERIDIAN FOUNDATION RESERVE")
    print("FIN 43900 — PROJECT 2")
    print("=" * 55)

    for result in results:
        print(f"\n{result['portfolio']}")
        print("-" * 45)

        for asset, weight in zip(
            ASSETS,
            result["weights"]
        ):
            print(f"{asset}: {weight * 100:.1f}%")

        print(
            f"Expected return: "
            f"{result['expected_return'] * 100:.2f}%"
        )

        print(
            f"Volatility: "
            f"{result['volatility'] * 100:.2f}%"
        )

        print(
            f"Reserve eligible: "
            f"{result['reserve_weight'] * 100:.1f}%"
        )

        print(
            f"Five-day liquidity: "
            f"{result['liquid_weight'] * 100:.1f}%"
        )

        print(
            f"Mandate verdict: "
            f"{result['mandate_verdict']}"
        )

        print(
            f"Failed rules: "
            f"{result['failed_rules']}"
        )

    print("\nUnresolved:", LOSS_RULE_STATUS)