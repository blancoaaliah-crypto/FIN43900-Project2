Project 2 — Investment Committee Decision Memo

Course: FIN 43900 — AI-Augmented Finance
Project: Meridian Foundation Reserve
Portfolio Value: $100 million
Final Investment Recommendation: DEFER IMPLEMENTATION
Provisional New-Capital Allocation: 0%

GitHub Repository: https://github.com/blancoaaliah-crypto/FIN43900-Project2

1. Executive Summary

The Meridian Foundation Reserve is a hypothetical $100 million investment portfolio with a 6.5% annual expected-return objective. The portfolio must also satisfy requirements involving liquidity, reserve coverage, issuer concentration, and long-only investment allocations.

For Project 2, I developed a Python and Streamlit investment management application that compares portfolio construction methods, evaluates investment mandate compliance, incorporates a point-in-time interest-rate signal, and tests portfolio performance under changing financial assumptions.

The constrained portfolio produced an expected annual return of 6.51%, estimated annual volatility of 9.44%, and reserve-eligible coverage of 20%. Although this portfolio passed the currently checkable mandate requirements, its expected return exceeded the foundation's 6.5% objective by only 0.01 percentage points.

I completed independent validation through automated calculation checks, baseline comparisons, stress testing, changed-input testing, historical estimation-window sensitivity analysis, and application output review.

The validation identified three significant concerns:

The original portfolio failed the return objective when expected returns were reduced by only 0.25 percentage points while maintaining the original allocation.

Re-optimization under lower expected-return assumptions required greater global equity exposure, increased estimated volatility, and reduced reserve coverage.

Historical estimation-window comparisons produced substantially different expected returns, volatility estimates, and portfolio allocations.

Additionally, the CIO's calendar-year loss rule remains unresolved, preventing complete confirmation of investment mandate compliance.

Final Recommendation: DEFER IMPLEMENTATION.

I recommend allocating 0% of new capital to the proposed constrained portfolio until the foundation's unresolved mandate requirement is clarified and additional analysis supports a more robust investment strategy.

This recommendation is based on the completed financial validation rather than an absence of testing.

2. Investment Mandate and Portfolio Requirements

The Meridian Foundation Reserve operates under the following hypothetical investment requirements.

Requirement

Investment Mandate

Portfolio value

$100 million

Annual expected-return objective

At least 6.5%

Minimum reserve-eligible assets

3%

Five-business-day liquidity

At least 90%

Maximum single-company issuer concentration

8%, subject to applicable exemptions

Portfolio allocation

Long-only; weights must total 100%

Calendar-year loss requirement

CIO clarification required

The application evaluates the requirements that can currently be expressed as numerical or classification-based constraints.

Treasury securities and diversified investment funds are treated as exempt from the individual issuer concentration restriction under the application's assumptions.

The application also evaluates liquidity using the modeled asset classifications and five-business-day liquidity assumptions.

However, the CIO's calendar-year loss requirement has not been sufficiently defined to determine compliance.

As a result, the application's PASS CHECKABLE RULES verdict should not be interpreted as full investment committee approval.

The distinction between mathematical feasibility and investment suitability is central to my final recommendation.

3. Portfolio Construction and Baseline Comparison

The application evaluates four asset classes:

Treasury bills.

10-year Treasury notes.

Investment-grade bond fund.

Global equity index fund.

The baseline annual expected-return assumptions are:

Asset Class

Expected Annual Return

Treasury bills

3.50%

10-year Treasury notes

4.30%

Investment-grade bond fund

5.00%

Global equity index fund

8.00%

These figures are illustrative modeling assumptions rather than guaranteed future investment returns.

I compared equal-weight, inverse-volatility, benchmark, and constrained optimized portfolio construction approaches.

The equal-weight approach allocates 25% to each asset.

The inverse-volatility approach emphasizes assets with lower estimated volatility, while the benchmark uses 40% investment-grade bonds and 60% global equities.

The constrained optimizer searches a 5-percentage-point allocation grid for the lowest-volatility portfolio satisfying the implemented investment requirements.

Baseline Strategy Comparison

Portfolio Strategy

Expected Annual Return

Annual Volatility

Inverse-volatility portfolio

3.77%

1.05%

Benchmark portfolio

6.80%

10.46%

Constrained optimized portfolio

6.51%

9.44%

The inverse-volatility portfolio had the lowest estimated volatility but failed the foundation's 6.5% return objective.

The benchmark exceeded the return objective but had higher estimated volatility than the constrained optimized portfolio.

The constrained optimizer selected a portfolio that met the currently implemented requirements while reducing estimated volatility relative to the benchmark.

Selected Constrained Portfolio

Asset Class

Portfolio Allocation

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
Reserve-Eligible Coverage: 20%
Application Verdict: PASS CHECKABLE RULES

