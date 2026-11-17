Project 2 — Investment Committee Decision Memo

Course: FIN 43900 — AI-Augmented Finance
Project: Meridian Foundation Reserve
Portfolio Value: $100 million
Final Recommendation: Defer Implementation

1. Executive Summary

The Meridian Foundation Reserve is a $100 million investment portfolio with an annual return objective of 6.5%. The portfolio must also satisfy requirements for liquidity, reserve coverage, issuer concentration, and long-only investment allocations.

For Project 2, I developed a Streamlit investment management application that compares portfolio construction methods, evaluates mandate compliance, incorporates a point-in-time interest rate signal, and tests portfolio performance under different assumptions.

I completed independent validation through baseline comparisons, stress testing, changed-input testing, historical estimation-window sensitivity analysis, and application output checks.

The constrained portfolio produced an expected annual return of 6.51% and estimated annual volatility of 9.44%. Although it passed the currently checkable mandate requirements, its expected return exceeded the 6.5% objective by only 0.01 percentage points.

My completed validation showed that the portfolio's performance and allocation are sensitive to expected-return assumptions and historical estimation windows.

My final recommendation is to defer implementation and allocate 0% of new capital to the proposed strategy.

This decision is based on the validation results rather than an absence of testing.

2. Investment Mandate

The Meridian Foundation Reserve has the following requirements:

Requirement

Mandate

Portfolio value

$100 million

Annual return objective

6.5%

Minimum reserve-eligible assets

3%

Five-business-day liquidity

At least 90%

Maximum issuer concentration

8%

Portfolio allocation

Long-only; weights total 100%

Treasury securities and diversified investment funds are treated as exempt from the individual issuer concentration restriction under the application's assumptions.

The CIO's calendar-year loss rule remains unresolved. Therefore, the application's compliance verdict is limited to the mandate requirements that can currently be checked.

3. Portfolio Construction and Baseline Comparison

The application evaluates four asset classes:

Treasury bills

10-year Treasury notes

Investment-grade bond fund

Global equity index fund

I compared an equal-weight portfolio, an inverse-volatility portfolio, a benchmark portfolio, and a constrained optimized portfolio.

The equal-weight approach allocates 25% to each asset. The inverse-volatility approach places greater weight on lower-volatility investments, while the constrained optimizer searches for an allocation that meets the implemented investment requirements.

The inverse-volatility portfolio produced an expected annual return of approximately 3.77% and annual volatility of 1.05%. Its reserve coverage was approximately 90.3%, but its expected return did not satisfy the 6.5% objective.

The benchmark portfolio, consisting of 40% investment-grade bonds and 60% global equities, produced an expected return of approximately 6.80% and volatility of 10.46%.

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

Expected annual return: 6.51%
Estimated annual volatility: 9.44%
Reserve-eligible coverage: 20%
Mandate verdict: PASS CHECKABLE RULES

The constrained portfolio achieved the return objective with lower estimated volatility than the benchmark. However, the small margin above the return objective made the portfolio sensitive to changes in assumptions.

4. Point-in-Time Signal Validation

I incorporated the DGS10 daily 10-year Treasury yield series into the application as an interest rate signal.

The point-in-time process is designed to use information available as of the selected investment decision date rather than relying on later observations.

This helps reduce look-ahead bias, which occurs when future information is incorrectly used to evaluate an earlier investment decision.

I implemented and tested the point-in-time signal functionality as part of the completed application validation.

The DGS10 signal provides additional context for investment decisions, but it does not guarantee future interest rate movements or portfolio performance.

The historical proxy analysis remains subject to the limitations of the available data and should not be interpreted as a fully verified historical trading record.

5. Completed Stress Testing

I independently tested the constrained portfolio under alternative expected-return assumptions, transaction costs, and reserve requirements.

The stress scenarios included:

Expected-return reductions of 0.25 and 0.50 percentage points.

Transaction cost assumptions of 10 and 25 basis points.

An increase in the minimum reserve requirement to 25%.

The original portfolio's expected annual return was 6.51%, leaving only a 0.01 percentage-point cushion above the objective.

Reducing all asset expected returns by 0.25 percentage points while keeping the original allocation fixed lowered the portfolio's expected return to 6.26%. This failed the 6.5% objective.

The portfolio also failed the higher 25% reserve requirement because its original reserve coverage was only 20%.

The transaction cost scenarios further demonstrated the importance of considering implementation costs when evaluating a portfolio with a narrow expected-return margin.

These completed tests showed that the original portfolio's mandate compliance was sensitive to changes in assumptions.

6. Changed-Input Test Results

I also evaluated the optimizer's response to a 0.25 percentage-point reduction in the expected returns of all four assets.

