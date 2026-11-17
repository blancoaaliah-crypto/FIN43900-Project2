Project 2 — Locked Changed-Input Record

Course: FIN 43900 — AI-Augmented Finance
Project: Meridian Foundation Reserve
Test: Expected-Return Assumption Change
Test Status: Completed
Test Date: November 17, 2026
GitHub Repository: https://github.com/blancoaaliah-crypto/FIN43900-Project2

1. Test Setup

The purpose of this changed-input test was to determine whether the investment management application could identify a portfolio satisfying the Meridian Foundation Reserve's investment mandate after a reduction in expected annual returns.

Changed input: Expected annual returns for all four assets.

Original adjustment: 0.00 percentage points.

New adjustment: −0.25 percentage points.

Test method: Re-optimize the portfolio using the revised expected-return assumptions.

All other scenario settings, including volatility assumptions, correlations, allocation constraints, and the optimization method, remained unchanged.

The optimizer searches portfolio allocations in 5-percentage-point increments and selects the lowest-volatility allocation satisfying the currently implemented mandate checks.

2. Investment Mandate

The Meridian Foundation Reserve manages a hypothetical $100 million investment portfolio.

Requirement

Mandate

Expected annual return

At least 6.5%

Reserve coverage

At least 3%

Five-business-day liquidity

At least 90%

Single-company issuer concentration

No more than 8%, where applicable

Portfolio weights

Long-only; sum to 100%

Calendar-year loss rule

Requires CIO clarification

The calendar-year loss rule remains unresolved. A portfolio passing the implemented checks is not automatically approved for investment.

3. AI-Off Prediction — Before Test

Before running the changed-input test, I predicted that reducing expected annual returns would make it harder for the portfolio to satisfy the foundation's 6.5% annual return objective.

The original portfolio had an expected return of 6.51%, exceeding the objective by only 0.01 percentage points.

I expected the optimizer to increase global equity exposure because global equities had the highest expected return among the four available investments.

I also expected the revised portfolio to have higher annual volatility because increased equity exposure would likely increase overall portfolio risk.

My original directional predictions were:

Global equity exposure would increase.

Estimated portfolio volatility would increase.

The return objective would become harder to satisfy.

Reserve coverage could decline as the optimizer adjusted the portfolio.

These predictions were based on the relative expected returns of the available investments and the constraints used in the optimization model.

The original prediction did not specify a numerical magnitude for the allocation or volatility change. Quantitative results are evaluated separately in Section 9 rather than presented as predictions made before testing.

4. Prediction Lock and GitHub Evidence

AI-off prediction status: Reported as completed before running the changed-input test.

Pre-test Git commit: Not created at the time of the original test.

I completed my AI-off prediction before running the changed-input test. However, I had not yet learned how to commit my Project 2 files to GitHub.

After completing the test, I preserved my prediction, observed results, financial analysis, and application code in the repository.

Completed-project commit: 70133a3
Commit date: November 17, 2026
Recorded timestamp: 4:09 PM EST
Commit description: Add Project 2 investment management application

This commit preserves the completed work, including the prediction and actual results.

Because the commit was created after the test, it does not independently establish the original prediction's timing. The missing pre-test Git commit remains an evidence limitation.

I do not represent this commit as proof of a prediction locked before execution.

5. Baseline Financial Assumptions

The portfolio uses four investment alternatives.

Investment

Expected Annual Return

Annual Volatility

Treasury bills

3.50%

0.50%

Treasury 10-year notes

4.30%

7.00%

Investment-grade bond fund

5.00%

6.00%

Global equity index fund

8.00%

16.00%

These are illustrative portfolio modeling assumptions rather than live market forecasts.

Expected portfolio return is calculated as:

[
E(R_p)=\sum_i w_i E(R_i)
]

Portfolio volatility is calculated as:

[
\sigma_p=\sqrt{w^\top\Sigma w}
]

where (w) represents the portfolio weights and (\Sigma) represents the covariance matrix constructed from asset volatilities and correlations.

