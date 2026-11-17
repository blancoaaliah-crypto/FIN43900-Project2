Project 2 — Validation and AI-Use Record

Course: FIN 43900 — AI-Augmented Finance
Project: Meridian Foundation Reserve
Portfolio Value: $100 million
Validation Status: Completed application and scenario testing
Final Investment Decision: DEFER IMPLEMENTATION
Provisional New-Capital Allocation: 0%

GitHub Repository: https://github.com/blancoaaliah-crypto/FIN43900-Project2
Original Project Commit: 70133a3
Updated Locked Changed-Input Commit: 9d2cd66
Clean-Environment Evidence Commit: a147ad8

1. Purpose

This document records the validation activities, testing results, AI assistance, independent review, and modeling limitations associated with my Project 2 investment management application.

I developed the application using Python and Streamlit to evaluate portfolio allocations, expected returns, estimated volatility, mandate compliance, point-in-time interest-rate signals, and alternative investment scenarios.

My validation activities included:

Portfolio calculation checks.

Baseline portfolio comparisons.

Investment mandate validation.

Fixed-allocation stress testing.

AI-off prediction and changed-input testing.

Historical estimation-window sensitivity analysis.

Point-in-time interest-rate signal testing.

Review of application outputs and financial assumptions.

Fresh-environment reproduction testing.

The objective was to evaluate whether the application's calculations were internally consistent, whether the implemented mandate rules behaved as expected, and whether the financial evidence supported an investment recommendation.

2. Portfolio Calculation Validation

The application evaluates four asset classes:

Treasury bills.

10-year Treasury notes.

Investment-grade bond fund.

Global equity index fund.

Baseline Financial Assumptions

Asset

Expected Annual Return

Annual Volatility

Treasury bills

3.50%

0.50%

10-year Treasury notes

4.30%

7.00%

Investment-grade bond fund

5.00%

6.00%

Global equity index fund

8.00%

16.00%

These values are illustrative modeling assumptions rather than live market forecasts.

Portfolio expected return is calculated using:

[
E(R_p)=\sum_{i=1}^{n}w_iE(R_i)
]

Portfolio volatility is calculated using:

[
\sigma_p=\sqrt{w^\top\Sigma w}
]

Where:

(w_i) represents the allocation to asset (i).

(E(R_i)) represents the expected return of asset (i).

(\Sigma) represents the covariance matrix.

(\sigma_p) represents estimated annual portfolio volatility.

Baseline Portfolio Comparison

Portfolio

Expected Return

Annual Volatility

Inverse-volatility

3.77%

1.05%

Benchmark

6.80%

10.46%

Constrained optimized

6.51%

9.44%

The inverse-volatility portfolio produced the lowest estimated volatility but failed the 6.5% annual return objective.

The benchmark achieved a higher expected return but also had higher estimated volatility than the constrained portfolio.

The constrained optimizer selected the lowest-volatility feasible allocation found using a 5-percentage-point allocation grid.

Selected Constrained Portfolio

Asset

Allocation

Treasury bills

0%

10-year Treasury notes

20%

Investment-grade bond fund

25%

Global equity index fund

55%

Total

100%

Expected Annual Return: 6.51%
Estimated Annual Volatility: 9.44%
Reserve Coverage: 20%

The selected portfolio met the currently implemented mandate requirements but exceeded the return objective by only 0.01 percentage points.

3. Automated Calculation Validation

I executed project2_validation.py to test the internal consistency of the application's financial calculations.

Validation Results

Validation Check

Actual Result

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

Overall Result: 5 of 5 checks passed.

The expected-return check evaluated whether portfolio return was consistent with the asset weights and expected returns.

The volatility check evaluated whether the calculated portfolio volatility was consistent with the covariance-based portfolio formula.

The weight check verified that the portfolio allocation totaled 100%.

The covariance checks verified that the covariance matrix was symmetric and positive semidefinite.

These checks support the application's internal mathematical consistency.

However, passing these checks does not independently prove that the expected returns, volatilities, correlations, or historical assumptions are economically accurate.

Reproduction Command

From the Project 2 directory:

python project2_validation.py

4. Investment Mandate Validation

The Meridian Foundation Reserve has a hypothetical $100 million investment mandate.

Requirement

Mandate

Original Portfolio Result

Expected annual return

At least 6.5%

6.51% — PASS

