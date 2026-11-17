
"""
FIN 43900 — Project 2
Meridian Foundation Reserve
Portfolio Validation and Stress Testing

AI-assisted implementation: Codex/ChatGPT.
Educational analysis only — not investment advice.
"""

import numpy as np
import pandas as pd

from project2_portfolio import (
    ASSETS,
    EXPECTED_RETURNS,
    VOLATILITIES,
    CORRELATIONS,
    OBJECTIVE_RETURN,
    RESERVE_MINIMUM,
    MINIMUM_LIQUID_SHARE,
    build_covariance_matrix,
    portfolio_return,
    portfolio_volatility,
    check_mandate,
    search_lowest_risk,
)


def independent_checks():
    """
    Cross-check portfolio return and variance using
    explicit loops rather than the matrix operations
    in the main portfolio module.
    """
    weights = np.array([0.0, 0.20, 0.25, 0.55])

    covariance = build_covariance_matrix(
        CORRELATIONS, VOLATILITIES
    )

    manual_return = sum(
        float(weights[i] * EXPECTED_RETURNS[i])
        for i in range(len(weights))
    )

    manual_variance = sum(
        float(weights[i] * weights[j] * covariance[i, j])
        for i in range(len(weights))
        for j in range(len(weights))
    )

    model_return = portfolio_return(
        weights, EXPECTED_RETURNS
    )

    model_vol = portfolio_volatility(
        weights, covariance
    )

    return {
        "Return calculation": np.isclose(
            manual_return, model_return
        ),
        "Volatility calculation": np.isclose(
            np.sqrt(manual_variance), model_vol
        ),
        "Weights sum to 100%": np.isclose(
            weights.sum(), 1.0
        ),
        "Covariance symmetric": np.allclose(
            covariance, covariance.T
        ),
        "Covariance PSD": (
            np.linalg.eigvalsh(covariance).min() >= -1e-10
        ),
    }


def evaluate_fixed_allocation(
    weights,
    returns,
    vols,
    transaction_cost_bps=0.0,
    reserve_minimum=RESERVE_MINIMUM,
):
    """
    Test a fixed allocation without re-optimizing.

    Transaction costs are modeled as a one-time
    portfolio-wide deduction in basis points,
    not a recurring annual fee.
    """
    covariance = build_covariance_matrix(
        CORRELATIONS, vols
    )

    gross_return = portfolio_return(weights, returns)
    net_return = (
        gross_return - transaction_cost_bps / 10000
    )

    volatility = portfolio_volatility(
        weights, covariance
    )

    mandate = check_mandate(
        weights,
        net_return,
        volatility=volatility,
        reserve_minimum=reserve_minimum,
    )

    return {
        "Net Return (%)": net_return * 100,
        "Volatility (%)": volatility * 100,
        "Reserve (%)": mandate["reserve_weight"] * 100,
        "Verdict": mandate["mandate_verdict"],
        "Failed Rules": (
            ", ".join(mandate["failed_rules"])
            if mandate["failed_rules"]
            else "None"
        ),
    }


def run_stress_tests():
    """
    Stress the baseline constrained allocation.

    The fixed-weight tests show fragility without
    hiding failures through re-optimization.
    """
    baseline = search_lowest_risk()

    if baseline is None:
        raise ValueError(
            "No feasible baseline constrained portfolio."
        )

    weights = np.asarray(
        baseline["weights"], dtype=float
    )

    scenarios = [
        {
            "Scenario": "Baseline",
            "returns": EXPECTED_RETURNS,
            "vols": VOLATILITIES,
            "cost": 0,
            "reserve_min": RESERVE_MINIMUM,
        },
        {
            "Scenario": "Returns -0.25 pp",
            "returns": EXPECTED_RETURNS - 0.0025,
            "vols": VOLATILITIES,
            "cost": 0,
            "reserve_min": RESERVE_MINIMUM,
        },
        {
            "Scenario": "Returns -0.50 pp",
            "returns": EXPECTED_RETURNS - 0.0050,
            "vols": VOLATILITIES,
            "cost": 0,
            "reserve_min": RESERVE_MINIMUM,
        },
        {
            "Scenario": "Volatility +25%",
            "returns": EXPECTED_RETURNS,
            "vols": VOLATILITIES * 1.25,
            "cost": 0,
            "reserve_min": RESERVE_MINIMUM,
        },
        {
            "Scenario": "Transaction cost 10 bps",
            "returns": EXPECTED_RETURNS,
            "vols": VOLATILITIES,
            "cost": 10,
            "reserve_min": RESERVE_MINIMUM,
        },
        {
            "Scenario": "Transaction cost 25 bps",
            "returns": EXPECTED_RETURNS,
            "vols": VOLATILITIES,
            "cost": 25,
            "reserve_min": RESERVE_MINIMUM,
        },
        {
            "Scenario": "Reserve minimum 25%",
            "returns": EXPECTED_RETURNS,
            "vols": VOLATILITIES,
            "cost": 0,
            "reserve_min": 0.25,
        },
    ]

    rows = []

    for scenario in scenarios:
        result = evaluate_fixed_allocation(
            weights=weights,
            returns=scenario["returns"],
            vols=scenario["vols"],
            transaction_cost_bps=scenario["cost"],
            reserve_minimum=scenario["reserve_min"],
        )

        rows.append({
            "Scenario": scenario["Scenario"],
            **result,
        })

    return pd.DataFrame(rows)


def stop_condition(stress_results):
    """
    Flag failure if any non-baseline stress scenario
    violates a checkable mandate rule.

    This is a proposed conservative process gate,
    not an established CIO policy.
    """
    stressed = stress_results[
        stress_results["Scenario"] != "Baseline"
    ]

    failed = stressed[
        stressed["Verdict"] == "FAIL"
    ]

    if not failed.empty:
        return {
            "stop": True,
            "reason": (
                "At least one stress scenario fails "
                "a checkable rule."
            ),
            "failed_scenarios": (
                failed["Scenario"].tolist()
            ),
        }

    return {
        "stop": False,
        "reason": "All defined stress scenarios passed.",
        "failed_scenarios": [],
    }


def main():
    print("\nPROJECT 2 — VALIDATION")
    print("=" * 55)

    checks = independent_checks()

    for name, passed in checks.items():
        print(
            f"{name}: {'PASS' if passed else 'FAIL'}"
        )

    if not all(checks.values()):
        raise AssertionError(
            "Independent calculation checks failed."
        )

    print("\nSTRESS TEST RESULTS")
    print("=" * 55)

    results = run_stress_tests()

    print(results.to_string(index=False))

    decision = stop_condition(results)

    print("\nPROCESS STOP CONDITION")
    print("=" * 55)

    print("Stop:", decision["stop"])
    print("Reason:", decision["reason"])
    print(
        "Failed scenarios:",
        decision["failed_scenarios"]
    )


if __name__ == "__main__":
    main()