The portfolio achieved the return objective but maintained only a narrow expected-return margin.

This creates a concern because even small changes in market assumptions or implementation costs could cause the strategy to fall below the foundation's objective.

The selected allocation is also the lowest-volatility feasible portfolio identified within the application's discrete search grid, not necessarily the continuous global optimum.

4. Point-in-Time Interest-Rate Signal

I incorporated the DGS10 daily 10-year Treasury yield series into the application as a point-in-time interest-rate signal.

The purpose of this feature is to provide additional financial context while reducing the risk of look-ahead bias.

Look-ahead bias occurs when information that was not available at the time of an investment decision is incorrectly included in the analysis.

The application's decision-date controls are designed to restrict the signal to observations eligible as of the selected investment date.

I implemented and tested this functionality as part of the application validation process.

The interest-rate signal can help explain changing Treasury market conditions and provide context for fixed-income allocation decisions.

However, the DGS10 signal does not guarantee future interest-rate movements, bond returns, or portfolio performance.

Additionally, the historical ETF proxy data used elsewhere in the project have separate data-availability limitations and should not be interpreted as a fully verified point-in-time trading record.

Therefore, the signal is best treated as a supporting investment decision tool rather than an independent basis for allocating foundation capital.

5. Completed Stress Testing

I tested the original constrained portfolio under alternative financial assumptions and investment requirements.

These scenarios maintained the original portfolio weights to isolate the impact of changing individual assumptions.

Stress-Test Results

Scenario

Expected Return

Annual Volatility

Mandate Result

Original portfolio

6.51%

9.44%

PASS

Expected returns reduced 0.25 pp

6.26%

9.44%

FAIL

Expected returns reduced 0.50 pp

6.01%

9.44%

FAIL

Asset volatility increased 25%

6.51%

11.80%

PASS CHECKABLE RULES

Transaction cost of 10 bps

6.41%

9.44%

FAIL

Transaction cost of 25 bps

6.26%

9.44%

FAIL

Minimum reserve requirement increased to 25%

6.51%

9.44%

FAIL

Stress-Test Summary: Five of seven scenarios failed at least one currently checkable requirement.

Expected-Return Sensitivity

The original constrained portfolio generated an expected annual return of 6.51%, exceeding the foundation's return objective by only 0.01 percentage points.

Reducing expected returns by 0.25 percentage points lowered the fixed portfolio's expected return to 6.26%.

A 0.50-percentage-point reduction lowered expected return to 6.01%.

Both scenarios failed the 6.5% objective.

These results indicate that the original portfolio's compliance depends heavily on the assumed asset returns.

Transaction-Cost Sensitivity

The application also evaluated transaction-cost assumptions of 10 and 25 basis points.

Under the simplified one-time cost deduction used in the stress test, expected portfolio return declined to 6.41% and 6.26%, respectively.

Both results fell below the return objective.

Although these scenarios do not represent a complete ongoing implementation-cost model, they demonstrate that a narrow expected-return margin leaves little room for expenses.

Reserve and Volatility Sensitivity

Increasing the minimum reserve requirement to 25% caused the original portfolio to fail because reserve-eligible coverage remained at 20%.

Increasing asset volatilities by 25% raised estimated portfolio volatility from 9.44% to approximately 11.80%.

The volatility scenario continued to pass the currently checkable rules because the application does not implement a numerical volatility ceiling.

However, passing that test does not mean the increased volatility is necessarily acceptable to the investment committee.

Stress-Test Interpretation

The stress tests demonstrate that the original portfolio is mathematically feasible under the baseline assumptions but is not particularly robust to changes in expected returns, implementation costs, or reserve requirements.

The results support further review before committing capital.

6. AI-Off Prediction and Changed-Input Test

I completed an AI-off prediction before running a changed-input test.

I predicted that reducing expected asset returns would make the foundation's 6.5% objective more difficult to achieve.

I also expected the optimizer to increase global equity exposure because equities had the highest modeled expected return.

Finally, I expected estimated portfolio volatility to increase.

Changed-Input Scenario

The expected annual return of each asset was reduced by 0.25 percentage points.

Unlike the fixed-allocation stress tests, this scenario allowed the optimizer to construct a new portfolio.

Actual Changed-Input Results

Measure

Original Portfolio

Re-Optimized Portfolio

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

PASS

PASS

Financial Interpretation

The optimizer increased global equity exposure from 55% to 60% and reduced 10-year Treasury exposure from 20% to 5%.

It also increased investment-grade bond exposure from 25% to 35%.

The revised allocation achieved an expected annual return of 6.52%, allowing it to continue satisfying the 6.5% return objective.

However, estimated annual volatility increased from 9.44% to 10.36%.

Reserve coverage declined from 20% to 5%, leaving only a 2-percentage-point cushion above the foundation's minimum reserve requirement.