Reserve-eligible assets

At least 3%

20% — PASS

Five-business-day liquidity

At least 90%

PASS under application assumptions

Single-company issuer concentration

Maximum 8%, where applicable

PASS under applicable exemptions

Long-only allocation

No negative weights

PASS

Total allocation

100%

PASS

Calendar-year loss rule

CIO clarification required

NOT VERIFIED

Application Verdict: PASS CHECKABLE RULES

The application distinguishes between rules it can evaluate and the CIO's unresolved calendar-year loss requirement.

The liquidity and issuer checks rely on the modeled asset universe and its assumptions, including the treatment of diversified funds and Treasury securities.

Passing the currently checkable rules does not establish that the portfolio is fully approved for investment.

5. Completed Stress Testing

I tested the original constrained portfolio under alternative financial assumptions and mandate requirements.

These stress tests maintained the original portfolio weights rather than re-optimizing the allocation.

Stress-Test Results

Scenario

Expected Return

Annual Volatility

Verdict

Original portfolio

6.51%

9.44%

PASS

Expected returns −0.25 pp

6.26%

9.44%

FAIL

Expected returns −0.50 pp

6.01%

9.44%

FAIL

Volatility +25%

6.51%

11.80%

PASS CHECKABLE RULES

Transaction cost 10 bps

6.41%

9.44%

FAIL

Transaction cost 25 bps

6.26%

9.44%

FAIL

Reserve minimum increased to 25%

6.51%

9.44%

FAIL

The transaction-cost scenarios apply one-time portfolio-level cost deductions for sensitivity analysis.

Stress-Test Interpretation

The original portfolio exceeded the 6.5% return objective by only 0.01 percentage points.

Reducing expected returns by 0.25 percentage points caused the original allocation to fail the return objective.

A 0.50-percentage-point reduction produced an even larger shortfall.

The transaction-cost scenarios also reduced the modeled return below the objective.

Increasing the minimum reserve requirement to 25% caused a failure because the original portfolio maintained only 20% reserve coverage.

Increasing asset volatilities by 25% raised estimated portfolio volatility to approximately 11.80%. This scenario passed the currently checkable mandate rules because the application does not implement a numerical volatility ceiling.

Process Stop Condition

Stop Condition: TRUE
Failed Scenarios: 5

The results demonstrate that the original portfolio's mandate compliance is sensitive to relatively small changes in financial assumptions and implementation requirements.

6. AI-Off Prediction and Changed-Input Validation

Before running the changed-input test, I completed an AI-off prediction about how the constrained portfolio would respond to a reduction in expected returns.

Original Prediction

I predicted that lowering expected returns would make it more difficult to achieve the foundation's 6.5% annual return objective.

I also expected the optimizer to increase global equity exposure because equities had the highest expected return among the four asset classes.

Finally, I expected estimated portfolio volatility to increase as the optimizer adjusted the allocation.

The original prediction was directional and did not specify numerical magnitudes for the allocation or volatility changes.

Changed-Input Test Setup

Changed Input: Expected annual returns
Original Adjustment: 0.00 percentage points
New Adjustment: −0.25 percentage points
Other Scenario Settings: Unchanged
Method: Re-optimize the portfolio

Actual Changed-Input Results

Measure

Original

Changed Input

Expected annual return

6.51%

6.52%

Annual volatility

9.44%

10.36%

Treasury bills

0%

0%

10-year Treasury notes

20%

5%

Investment-grade bonds

25%

35%

Global equities

55%

60%

Reserve coverage

20%

5%

Mandate verdict

PASS CHECKABLE RULES

PASS CHECKABLE RULES

Prediction Versus Actual Results

The actual results matched my prediction that global equity exposure and estimated portfolio volatility would increase.

Global equity exposure increased from 55% to 60%, a 5-percentage-point increase.

Estimated annual volatility increased from 9.44% to 10.36%, a 0.92-percentage-point increase.

One result that surprised me was that the re-optimized portfolio still met the 6.5% annual return objective despite the reduction in expected returns.

However, reserve coverage declined from 20% to 5%, leaving a smaller cushion above the foundation's 3% minimum.

Quantitative Assessment

If the original portfolio weights had remained unchanged, reducing every asset's expected return by 0.25 percentage points would have reduced portfolio expected return from 6.51% to 6.26%.