Unlike the fixed-allocation stress test, the changed-input test allowed the application to re-optimize the portfolio.

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

The optimizer increased the allocation to global equities from 55% to 60% and reduced the allocation to 10-year Treasury notes from 20% to 5%.

The re-optimized portfolio achieved an expected return of 6.52%, allowing it to continue meeting the return objective.

However, annual volatility increased from 9.44% to 10.36%, and reserve coverage declined from 20% to 5%.

These results demonstrated that the optimizer could compensate for lower expected-return assumptions by changing portfolio allocations, but the revised allocation introduced additional estimated risk and reduced the reserve cushion.

The changed-input test reinforced my decision not to recommend immediate implementation.

7. Historical Estimation-Window Validation

I completed a historical estimation-window sensitivity analysis using monthly proxy data for SGOV, IEF, LQD, and VT.

The dataset contained 63 monthly price observations and 62 monthly return observations, covering January 2021 through March 2026.

I compared the original Lab 14 assumptions, the full historical sample, and the most recent 36 months.

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

The original fixed allocation produced an estimated return of 5.71% using the full historical sample, which failed the foundation's annual return objective.

However, the same allocation produced an estimated return of 10.59% using the most recent 36 months.

The re-optimized portfolios also produced substantially different results across estimation windows.

This completed analysis demonstrated that the portfolio's estimated return, volatility, and optimal allocation depend significantly on the historical period used.

The findings were an important factor in my final investment recommendation.

8. Independent Validation Findings

I completed the following validation activities for Project 2:

Baseline comparison: Compared the equal-weight, inverse-volatility, benchmark, and constrained portfolio approaches.

Mandate testing: Evaluated expected returns, reserve coverage, liquidity, issuer concentration, and portfolio weight constraints.

Stress testing: Tested reduced expected returns, transaction costs, and an increased reserve requirement.

Changed-input testing: Compared the original constrained allocation with the re-optimized allocation after changing expected-return assumptions.

Historical sensitivity analysis: Compared portfolio performance under different historical estimation windows.

Point-in-time signal testing: Implemented and tested the DGS10 interest rate signal and its decision-date controls.

Application output checks: Ran the Streamlit application and reviewed the resulting allocations, risk estimates, and compliance verdicts.

These validation activities helped identify the strengths and limitations of the portfolio construction process.

The application successfully demonstrated how portfolio optimization and risk controls can support investment decisions.

However, the results also showed that the portfolio's expected performance was sensitive to modeling assumptions.

The remaining uncertainty is a limitation of the investment strategy and its assumptions, not a statement that independent validation was left incomplete.

9. Investment Decision and Rationale

Final Recommendation: Defer Implementation.

Based on my completed independent validation, I do not recommend immediately allocating capital to the constrained portfolio.

Although the original portfolio achieved the 6.5% expected-return objective and passed the currently checkable mandate rules, the validation results revealed several concerns.

First, the original expected return was only 6.51%, providing almost no cushion above the objective.

Second, the fixed-allocation stress test showed that a 0.25 percentage-point reduction in expected returns caused the portfolio to fail the return objective.

Third, the changed-input test showed that maintaining the return objective through re-optimization required higher estimated volatility and reduced reserve coverage.

Fourth, the historical estimation-window analysis demonstrated that expected portfolio performance changed substantially depending on the sample period.

Finally, the CIO's calendar-year loss rule remains undefined, preventing a complete determination of mandate compliance.

Together, these findings support a cautious investment decision.

Provisional new-capital allocation: 0%.

The investment committee should monitor expected returns, estimated volatility, reserve coverage, five-business-day liquidity, and issuer concentration.

Implementation should be reconsidered if the strategy demonstrates acceptable robustness under updated assumptions and the CIO clarifies the calendar-year loss rule.

10. Final Conclusion

Project 2 demonstrated how an investment management application can combine portfolio optimization, mandate compliance checks, point-in-time information, stress testing, and historical sensitivity analysis to support an investment committee decision.

My constrained portfolio initially achieved the foundation's return objective with lower estimated volatility than the benchmark.

However, my independent validation showed that the portfolio's results were sensitive to changes in expected returns, optimization assumptions, and historical estimation windows.

The changed-input test also demonstrated that preserving the return objective could require accepting additional volatility and reduced reserve coverage.

My final decision is to defer implementation based on the evidence produced by my completed validation.

This recommendation reflects the importance of evaluating portfolio robustness rather than relying only on an optimizer's initial result.

AI and Educational Disclosure: This project is an educational investment management simulation and does not constitute investment advice. AI tools assisted with application development, debugging, and documentation. I independently tested the application's behavior, reviewed portfolio calculations and mandate results, and evaluated the findings used to support my investment recommendation.