6. Original Portfolio Results

The original optimization used the baseline financial assumptions without any return adjustment.

Investment

Original Allocation

Treasury bills

0%

Treasury 10-year notes

20%

Investment-grade bond fund

25%

Global equity index fund

55%

Total

100%

Original portfolio metrics:

Expected annual return: 6.51%

Estimated annual volatility: 9.44%

Reserve coverage: 20%

Mandate verdict: PASS CHECKABLE RULES

The original portfolio met the implemented mandate checks but exceeded the required return by only 0.01 percentage points.

7. Changed-Input Results

The expected return of each investment was reduced by 0.25 percentage points.

Investment

Original Return

Revised Return

Treasury bills

3.50%

3.25%

Treasury 10-year notes

4.30%

4.05%

Investment-grade bond fund

5.00%

4.75%

Global equity index fund

8.00%

7.75%

The optimizer then searched for a new allocation.

Investment

Revised Allocation

Treasury bills

0%

Treasury 10-year notes

5%

Investment-grade bond fund

35%

Global equity index fund

60%

Total

100%

Revised portfolio metrics:

Expected annual return: 6.52%

Estimated annual volatility: 10.36%

Reserve coverage: 5%

Mandate verdict: PASS CHECKABLE RULES

The revised portfolio still passed the currently implemented mandate checks, but its estimated volatility increased and reserve coverage declined.

8. Original Versus Changed-Input Comparison

Metric

Original

Changed Input

Difference

Expected annual return

6.51%

6.52%

+0.01 pp

Annual volatility

9.44%

10.36%

+0.92 pp

Treasury bills

0%

0%

0 pp

Treasury 10-year notes

20%

5%

−15 pp

Investment-grade bond fund

25%

35%

+10 pp

Global equity index fund

55%

60%

+5 pp

Reserve coverage

20%

5%

−15 pp

The revised allocation increased exposure to global equities and reduced exposure to Treasury 10-year notes.

The slightly higher expected portfolio return resulted from re-optimization, not an improvement in the expected returns of the underlying investments.

9. Prediction Versus Actual

Did the result match my prediction?

Yes. The results matched the predicted direction of the allocation and risk changes.

Global equity exposure increased from 55% to 60%, and estimated annual volatility increased from 9.44% to 10.36%.

The optimizer accepted greater modeled risk to compensate for lower expected returns.

Quantitative Assessment of the Prediction

The original portfolio had an expected return of 6.51%. Reducing every asset's expected return by 0.25 percentage points would lower the fixed-weight portfolio return to:

[
6.51%-0.25%=6.26%
]

This would fall below the foundation's 6.5% return objective by 0.24 percentage points.

The optimizer instead increased global equity exposure from 55% to 60%, an increase of 5 percentage points.

Estimated annual volatility rose from 9.44% to 10.36%, an increase of 0.92 percentage points.

Reserve coverage declined from 20% to 5%, a reduction of 15 percentage points.

These numerical results support the predicted direction of change. However, the original AI-off prediction did not specify a numerical magnitude for the allocation or volatility change, so the magnitudes are evaluated retrospectively rather than claimed as pre-test forecasts.

What surprised me?

I was surprised that the revised portfolio still achieved the 6.5% return objective despite the reduction in expected returns across all four assets.

However, the revised portfolio required greater equity exposure and reduced reserve coverage from 20% to 5%.

Although reserve coverage remained above the 3% minimum, the revised allocation had less flexibility if reserve requirements increased.

How did the investment decision change?

The test reinforced my recommendation to defer implementation.

The revised allocation passed the currently checkable mandate rules, but it had higher estimated volatility and lower reserve coverage.

This demonstrated that satisfying numerical constraints does not automatically make an investment strategy appropriate for implementation.

10. Discrepancy Diagnosis

The original portfolio had an expected annual return of 6.51%.

If the original portfolio weights had remained unchanged after reducing expected returns by 0.25 percentage points, the expected annual return would have been:

[
6.51%-0.25%=6.26%
]

