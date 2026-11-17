Project 2 — Investment Management Application

Course: FIN 43900 — AI-Augmented Finance
Project: Meridian Foundation Reserve
Portfolio Value: $100 million
Final Investment Recommendation: Defer Implementation
Provisional New-Capital Allocation: 0%

1. Project Overview

For Project 2, I developed a Python and Streamlit investment management application for the fictional Meridian Foundation Reserve.

The foundation manages a $100 million portfolio with a 6.5% annual return objective and additional requirements for reserve coverage, liquidity, issuer concentration, and portfolio allocation.

The application compares portfolio construction strategies, evaluates mandate compliance, incorporates a point-in-time interest rate signal, and tests portfolio performance under alternative assumptions.

I completed independent validation through baseline comparisons, stress testing, changed-input testing, historical estimation-window sensitivity analysis, point-in-time signal testing, and application output reviews.

My final recommendation is to defer implementation based on the results of the completed validation.

2. Educational and AI Disclosure

This project is an educational investment management simulation and does not constitute investment advice.

AI tools assisted with planning, Python and Streamlit development, debugging, explanations, and documentation.

I independently ran and reviewed the application, evaluated portfolio calculations and mandate results, and completed an AI-off prediction before running the changed-input test.

I compared the prediction with the application's observed results and used the completed validation findings to support my investment recommendation.

AI-generated outputs were not assumed to be correct without review.

3. Investment Mandate

The Meridian Foundation Reserve has the following investment requirements:

Requirement

Mandate

Portfolio value

$100 million

Annual return objective

At least 6.5%

Minimum reserve-eligible assets

3%

Five-business-day liquidity

At least 90%

Maximum issuer concentration

8%

Portfolio allocation

Long-only; weights total 100%

Treasury securities and diversified funds are treated as exempt from the individual issuer concentration restriction under the application's assumptions.

The CIO's calendar-year loss rule remains unresolved. The application therefore reports compliance only with the currently checkable mandate requirements.

4. Investment Universe

The application evaluates four asset classes:

Asset

Role

Treasury bills

Short-term reserves and liquidity

10-year Treasury notes

Government fixed-income exposure

Investment-grade bond fund

Diversified fixed-income exposure

Global equity index fund

Long-term growth exposure

The application compares four portfolio approaches:

Equal-weight allocation.

Inverse-volatility allocation.

Benchmark allocation.

Constrained portfolio optimization.

The benchmark uses 40% investment-grade bonds and 60% global equities.

5. Application Features

Portfolio Construction

The application calculates portfolio expected returns, estimated volatility, and investment allocations.

It compares equal-weight, inverse-volatility, benchmark, and constrained portfolios.

The constrained optimizer searches for allocations that satisfy the implemented mandate requirements.

Mandate Compliance

The application evaluates:

Expected annual return.

Reserve-eligible asset coverage.

Five-business-day liquidity.

Issuer concentration.

Long-only investment weights.

Total portfolio allocation.

The application reports PASS CHECKABLE RULES when the implemented requirements are satisfied.

Point-in-Time Interest Rate Signal

The application incorporates the DGS10 daily 10-year Treasury yield series.

The signal uses decision-date controls intended to prevent later observations from entering earlier investment decisions.

This supports point-in-time analysis and reduces the risk of look-ahead bias.

Stress Testing

The application evaluates the effect of:

Lower expected returns.

Transaction costs.

Higher reserve requirements.

These tests help identify whether the original portfolio remains compliant when assumptions change.

Historical Estimation-Window Sensitivity

The application uses monthly historical proxy data for:

SGOV

IEF

LQD

VT

It compares portfolio estimates under the original Lab 14 assumptions, the full historical sample, and the most recent 36 months.

Changed-Input Testing

The application allows expected-return assumptions to change and re-optimizes the constrained portfolio.

I completed an AI-off prediction before running the changed-input test and compared my prediction against the actual results.

6. Selected Portfolio Results

The original constrained optimizer selected the following allocation:

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
Reserve coverage: 20%
Mandate verdict: PASS CHECKABLE RULES

The constrained portfolio met the 6.5% return objective with lower estimated volatility than the benchmark.

However, its expected return exceeded the objective by only 0.01 percentage points.

7. Completed Validation Results

Baseline Comparison

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

The inverse-volatility portfolio produced low estimated volatility but did not meet the return objective.

The constrained portfolio met the objective with lower estimated volatility than the benchmark.

Stress-Test Results

I tested the original fixed allocation under expected-return reductions, transaction costs, and an increased reserve requirement.

Scenario

Result

Original assumptions

6.51% expected return — PASS

Expected returns reduced by 0.25 percentage points

6.26% — FAIL

Expected returns reduced by 0.50 percentage points

6.01% — FAIL

Reserve minimum increased to 25%

Original 20% coverage — FAIL

The application also included transaction-cost scenarios of 10 and 25 basis points.

These tests demonstrated that the original allocation was sensitive to relatively small changes in assumptions.

Changed-Input Results

I reduced the expected returns of all four assets by 0.25 percentage points and allowed the constrained optimizer to calculate a new allocation.

Measure

Original