[
6.51%-0.25%=6.26%
]

That result would have failed the 6.5% return objective.

Instead, the optimizer constructed a new allocation.

It reduced 10-year Treasury exposure from 20% to 5%, increased investment-grade bonds from 25% to 35%, and increased global equities from 55% to 60%.

The revised portfolio achieved a 6.52% expected return, but with higher estimated volatility and lower reserve coverage.

This demonstrates the distinction between fixed-allocation sensitivity and portfolio re-optimization.

The numerical changes were measured after testing and are not presented as numerical predictions made beforehand.

Prediction Lock and GitHub Evidence

I completed the original AI-off prediction before running the changed-input test.

However, I had not yet committed my files to GitHub at that time.

The original project was subsequently committed under:

Commit: 70133a3
Date: November 17, 2026

The updated Locked Changed-Input Record was subsequently pushed under:

Commit: 9d2cd66
Description: Strengthen Project 2 changed-input evidence and reversal triggers

These commits preserve the project work and its documentation. They do not independently establish a pre-test Git lock because the original prediction and observed results were committed after testing.

The prediction, actual results, financial analysis, and evidence limitation are explained in greater detail in Project 2 Locked Changed Input.md.

7. Historical Estimation-Window Validation

I completed a historical estimation-window sensitivity analysis using monthly proxy data for:

SGOV — Treasury bill exposure.

IEF — Treasury bond exposure.

LQD — Investment-grade corporate bond exposure.

VT — Global equity exposure.

The dataset contained 63 monthly price observations and 62 monthly return observations covering January 2021 through March 2026.

I compared the original Lab 14 assumptions, the full historical sample, and the most recent 36 months.

Historical Results

Estimation Window

Portfolio

Expected Return

Volatility

Reserve Coverage

Return Objective

Lab 14 assumptions

Fixed allocation

6.51%

9.44%

20%

PASS

Full history

Fixed allocation

5.71%

11.04%

20%

FAIL

Full history

Re-optimized

6.69%

6.49%

55%

PASS

Last 36 months

Fixed allocation

10.59%

8.98%

20%

PASS

Last 36 months

Re-optimized

7.02%

2.35%

80%

PASS

The original fixed allocation produced an estimated return of 5.71% using the full historical sample, below the 6.5% objective.

Using the most recent 36 months, the same allocation produced an estimated return of 10.59%.

The re-optimized portfolios also produced substantially different results across estimation windows.

These findings demonstrate that portfolio estimates and recommended allocations are sensitive to the historical sample selected.

The analysis reinforced my concern about relying on a single set of expected-return and volatility assumptions.

Reproduction Command

python compare_windows.py

The historical proxy analysis is a sensitivity exercise, not a fully verified point-in-time investment backtest.

8. Point-in-Time Signal Validation

I implemented and tested the DGS10 daily 10-year Treasury yield series as a point-in-time interest-rate signal.

The application uses decision-date controls intended to prevent later observations from entering an earlier investment decision.

The signal evaluates Treasury yield behavior using information eligible under the application's date-selection logic.

I ran the point-in-time signal functionality and reviewed its behavior using available decision-date inputs.

This functionality helps reduce the risk of look-ahead bias.

However, the point-in-time design does not independently prove that every historical source observation was available at precisely the same time assumed by the application.

The historical ETF proxy data also have separate provenance limitations.

The DGS10 signal provides additional financial context but does not guarantee future interest-rate movements or portfolio performance.

9. Application and Code Validation

I ran the Python and Streamlit application and reviewed outputs from its portfolio construction, optimization, and validation components.

Application Components

File

Purpose

project2_app.py

Interactive Streamlit investment dashboard

project2_portfolio.py

Portfolio calculations, optimization, and mandate checks

project2_validation.py

Calculation checks and stress testing

compare_windows.py

Historical estimation-window comparisons

monthly_prices.csv

Saved historical price observations

Completed Functional Testing

I reviewed:

Portfolio weights and allocation totals.

Expected-return and volatility calculations.

Baseline strategy comparisons.

Constrained optimization.

Mandate compliance.

Fixed-allocation stress scenarios.

Changed-input re-optimization.

Historical estimation-window sensitivity.

Point-in-time interest-rate signal behavior.

Investment recommendation outputs.

The application produced results that could be compared across baseline, changed-input, stress, and historical scenarios.