This would have failed the foundation's 6.5% return objective.

However, the application re-optimized the portfolio instead of maintaining the original weights.

The optimizer:

Reduced Treasury 10-year note exposure from 20% to 5%.

Increased investment-grade bond exposure from 25% to 35%.

Increased global equity exposure from 55% to 60%.

These changes produced an expected annual return of 6.52%.

The difference between the 6.26% fixed-weight result and the 6.52% re-optimized result demonstrates why fixed-weight sensitivity and re-optimization can produce different outcomes.

The revised allocation achieved the return objective but required higher volatility and reduced reserve coverage.

11. Financial Interpretation

The changed-input test demonstrates that the optimizer can adapt to weaker expected-return assumptions.

However, the revised allocation involves several tradeoffs.

Higher volatility: Estimated annual volatility increased from 9.44% to 10.36%, indicating greater modeled portfolio risk.

Lower reserve coverage: Reserve coverage declined from 20% to 5%, reducing the cushion above the 3% minimum.

Narrow return cushion: The revised portfolio exceeded the 6.5% objective by only 0.02 percentage points.

These results show that small changes in financial assumptions can materially affect portfolio allocations.

The application is therefore a decision-support tool rather than an automatic investment approval system.

12. Independent Validation and Stress Testing

The portfolio validation script was executed to evaluate calculation consistency and sensitivity to adverse assumptions.

Calculation Checks

Validation Check

Result

Expected-return calculation

PASS

Portfolio-volatility calculation

PASS

Portfolio weights sum to 100%

PASS

Covariance matrix symmetry

PASS

Covariance matrix positive semidefiniteness

PASS

All five checks passed.

These checks demonstrate internal calculation consistency but do not independently establish the accuracy of the financial assumptions.

Fixed-Weight Stress Tests

Scenario

Net Return

Volatility

Verdict

Baseline

6.51%

9.44%

PASS

Returns −0.25 pp

6.26%

9.44%

FAIL

Returns −0.50 pp

6.01%

9.44%

FAIL

Volatility +25%

6.51%

11.80%

PASS

Transaction cost 10 bps

6.41%

9.44%

FAIL

Transaction cost 25 bps

6.26%

9.44%

FAIL

Reserve minimum 25%

6.51%

9.44%

FAIL

The transaction-cost scenarios apply a one-time portfolio-level cost deduction for sensitivity analysis.

The volatility scenario passed the currently checkable rules because the implemented mandate does not include a numerical volatility ceiling.

Five scenarios failed at least one checkable mandate requirement.

Process stop condition: TRUE

Reason: At least one stress scenario failed a checkable mandate rule.

The fixed-weight stress tests are distinct from the changed-input re-optimization test.

13. Final Investment Decision

Recommendation: DEFER IMPLEMENTATION

Provisional new-capital allocation: 0%.

Although the changed-input portfolio passed the currently checkable rules, it required greater estimated risk and reduced reserve coverage.

The original allocation also failed multiple adverse stress scenarios, indicating sensitivity to expected-return assumptions, implementation costs, and reserve requirements.

The investment committee should not authorize implementation until the strategy has sufficient supporting evidence and the unresolved CIO calendar-year loss rule is clarified.

14. Monitoring and Reversal Triggers

Metric

Trigger

Required Action

Expected annual return

Below 6.5%

Reject allocation or reassess assumptions

Reserve coverage

Below 3%

Reject allocation

Five-business-day liquidity

Below 90%

Reject allocation

Single-company issuer concentration

Above 8%, where applicable

Reject allocation

Annual volatility

Material deterioration relative to baseline

Review risk suitability

Transaction-cost sensitivity

Net return below 6.5%

Review implementation economics

Historical estimation windows

Materially different portfolio conclusions

Investigate model instability

CIO calendar-year loss rule

Undefined or unverified

Continue deferral

These triggers distinguish a portfolio that passes numerical constraints from one that is sufficiently robust for investment committee approval.

15. Conditions for Reconsideration

Implementation may be reconsidered only after updated financial assumptions and additional validation support the strategy.