The observed increase in global equity exposure and portfolio volatility matched my original prediction.

The surprising result was that the optimizer could still meet the return objective after reducing expected asset returns.

This occurred because the optimizer changed the portfolio allocation rather than maintaining the original weights.

If the original allocation had remained unchanged, expected return would have declined to 6.26%, failing the objective.

The changed-input results illustrate an important investment tradeoff: an optimizer may preserve a target expected return by accepting higher estimated volatility and reducing other financial cushions.

The test reinforced my recommendation to defer implementation.

Prediction Evidence Limitation

The AI-off prediction was completed before running the changed-input test.

However, it was not committed to GitHub before the test occurred.

The later GitHub commits preserve the prediction, results, and analysis but do not independently prove the prediction's pre-test timing.

This limitation is disclosed in the separate Locked Changed-Input Record.

7. Historical Estimation-Window Sensitivity Analysis

I completed a historical estimation-window sensitivity analysis using monthly proxy data for four exchange-traded funds:

SGOV — Treasury bill exposure.

IEF — Treasury bond exposure.

LQD — Investment-grade corporate bond exposure.

VT — Global equity exposure.

The dataset contained 63 monthly price observations and 62 monthly return observations covering January 2021 through March 2026.

I compared the original Lab 14 assumptions, the full historical sample, and the most recent 36 months.

Historical Comparison Results

Estimation Window

Portfolio

Expected Return

Annual Volatility

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

Historical Results and Interpretation

The original fixed allocation produced an estimated annual return of 5.71% when evaluated using the full historical sample.

This failed the foundation's 6.5% annual expected-return objective.

However, the same portfolio produced an estimated annual return of 10.59% using the most recent 36 months.

The re-optimized portfolios also produced materially different results depending on the historical estimation window.

Under the full historical sample, the re-optimized portfolio produced an expected return of 6.69%, estimated volatility of 6.49%, and reserve coverage of 55%.

Using the most recent 36 months, the re-optimized portfolio produced an expected return of 7.02%, estimated volatility of 2.35%, and reserve coverage of 80%.

These differences demonstrate that historical estimation-window selection can substantially influence both portfolio estimates and recommended allocations.

The higher return estimated from the most recent 36 months should not be interpreted as a reliable forecast of future performance.

Instead, the results illustrate the risk of drawing investment conclusions from one historical sample.

The historical analysis is a sensitivity exercise rather than a fully verified point-in-time investment backtest.

Investment Implication

The foundation should not rely exclusively on one historical period when selecting expected returns, estimating volatility, or determining portfolio weights.

The large variation across estimation windows strengthens the case for additional robustness testing before implementation.

8. Independent Validation and AI-Output Verification

I completed several validation activities to assess the application's mathematical consistency, financial assumptions, and investment outputs.

Automated Calculation Validation

I executed project2_validation.py to test the application's portfolio calculations.

Automated Check

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

Automated Validation Result: 5 of 5 checks passed.

These results support the internal mathematical consistency of the application's calculations.

However, successful mathematical checks do not independently establish that the financial assumptions are accurate or that the resulting portfolio is suitable for implementation.

Independent Expected-Return Verification

I also independently calculated the expected return of the original constrained portfolio.

The expected-return formula is:

[
E(R_p)=\sum_i w_iE(R_i)
]

Using the original portfolio weights and expected returns:

[
E(R_p)=(0.00)(0.035)+(0.20)(0.043)+(0.25)(0.05)+(0.55)(0.08)
]

[
E(R_p)=0+0.0086+0.0125+0.044
]

[
E(R_p)=0.0651=6.51%
]

The independently calculated return matched the application's reported expected return of 6.51%.

Verification Result: PASS

This confirms the arithmetic of the expected-return calculation under the stated assumptions.

It does not independently verify the accuracy of those assumptions or establish that the optimizer has identified the best possible real-world portfolio.

The original specific AI-generated output associated with this calculation has not yet been linked to the verification record.

Additional Independent Validation

I also reviewed:

Baseline strategy comparisons.

Mandate compliance results.

Fixed-allocation stress-test scenarios.

Changed-input re-optimization.

Historical estimation-window comparisons.

Point-in-time interest-rate signal functionality.

Streamlit application outputs.

Together, these activities provided evidence about the application's strengths and limitations.

The validation results demonstrate that the application can support investment analysis while also identifying weaknesses in the assumptions underlying the investment recommendation.

9. Investment Committee Decision and Rationale

Final Recommendation: DEFER IMPLEMENTATION

Provisional New-Capital Allocation: 0%

Based on the completed validation, I do not recommend immediately allocating foundation capital to the proposed constrained portfolio.

The decision is supported by five primary findings.

1. Insufficient Expected-Return Cushion