The optimization method uses a discrete 5-percentage-point allocation grid.

Therefore, the application identifies the lowest-volatility feasible portfolio found on that grid, not necessarily the continuous global optimum.

10. AI Assistance and Independent Human Review

AI tools assisted with Project 2 development and documentation.

AI-Assisted Activities

AI assistance was used for:

Planning the Python and Streamlit application structure.

Developing and debugging application code.

Explaining portfolio optimization and risk-return calculations.

Organizing stress-testing and validation workflows.

Interpreting portfolio sensitivity results.

Drafting and revising project documentation.

Human Review and Testing

I ran the application, reviewed its displayed results, compared portfolio allocations, and evaluated the investment conclusions.

I examined how the optimizer responded to changed expected-return assumptions and how the portfolio behaved under different stress scenarios and historical estimation windows.

I also completed my changed-input prediction without AI assistance before running the test.

After the test, I compared my prediction with the observed results and documented the differences.

My final investment recommendation was based on the financial evidence from the completed validation.

Specific AI-Output Verification — Portfolio Expected Return

Output evaluated: The reported baseline constrained portfolio expected annual return of 6.51%.

Verification objective: Independently determine whether the reported expected return is mathematically correct using the portfolio weights and expected-return assumptions.

Verification method: Separate weighted-average calculation performed outside the Streamlit application and portfolio optimization code.

Original Portfolio Inputs

Asset

Portfolio Weight

Expected Annual Return

Treasury bills

0%

3.50%

10-year Treasury notes

20%

4.30%

Investment-grade bond fund

25%

5.00%

Global equity index fund

55%

8.00%

Total

100%



Independent Calculation

Expected portfolio return is calculated as:

[
E(R_p)=\sum_i w_iE(R_i)
]

Substituting the portfolio inputs:

[
E(R_p)=(0.00)(0.035)+(0.20)(0.043)+(0.25)(0.05)+(0.55)(0.08)
]

[
E(R_p)=0+0.0086+0.0125+0.044
]

[
E(R_p)=0.0651=6.51%
]

Verification Results

Check

Result

Reported application return

6.51%

Independently calculated return

6.51%

Difference

0.00 percentage points

Portfolio weights total

100%

Mathematical verification

PASS

AI-Output Verification Outcome

Output evaluated: The reported baseline portfolio expected annual return of 6.51%.

Independent evidence: A separate weighted-average calculation using the four asset allocations and their expected-return assumptions.

Calculated result: 6.51%.

Difference from reported output: 0.00 percentage points.

Verification decision: ACCEPT the reported numerical result as arithmetically correct under the stated assumptions.

Scope: This verification supports the expected-return calculation only. It does not validate the underlying expected-return assumptions or the optimizer's selection of portfolio weights.

Evidence limitation: The original AI-generated response or code suggestion associated with this output has not yet been identified. Therefore, the calculation is independently verified, but the connection to a specific AI output remains incomplete.

Financial Interpretation

The portfolio meets the foundation's 6.5% annual expected-return objective by only 0.01 percentage points.

Although the calculation is correct, the narrow margin makes the investment decision sensitive to changes in expected returns and transaction costs.

For example, reducing every asset's expected return by 0.25 percentage points while maintaining the original weights lowers the portfolio return to 6.26%, which fails the mandate.

This supports the recommendation to defer implementation until the portfolio's assumptions and risk exposure have been evaluated further.

Scope of Verification

This check confirms the arithmetic of the reported expected return. It does not independently establish the accuracy of the expected-return assumptions or validate the entire optimization algorithm.

The original AI-generated response or code suggestion associated with this calculation still needs to be identified in the supporting evidence so the verification can be traced to a specific AI output.

11. Reproducibility and GitHub Evidence

Repository: https://github.com/blancoaaliah-crypto/FIN43900-Project2

Original Project Commit: 70133a3

Updated Locked Changed-Input Documentation Commit: 9d2cd66

Clean-Environment Evidence Commit: a147ad8

Reproduction Commands

From the Project 2 directory:

python -m pip install -r requirements.txt
python project2_validation.py
python compare_windows.py
python -m streamlit run project2_app.py

These commands allow the calculation checks, historical comparison, and interactive application to be rerun in an appropriately configured Python environment.

Completed Clean-Environment Reproduction