At a minimum, the proposed portfolio must:

Produce an expected annual return of at least 6.5%.

Maintain reserve coverage of at least 3%.

Maintain five-business-day liquidity of at least 90%.

Comply with the 8% single-company issuer concentration limit, where applicable.

Be evaluated under alternative historical estimation windows and transaction-cost assumptions.

Receive a documented interpretation of the CIO's calendar-year loss rule.

Receive explicit investment committee approval.

Any unfavorable stress-test or sensitivity results must be reviewed and explained before implementation.

Proposed Review Window and Reversal Conditions

As a proposed governance procedure, the investment committee should reassess the deferred strategy within 30 calendar days after receiving the CIO's written clarification of the calendar-year loss rule.

At that review, implementation should be reconsidered only if a documented portfolio:

Achieves at least 6.5% expected annual return after modeled transaction costs.

Maintains reserve coverage of at least 3%.

Maintains five-business-day liquidity of at least 90%.

Complies with applicable issuer concentration limits.

Demonstrates acceptable results under updated assumptions and the committee's specified stress scenarios.

Meeting these conditions would permit renewed committee consideration, not automatic investment approval.

The 30-day window is a proposed review procedure, not an existing requirement of the foundation's investment mandate.

Until these conditions are satisfied, the recommendation remains DEFER, with 0% of new capital allocated to the proposed strategy.

16. Reproducibility and Evidence

GitHub Repository: https://github.com/blancoaaliah-crypto/FIN43900-Project2

Original completed-project commit: 70133a3
Commit date: November 17, 2026
Recorded timestamp: 4:09 PM EST

Relevant Files

project2_app.py — Interactive Streamlit investment application.

project2_portfolio.py — Portfolio calculations, optimization, and mandate checks.

project2_validation.py — Calculation checks and stress scenarios.

compare_windows.py — Historical estimation-window comparison.

monthly_prices.csv — Historical price data.

Project 2 validation-and-ai-use.md — Validation and AI-use documentation.

decision-memo.md — Investment committee recommendation.

clean-run-log.md — Fresh-environment reproduction evidence.

Changed-Input Reproduction Procedure

Open the Project 2 application.

Set the expected-return adjustment to 0.00 percentage points.

Record the original portfolio allocation and financial metrics.

Change the expected-return adjustment to −0.25 percentage points.

Allow the application to re-optimize.

Record the revised allocation, expected return, volatility, reserve coverage, and mandate verdict.

Compare the observed results with this document.

Clean-Environment Reproduction Evidence

On November 17, 2026, I completed a fresh-environment reproduction test using a separate GitHub clone and newly created Python virtual environment.

The test successfully reproduced all five automated mathematical validation checks, the stress-testing results, the historical estimation-window comparison, and the Streamlit application startup.

The completed reproduction log is available at:

burry/Project 2/Project 2 docs/clean-run-log.md

Git commit: a147ad8
Commit description: Add Project 2 clean-environment reproduction evidence

This provides additional evidence of technical reproducibility. It does not establish that the original AI-off prediction was committed before the changed-input test.

Evidence Limitation

The original completed-project Git commit preserves the AI-off prediction and observed results, but it does not independently verify a pre-test Git lock.

The original prediction timing therefore remains self-reported.

No later commit is presented as proof that the prediction was locked before execution.

17. Final Conclusion

The changed-input test demonstrates that the portfolio optimization application can respond to weaker expected-return assumptions by adjusting portfolio allocations.

The results matched my AI-off prediction that global equity exposure and estimated volatility would increase.

However, the revised portfolio also had reduced reserve coverage and only a narrow margin above the return objective.

The original allocation failed multiple stress scenarios, reinforcing concerns about sensitivity to financial assumptions.

Although the application identified a feasible revised allocation, the available evidence does not justify immediate implementation.

Final Investment Recommendation: DEFER IMPLEMENTATION.

Recommended New-Capital Allocation: 0% until additional validation, mandate clarification, and investment committee approval are completed.