Changed Input

Expected return

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

The re-optimized portfolio continued meeting the 6.5% objective, but estimated volatility increased and reserve coverage declined.

My AI-off prediction correctly anticipated increased global equity exposure and higher estimated volatility.

Historical Estimation-Window Results

Estimation Window

Portfolio

Expected Return

Volatility

Lab 14 assumptions

Fixed allocation

6.51%

9.44%

Full history

Fixed allocation

5.71%

11.04%

Full history

Re-optimized

6.69%

6.49%

Last 36 months

Fixed allocation

10.59%

8.98%

Last 36 months

Re-optimized

7.02%

2.35%

The historical analysis demonstrated that portfolio estimates and optimized allocations can change substantially depending on the estimation window.

8. Project Files

The main project files are organized as follows:

burry/
└── Project 2/
    ├── README.md
    ├── project2_app.py
    ├── project2_portfolio.py
    ├── project2_validation.py
    ├── project2_signals.py
    ├── [historical price CSV]
    └── docs/
        ├── decision-memo.md
        ├── validation-and-ai-use.md
        ├── locked-changed-input-record.md
        └── [video transcripts and submission manifest]

The historical CSV and other supporting file names should match the files actually included in the submitted repository.

9. How to Run the Application

Step 1 — Open the Repository

Open the FIN43900-Fall2026 repository in VS Code.

Navigate to the Project 2 directory:

cd "burry/Project 2"

Step 2 — Activate the Python Environment

If using the repository's existing virtual environment on macOS:

source ../../.venv/bin/activate

This command assumes the virtual environment is located at the repository root.

Step 3 — Install Required Packages

The application uses Python, Streamlit, and portfolio analysis libraries.

Install the dependencies listed in the project's environment or requirements file, if available.

Step 4 — Start Streamlit

Run:

streamlit run project2_app.py

Streamlit will display a local URL where the application can be opened in a browser.

Step 5 — Use the Application

Within the application:

Review the investment mandate.

Compare the baseline portfolios.

Examine the constrained optimized allocation.

Review the mandate compliance verdict.

Evaluate the DGS10 point-in-time signal.

Run stress scenarios.

Compare historical estimation windows.

Change expected-return assumptions and review re-optimization.

Review the investment committee recommendation.

10. Independent Validation and AI Use

I completed independent application testing and reviewed the results across the portfolio construction, mandate compliance, point-in-time signal, stress-testing, changed-input, and historical estimation-window components.

I also completed an AI-off prediction before running the changed-input test.

The prediction anticipated that lowering expected returns would make the objective more difficult to achieve, increase global equity exposure, and increase portfolio volatility.

After running the test, I compared those expectations with the observed results and documented the discrepancy between fixed-allocation sensitivity and re-optimized performance.

AI tools assisted with coding, debugging, explanations, and documentation, but I reviewed the application outputs and made the final investment recommendation based on the completed validation.

Further details are recorded in:

docs/decision-memo.md

docs/validation-and-ai-use.md

The separate Project 2 Locked Changed-Input Record

Any required pre-test Git commit evidence must be supported by the actual repository history.

11. Investment Committee Decision

Final Recommendation: Defer Implementation.

The original constrained portfolio met the 6.5% annual return objective and passed the currently checkable mandate rules.

However, the completed validation identified important concerns.

The expected return cushion was narrow, fixed-allocation stress scenarios produced mandate failures, and historical estimates changed significantly across estimation windows.

The changed-input test also showed that maintaining the return objective through re-optimization required higher estimated volatility and lower reserve coverage.

The CIO's calendar-year loss rule remains undefined, preventing full mandate certification.

Provisional allocation of new capital: 0%.

The committee should reconsider implementation if the strategy demonstrates acceptable robustness under updated assumptions and the CIO clarifies the calendar-year loss rule.

12. Demonstration Videos

The project submission includes three demonstration videos.

Video 1 — Application Walkthrough

Demonstrates the application interface, investment mandate, portfolio construction, and constrained optimization.

YouTube link: [Add Video 1 URL]

Video 2 — Validation and Stress Testing

Demonstrates mandate checks, stress testing, historical estimation-window sensitivity, and point-in-time signal functionality.

YouTube link: [Add Video 2 URL]

Video 3 — Changed-Input Test and Investment Decision

Demonstrates the changed-input test, prediction comparison, observed portfolio changes, and final investment committee recommendation.

YouTube link: [Add Video 3 URL]

Transcripts are included with the project submission.

13. Final Project Conclusion

Project 2 demonstrates how Python and Streamlit can be used to build an investment management application that combines portfolio optimization, risk measurement, mandate checks, point-in-time signals, and scenario analysis.

My completed validation showed that the constrained portfolio could meet the foundation's annual return objective under the original assumptions.

However, the portfolio's performance was sensitive to changes in expected returns, optimization assumptions, and historical estimation windows.

My final investment decision is to defer implementation based on the completed validation findings.

This decision reflects the importance of evaluating investment robustness rather than relying only on an optimizer's initial result.

Educational Disclaimer: This application is intended for coursework and educational analysis only. It does not provide investment advice or recommend securities for real-world investment.