On November 17, 2026, I completed a fresh-environment reproduction test using a separate GitHub clone and newly created Python virtual environment.

The test successfully reproduced all five automated mathematical validation checks, the fixed-weight stress-testing results, and the historical estimation-window comparison. The Streamlit application also launched successfully.

The reproduction procedure and observed results are documented in:

burry/Project 2/Project 2 docs/clean-run-log.md

Evidence commit: a147ad8

This demonstrates that the project can be installed and executed outside my original development environment.

The test was performed by the developer, not an independent external reviewer.

The clean-run log documents the procedure and reported results. A separately preserved raw terminal transcript would provide stronger evidence of the complete execution history.

The repository provides a record of the project code and documentation, but the original Git history does not independently establish the pre-test prediction timing.

12. Model Limitations and Unresolved Issues

The completed validation identified several limitations.

Expected-return uncertainty: The original constrained portfolio exceeded the 6.5% objective by only 0.01 percentage points.

Optimization sensitivity: The changed-input test produced a different allocation with higher estimated volatility and lower reserve coverage.

Historical-window sensitivity: Expected returns and volatility estimates varied substantially across historical estimation windows.

Model assumptions: Expected returns, volatility, correlations, and the discrete allocation grid influence the selected portfolio.

Transaction costs: The stress-test costs are modeled as one-time portfolio-level deductions rather than a full ongoing implementation-cost model.

Data provenance: Historical ETF proxy data remain subject to limitations in source timing and point-in-time reproducibility.

Mandate coverage: The modeled liquidity and issuer-concentration checks depend on assumptions about the asset universe.

Calendar-year loss rule: The CIO has not defined the rule sufficiently for the application to verify compliance.

AI verification evidence: The independent portfolio-return calculation is documented, but the original specific AI output still needs to be linked to that verification.

Git evidence: The original prediction was completed before testing, but the Git commits were created afterward.

Reproducibility: A clean-environment test was completed successfully on November 17, 2026. The application, mathematical checks, stress scenarios, and historical comparison were reproduced in a fresh Python environment. This establishes developer-performed technical reproducibility but does not constitute independent third-party validation.

These limitations define the boundaries of the completed testing rather than indicating that the application was never tested.

13. Final Validation Assessment and Investment Decision

The completed validation demonstrated that the application can:

Compare portfolio strategies.

Calculate portfolio risk and expected return.

Evaluate implemented mandate requirements.

Respond to changed assumptions.

Display stress-test results.

Compare historical estimation windows.

Incorporate a point-in-time interest-rate signal.

The original constrained portfolio achieved:

Expected Annual Return: 6.51%
Estimated Annual Volatility: 9.44%
Reserve Coverage: 20%
Mandate Verdict: PASS CHECKABLE RULES

However, stress testing showed that the portfolio's return cushion was narrow.

The changed-input test demonstrated that preserving the return objective could require increased volatility and reduced reserve coverage.

The historical estimation-window analysis also demonstrated substantial sensitivity to the selected historical period.

These findings support my investment recommendation.

Final Investment Recommendation: DEFER IMPLEMENTATION

Provisional Allocation of New Capital: 0%

The investment committee should reconsider implementation only after updated assumptions, additional validation, and clarification of the CIO's calendar-year loss rule support approval.

The proposed review procedure is to reassess the strategy within 30 calendar days after receiving the CIO's written clarification.

Any reconsidered portfolio must meet the applicable mandate constraints and demonstrate an expected annual return of at least 6.5% after modeled transaction costs.

Meeting these conditions would allow committee reconsideration, not automatic approval.

The recommendation reflects the financial evidence and model limitations identified through testing.

14. AI and Educational Disclosure

This project is an educational investment management simulation and does not constitute investment advice.

AI tools assisted with application development, debugging, financial explanations, and documentation.

I ran and reviewed the application's outputs, completed an AI-off changed-input prediction before testing, and evaluated the validation findings used to support my investment recommendation.

The independently calculated expected return of 6.51% matches the application's reported baseline result.

AI-generated code and explanations were not treated as independently verified simply because they were produced by an AI tool.

The calculation checks, stress tests, changed-input comparison, historical analysis, clean-environment reproduction, and documented limitations provide the basis for evaluating the application's outputs.

Final Conclusion: The application is useful as an investment decision-support tool, but the available financial evidence supports deferring implementation rather than immediately allocating foundation capital.