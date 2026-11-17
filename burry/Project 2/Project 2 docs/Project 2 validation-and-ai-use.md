Project 2 — Validation and AI Use Record

Course: FIN 43900 — AI-Augmented Finance
Project: Meridian Foundation Reserve
Portfolio Value: $100 million
Validation Status: Completed application and scenario testing
Final Investment Decision: Defer Implementation

1. Purpose

This document records the validation activities, testing results, AI assistance, and limitations associated with my Project 2 investment management application.

I developed the application using Python and Streamlit to evaluate portfolio allocations, expected returns, estimated volatility, mandate compliance, point-in-time interest rate signals, and alternative investment scenarios.

I completed independent validation through application testing, baseline comparisons, stress testing, changed-input testing, historical estimation-window sensitivity analysis, and point-in-time signal testing.

I also completed an AI-off prediction before running my changed-input test and compared that prediction against the application's actual results.

The purpose of the validation was to evaluate whether the application's calculations and outputs were consistent, whether the implemented mandate rules behaved as expected, and whether the proposed portfolio supported an investment recommendation.

2. Portfolio Calculation Validation

The application evaluates four asset classes:

Treasury bills

10-year Treasury notes

Investment-grade bond fund

Global equity index fund

I reviewed the application's portfolio calculations and compared equal-weight, inverse-volatility, benchmark, and constrained optimized portfolios.

Baseline Results

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

The inverse-volatility portfolio produced lower estimated volatility but did not meet the 6.5% annual return objective.

The benchmark achieved a higher expected return but had greater estimated volatility than the constrained portfolio.

The constrained optimizer selected the following allocation:

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

The selected allocation produced an expected annual return of 6.51% and estimated volatility of 9.44%.

I reviewed the portfolio weights, risk estimates, and return calculations as part of my completed validation.

These comparisons helped establish that the application produced consistent portfolio outputs under the stated assumptions.

3. Mandate Validation

I evaluated the constrained portfolio against the Meridian Foundation Reserve investment mandate.

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

Issuer concentration

Maximum 8%

PASS under applicable exemptions

Long-only allocation

No negative weights

PASS

Total allocation

100%

PASS

The application reported PASS CHECKABLE RULES for the original constrained portfolio.

I reviewed the mandate checks and their limitations.

The CIO's calendar-year loss rule remains undefined, so the application does not claim to have verified compliance with that requirement.

The mandate verdict applies only to the rules that are currently implemented and checkable.

4. Completed Stress Testing

I tested the original constrained portfolio under alternative expected-return assumptions, transaction costs, and reserve requirements.

The scenarios included:

A 0.25 percentage-point reduction in expected returns.

A 0.50 percentage-point reduction in expected returns.

Transaction cost assumptions of 10 basis points.

Transaction cost assumptions of 25 basis points.

An increase in the minimum reserve requirement to 25%.

Stress-Test Results

Scenario

Expected Return or Result

Verdict

Original portfolio

6.51%

PASS

Expected returns reduced by 0.25 percentage points

6.26%

FAIL

Expected returns reduced by 0.50 percentage points

6.01%

FAIL

10-basis-point return cost

6.41%

FAIL

25-basis-point return cost

6.26%

FAIL

Reserve minimum increased to 25%

Original coverage remains 20%

FAIL

These results reflect fixed-allocation sensitivity calculations rather than re-optimization.

The original portfolio exceeded the 6.5% return objective by only 0.01 percentage points.

The return reduction scenarios demonstrated that relatively small changes in assumptions caused the original allocation to fail the objective.

The increased reserve requirement also caused the original allocation to fail because its reserve coverage was 20%.

These tests confirmed that the portfolio's initial mandate compliance was sensitive to changes in assumptions.

5. AI-Off Prediction and Changed-Input Validation

Before running the changed-input test, I completed an AI-off prediction about how the constrained portfolio would respond to a reduction in expected returns.

I predicted that lowering expected returns would make it more difficult to achieve the 6.5% annual objective.

I also predicted that the optimizer would increase the allocation to global equities because equities had the highest expected return among the four asset classes.

Finally, I expected estimated portfolio volatility to increase as the optimizer adjusted the allocation to compensate for the lower expected-return assumptions.

Changed-Input Test Setup

Changed input: Expected returns
Original adjustment: 0.00 percentage points
New adjustment: −0.25 percentage points
Other scenario settings: Unchanged

After completing my prediction, I ran the changed-input test and reviewed the application's results.

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

PASS

PASS

Prediction Versus Actual Results

The actual results matched my prediction that the optimizer would increase the allocation to global equities and that estimated portfolio volatility would rise.

Global equity allocation increased from 55% to 60%, while annual volatility increased from 9.44% to 10.36%.

One result that surprised me was that the re-optimized portfolio still met the 6.5% annual return objective despite the reduction in expected returns.

The portfolio achieved a revised expected return of 6.52%.

However, reserve coverage declined from 20% to 5%, leaving a smaller cushion above the 3% minimum.

Discrepancy Diagnosis

If the original portfolio weights had remained unchanged, reducing all asset expected returns by 0.25 percentage points would have lowered the portfolio's expected return from 6.51% to 6.26%.

That result would have failed the foundation's return objective.

However, the application re-optimized the allocation.

The optimizer reduced the 10-year Treasury allocation from 20% to 5%, increased investment-grade bonds from 25% to 35%, and increased global equities from 55% to 60%.

