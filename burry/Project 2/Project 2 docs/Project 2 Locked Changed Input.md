Project 2 — Locked Changed-Input Record

Test Setup

Project: Meridian Foundation Reserve

Changed input: Expected returns

Original adjustment: 0.00 percentage points

New adjustment: −0.25 percentage points

All other scenario settings remained unchanged.

Prediction — Before Test

I expected the reduction in expected returns to make it harder for the constrained portfolio to meet the 6.5% annual return objective.

I expected the optimizer to increase the allocation to global equities because they have the highest expected return among the four investments.

I also expected the portfolio to become riskier as the optimizer adjusted the allocation to compensate for the lower return assumptions.

The original portfolio earned only 6.51%, so there was very little room for a reduction in expected returns.

Prediction Lock

Prediction status: AI-off prediction and pre-test commit have been verified.

Actual Results

Original expected return: 6.51%

Changed-input expected return: 6.52%

Original annual volatility: 9.44%

Changed-input annual volatility: 10.36%

Original Portfolio Allocation

Treasury bills: 0%

Treasury 10-year note: 20%

Investment-grade bond fund: 25%

Global equity index fund: 55%

Changed-Input Portfolio Allocation

Treasury bills: 0%

Treasury 10-year note: 5%

Investment-grade bond fund: 35%

Global equity index fund: 60%

Original mandate verdict: PASS CHECKABLE RULES

Changed-input mandate verdict: PASS CHECKABLE RULES

Prediction Versus Actual

Did the result match my prediction?

The results matched the expected direction of the allocation change. The optimizer increased the global equity allocation from 55% to 60%, while annual volatility increased from 9.44% to 10.36%.

The changed portfolio still achieved the 6.5% annual return objective, which shows that re-optimization helped compensate for the lower expected returns.

What surprised me?

I was surprised that the portfolio could still meet the return objective after lowering the expected returns of every asset. However, the new portfolio required a higher allocation to global equities and had greater volatility.

I also noticed that reserve coverage declined from 20% to 5%, leaving less flexibility above the 3% minimum.

How did the investment decision change?

The results reinforced my recommendation to defer full adoption until additional validation is completed.

Although the revised portfolio passed the currently checkable mandate rules, it became more volatile and had a smaller reserve cushion.

Discrepancy Diagnosis

The original allocation would have produced an expected return of 6.26% after the reduction in return assumptions, which would fail the 6.5% objective.

However, the application re-optimized the portfolio instead of maintaining the original weights.

The optimizer reduced the Treasury 10-year note allocation from 20% to 5%, increased the investment-grade bond allocation from 25% to 35%, and increased global equities from 55% to 60%.

These adjustments increased the expected return to 6.52%, allowing the portfolio to satisfy the objective despite the lower asset-return assumptions.

The difference between the fixed-allocation prediction and the re-optimized result demonstrates why it is important to distinguish portfolio sensitivity from the optimizer's ability to find a different allocation.

Final Investment Decision

Recommendation: Defer full adoption and complete additional validation.

The changed-input test demonstrates that the portfolio can adjust to lower expected returns, but doing so increases estimated volatility and reduces reserve coverage.

The investment committee should review the robustness of the return assumptions, historical estimation windows, transaction costs, and unresolved calendar-year loss rule before authorizing implementation.

Provisional new-capital allocation: 0% until the validation concerns are addressed.

Monitoring triggers: Expected return below 6.5%, reserve coverage below 3%, five-day liquidity below 90%, issuer concentration above 8%, or material deterioration in estimated risk.

Reconsideration condition: Reconsider implementation after updated assumptions and stress tests support the strategy and the CIO clarifies the calendar-year loss rule.