The original portfolio produced an expected annual return of 6.51%.

This exceeded the foundation's 6.5% objective by only 0.01 percentage points.

Such a narrow margin provides little protection against estimation errors or implementation costs.

2. Sensitivity to Lower Expected Returns

Reducing expected asset returns by only 0.25 percentage points caused the original fixed portfolio to fail the return objective.

This indicates that the portfolio's baseline compliance is sensitive to the assumed financial inputs.

3. Increased Risk Under Re-Optimization

The changed-input test demonstrated that the optimizer could maintain the return objective by increasing global equity exposure.

However, estimated volatility increased from 9.44% to 10.36%, and reserve coverage declined from 20% to 5%.

The revised allocation maintained numerical feasibility but reduced the portfolio's risk and reserve cushions.

4. Historical Estimation Uncertainty

The historical sensitivity analysis produced substantially different portfolio estimates across the full historical sample and the most recent 36 months.

This suggests that the portfolio recommendation depends significantly on the estimation window and underlying assumptions.

5. Incomplete Mandate Clarification

The CIO's calendar-year loss requirement remains unresolved.

Although the portfolio passed the currently checkable mandate rules, full compliance cannot be established until this requirement is defined and evaluated.

Conditions for Reconsidering Implementation

Before reconsidering the proposed portfolio, the investment committee should require:

CIO clarification: Define the calendar-year loss rule and determine how compliance will be evaluated.

Updated assumptions: Review expected returns, volatilities, correlations, and the selected estimation windows.

Robustness testing: Evaluate additional adverse scenarios, including realistic transaction costs and alternative portfolio allocations.

Liquidity and concentration review: Confirm that the modeled liquidity and issuer exemptions accurately reflect the foundation's investment requirements.

Reproducibility review: Confirm that the application and supporting calculations can be reproduced from the repository in a fresh environment.

These conditions provide a path toward a future investment decision without prematurely approving the current allocation.

10. Reproducibility, Evidence, and Model Limitations

The Project 2 GitHub repository contains the application and supporting project documentation.

Repository: https://github.com/blancoaaliah-crypto/FIN43900-Project2

The supporting documentation includes:

Project 2 Validation and AI-Use Record.

Project 2 Locked Changed-Input Record.

Application code and portfolio calculations.

Automated validation and historical comparison scripts.

The Validation and AI-Use Record contains additional details about the automated checks, stress scenarios, changed-input testing, AI assistance, and independent review.

The Locked Changed-Input Record documents the original AI-off prediction, changed assumptions, observed results, and timing limitation.

The project has several limitations that should be considered when interpreting its results.

The portfolio uses modeled expected returns, volatility assumptions, and correlations rather than guaranteed future returns.

The optimizer searches a discrete allocation grid rather than solving for an unrestricted continuous optimum.

Historical ETF proxy results are sensitive to the sample period and are not a fully verified point-in-time backtest.

The liquidity and issuer-concentration checks rely on modeled assumptions and exemptions.

The CIO's calendar-year loss rule remains unresolved.

Although the application has been run and tested in the development environment, a fully documented fresh-environment reproduction remains to be completed.

These limitations do not invalidate the completed calculations, but they restrict the conclusions that can reasonably be drawn from them.

11. Final Conclusion

Project 2 demonstrated how a Python and Streamlit investment management application can combine portfolio optimization, mandate compliance checks, point-in-time information, stress testing, and historical sensitivity analysis to support investment committee decisions.

The original constrained portfolio achieved an expected annual return of 6.51% and estimated annual volatility of 9.44%.

It also passed the currently checkable investment mandate requirements.

However, my independent validation demonstrated that the portfolio's results were sensitive to expected-return assumptions, transaction costs, reserve requirements, and historical estimation windows.

The changed-input test showed that preserving the expected-return objective could require greater global equity exposure, increased estimated volatility, and reduced reserve coverage.

The historical analysis further demonstrated that portfolio estimates and recommended allocations can change substantially depending on the sample period used.

The unresolved calendar-year loss rule also prevents full confirmation of investment mandate compliance.

For these reasons, my final recommendation is to DEFER IMPLEMENTATION and allocate 0% of new capital to the proposed portfolio until the identified concerns have been addressed.

This decision reflects the importance of evaluating portfolio robustness, investment mandate compliance, and model limitations rather than relying solely on an optimizer's initial result.

AI and Educational Disclosure

This project is an educational investment management simulation and does not constitute investment advice.

AI tools assisted with application development, debugging, financial explanations, and documentation.

I ran and reviewed the application's outputs, completed an AI-off changed-input prediction before testing, independently verified the baseline expected-return calculation, and evaluated the financial findings supporting my final investment recommendation.

The completed validation results, supporting documentation, and disclosed limitations form the basis for the investment committee decision.