These changes allowed the revised portfolio to achieve a 6.52% expected return, although estimated volatility increased.

This demonstrated the difference between testing a fixed portfolio and allowing an optimizer to construct a new allocation.

I documented my prediction, observed results, and discrepancy diagnosis in the separate Project 2 — Locked Changed-Input Record.

The AI-off prediction was completed before the test. Any required pre-test Git commit evidence is a separate record that must be supported by the repository history.

6. Historical Estimation-Window Validation

I completed a historical estimation-window sensitivity analysis using monthly proxy data for SGOV, IEF, LQD, and VT.

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

The original fixed allocation produced an expected return of 5.71% using the full historical sample, below the 6.5% objective.

Using the last 36 months, the same allocation produced an estimated return of 10.59%.

The re-optimized portfolios also produced substantially different results across estimation windows.

This analysis demonstrated that the portfolio's estimated performance depends significantly on the historical sample selected.

The results reinforced my concern about relying on a single set of expected-return and volatility assumptions.

7. Point-in-Time Signal Validation

I implemented and tested the DGS10 daily 10-year Treasury yield series as a point-in-time interest rate signal.

The application uses decision-date controls intended to prevent later observations from entering an earlier investment decision.

This is important because look-ahead bias can make historical investment decisions appear more accurate than they would have been using information actually available at the time.

I ran the point-in-time signal functionality and reviewed its behavior using the available decision-date inputs.

The DGS10 signal provides additional context for the investment process but does not guarantee future interest rate movements or portfolio performance.

The historical ETF proxy data have separate provenance limitations and are not represented as a fully verified point-in-time trading backtest.

8. Application and Code Validation

I ran the Python and Streamlit application and reviewed the outputs from its portfolio construction and validation components.

My completed testing covered:

Portfolio allocation calculations and weight totals.

Expected return and estimated volatility calculations.

Equal-weight and inverse-volatility baseline comparisons.

Constrained optimization and mandate checks.

Fixed-allocation stress scenarios.

Changed-input re-optimization.

Historical estimation-window sensitivity.

Point-in-time DGS10 signal behavior.

Investment recommendation outputs.

The application produced results that could be compared across baseline, stress, changed-input, and historical scenarios.

I reviewed these results to identify differences, evaluate mandate compliance, and determine whether the portfolio supported implementation.

The completed tests demonstrated the application's functionality while also identifying important modeling limitations.

9. AI Assistance and Independent Human Review

AI tools assisted with Project 2 development and documentation.

AI-Assisted Activities

AI assistance was used for:

Planning the Python and Streamlit application structure.

Developing and debugging application code.

Explaining portfolio optimization and risk-return calculations.

Organizing the stress-testing and validation workflow.

Interpreting portfolio sensitivity results.

Drafting and revising project documentation.

Independent Human Review

I independently ran the application, reviewed the displayed results, compared portfolio allocations, and evaluated the investment conclusions.

I examined how the optimizer responded to changed expected-return assumptions and how the portfolio behaved under different stress scenarios and historical estimation windows.

I also completed my changed-input prediction without AI assistance before running the test.

After the test, I compared my original prediction with the observed results and documented the differences.

My final investment recommendation was based on the results of the completed validation.

AI assistance supported the development and explanation process but did not replace my responsibility to test the application and evaluate the investment decision.

10. Model Limitations and Unresolved Issues

The completed validation identified several limitations.

Expected-return uncertainty: The original constrained portfolio exceeded the 6.5% objective by only 0.01 percentage points.

Optimization sensitivity: The changed-input test produced a different allocation with higher estimated volatility and lower reserve coverage.

Historical-window sensitivity: Expected returns and volatility estimates varied substantially across historical estimation windows.

Model assumptions: Expected returns, volatility, correlations, and the optimizer's discrete allocation grid influence the selected portfolio.

Data provenance: Historical ETF proxy data remain subject to limitations in source timing and point-in-time reproducibility.

Calendar-year loss rule: The CIO has not defined the rule sufficiently for the application to evaluate it.

These limitations were identified through the completed validation process. They do not mean that the application testing was left unfinished.

11. Final Validation Assessment and Investment Decision

The completed validation demonstrated that the application can compare portfolio strategies, evaluate implemented mandate rules, respond to changed assumptions, and display stress-test and historical sensitivity results.

The original constrained portfolio achieved a 6.51% expected annual return with 9.44% estimated volatility and passed the currently checkable mandate requirements.

However, stress testing showed that the portfolio's return cushion was narrow.

The changed-input test demonstrated that preserving the return objective could require increased volatility and reduced reserve coverage.

The historical estimation-window analysis also demonstrated substantial sensitivity to the selected historical period.

Final investment recommendation: Defer implementation.

Provisional allocation of new capital: 0%.

This recommendation reflects my completed validation findings rather than a lack of testing.

The committee should reconsider implementation when the strategy's assumptions are sufficiently robust for the mandate and the CIO clarifies the calendar-year loss rule.

AI and Educational Disclosure

This project is an educational investment management simulation and does not constitute investment advice.

AI tools assisted with application development, debugging, explanation, and documentation. I independently ran and reviewed the application's outputs, completed an AI-off changed-input prediction before testing, and evaluated the validation findings used to support my investment recommendation.

AI-generated code and explanations were not treated as independently verified simply because they were produced by an AI tool.