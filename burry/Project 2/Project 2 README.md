Project 2 — Investment Management Application

Course: FIN 43900 — AI-Augmented Finance
Project: Meridian Foundation Reserve
Portfolio Value: $100 million
Final Investment Recommendation: DEFER IMPLEMENTATION
Provisional New-Capital Allocation: 0%

1. Project Overview

For Project 2, I developed a Python and Streamlit investment management application for the fictional Meridian Foundation Reserve. The application supports an investment committee decision by evaluating portfolio construction, expected returns, volatility, mandate compliance, point-in-time information, and portfolio sensitivity to changing assumptions.

The foundation manages a hypothetical $100 million portfolio with an annual expected-return objective of at least 6.5%. The investment strategy must also satisfy reserve, liquidity, issuer-concentration, and allocation requirements.

The application compares multiple portfolio strategies, performs constrained optimization, incorporates an interest-rate signal, and evaluates portfolio performance through stress testing and historical estimation-window comparisons.

Final decision: Defer implementation. Although the original constrained portfolio satisfies the currently checkable mandate requirements, the validation results demonstrate that the strategy is sensitive to relatively small changes in assumptions.

2. Investment Mandate

Requirement

Mandate

Portfolio value

$100 million

Annual expected return

At least 6.5%

Reserve-eligible assets

At least 3%

Five-business-day liquidity

At least 90%

Maximum issuer concentration

8%

Portfolio weights

Long-only; total 100%

CIO calendar-year loss rule

Not fully specified

Under the application's assumptions, Treasury securities and diversified investment funds are exempt from the individual issuer-concentration restriction.

The CIO's calendar-year loss rule remains unresolved. Consequently, the application distinguishes between satisfying the implemented requirements and receiving complete investment approval.

A result of PASS CHECKABLE RULES does not constitute full mandate certification.

3. Investment Universe

The portfolio contains four asset classes:

Asset

Investment Role

Baseline Expected Return

Treasury bills

Liquidity and short-term reserves

3.50%

10-year Treasury notes

Government fixed-income exposure

4.30%

Investment-grade bond fund

Diversified fixed-income exposure

5.00%

Global equity index fund

Long-term growth exposure

8.00%

The application compares four portfolio approaches:

Equal-weight portfolio — 25% in each asset.

Inverse-volatility portfolio — allocation based on relative asset volatility.

Benchmark portfolio — 40% investment-grade bonds and 60% global equities.

Constrained optimized portfolio — searches for a qualifying allocation under the implemented mandate.

The constrained optimization uses a discrete 5-percentage-point allocation grid. The selected portfolio is therefore the best qualifying result within the modeled search grid, not a proven continuous global optimum.

4. Application Features

Portfolio Construction

The application calculates portfolio expected returns, estimated annual volatility, portfolio weights, and comparisons between alternative investment strategies.

Mandate Compliance

The application evaluates expected return, reserve coverage, five-business-day liquidity, issuer concentration, long-only allocations, and portfolio weights totaling 100%.

Point-in-Time Interest Rate Signal

The application incorporates the DGS10 daily 10-year Treasury yield series.

Decision-date filtering is intended to prevent observations from after the selected decision date from influencing earlier investment decisions.

This reduces look-ahead bias in the interest-rate signal. The historical ETF proxy dataset has not been established as a fully point-in-time investment backtest.

Stress Testing

The application evaluates how the original fixed portfolio responds to reduced expected returns, increased volatility, transaction costs, and higher reserve requirements.

Historical Estimation-Window Analysis

Historical proxy data includes:

SGOV — short-term Treasury exposure

IEF — intermediate-term Treasury exposure

LQD — investment-grade corporate bonds

VT — global equities

The application compares results from the original Lab 14 assumptions, the full available historical sample, and the most recent 36 months.

Changed-Input Testing

The application allows expected-return assumptions to change and then re-optimizes the portfolio.

The changed-input test compares the original allocation with the allocation selected after the input changes.

5. Baseline Portfolio Results

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

The constrained optimizer selected:

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

Original portfolio results:

Expected annual return: 6.51%

Estimated annual volatility: 9.44%

Reserve-eligible allocation: 20%

Mandate verdict: PASS CHECKABLE RULES

The expected return exceeds the 6.5% objective by only 0.01 percentage points. This narrow margin is an important weakness of the proposed allocation.

6. Independent Validation

I ran project2_validation.py to check the calculations and portfolio model.

The script returned:

Validation Check

Result

Expected-return calculation

PASS

Portfolio-volatility calculation

PASS

Portfolio weights sum to 100%

PASS

Covariance matrix is symmetric

PASS

Covariance matrix is positive semidefinite

PASS

Automated validation result: 5 of 5 checks passed.

These checks support the mathematical consistency of the tested portfolio calculations. They do not independently certify every application feature, data source, or mandate interpretation.

7. Stress-Test Results

The original constrained allocation was held fixed while assumptions changed.

Scenario

Expected Net Return

Volatility

Mandate Verdict

Original baseline

6.51%

9.44%

PASS

Expected returns −0.25 percentage points

6.26%

9.44%

FAIL

Expected returns −0.50 percentage points

6.01%

9.44%

FAIL

Volatility +25%

6.51%

11.80%

PASS

Transaction cost 10 basis points

6.41%

9.44%

FAIL

Transaction cost 25 basis points

6.26%

9.44%

FAIL

Reserve minimum increased to 25%

6.51%

9.44%

FAIL

Stress-test summary:

Two scenarios passed the currently checkable rules.

Five scenarios failed at least one currently checkable rule.

The application's process stop condition was triggered.

The increased-volatility scenario passes because the implemented mandate does not contain a separate maximum-volatility threshold.

These results demonstrate that the original portfolio is sensitive to changes in expected returns, transaction costs, and reserve requirements.

8. Changed-Input Test

For the changed-input test, I reduced the expected returns of all four assets by 0.25 percentage points and allowed the constrained optimizer to select a new portfolio.

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

Before observing the changed-input results, I made an AI-off prediction that lowering expected returns would increase pressure to hold more global equities and raise portfolio volatility.

The observed results were consistent with those predictions.

The original fixed allocation would produce a 6.26% expected return after the 0.25-percentage-point reduction. The re-optimized portfolio instead produced a 6.52% expected return by changing its weights.

Although the new portfolio continued meeting the checkable return requirement, it had higher estimated volatility and lower reserve coverage.

The AI-off prediction and its comparison with the observed results are documented separately. The repository history does not independently establish that the prediction was committed before the test was run.

9. Historical Estimation-Window Sensitivity

The historical analysis compares how portfolio estimates change when different estimation periods are used.

Estimation Window

Portfolio

Expected Return

Annual Volatility

Lab 14 assumptions

Original fixed allocation

6.51%

9.44%

Full historical sample

Original fixed allocation

5.71%

11.04%

Full historical sample

Re-optimized allocation

6.69%

6.49%

Last 36 months

Original fixed allocation

10.59%

8.98%

Last 36 months

Re-optimized allocation

7.02%

2.35%

The full historical sample causes the original allocation to fall below the 6.5% expected-return objective.

The most recent 36-month window produces substantially different estimates.

These differences demonstrate estimation-window sensitivity. Historical estimates are not guaranteed forecasts, and the proxy data should not be interpreted as a fully point-in-time backtest.

10. Investment Committee Decision

Final Recommendation: DEFER IMPLEMENTATION

Provisional New-Capital Allocation: 0%

I recommend deferring implementation for five reasons:

The original portfolio exceeds the return objective by only 0.01 percentage points.

Five of seven stress scenarios fail at least one currently checkable requirement.

The changed-input re-optimization increases estimated volatility while reducing reserve coverage.

Historical return and volatility estimates vary substantially across estimation windows.

The CIO's calendar-year loss rule remains unresolved, preventing complete mandate certification.

The portfolio should be reconsidered after the CIO clarifies the outstanding rule, the model is tested with updated assumptions, and the strategy demonstrates acceptable robustness across additional scenarios.

The recommendation is based on the completed validation rather than the original optimizer result alone.

11. Project File Structure

The Project 2 directory contains:

burry/
└── Project 2/
    ├── Project 2 README.md
    ├── requirements.txt
    ├── project2_app.py
    ├── project2_portfolio.py
    ├── project2_validation.py
    ├── project2_signals.py
    ├── compare_windows.py
    ├── create_price_data.py
    ├── monthly_prices.csv
    └── Project 2 docs/
        ├── decision-memo.md
        ├── Project 2 validation-and-ai-use.md
        └── Project 2 Locked Changed Input.md

The requirements.txt file is intended to be committed with the completed repository. Demonstration video links and transcripts will be added when available.

12. Installation and Reproduction Instructions

Step 1 — Clone the Repository

git clone https://github.com/blancoaaliah-crypto/FIN43900-Project2.git
cd FIN43900-Project2
cd "burry/Project 2"

Step 2 — Create a Python Virtual Environment

Python 3 is required. The project was run locally using Python 3.14; compatibility with other Python versions has not been independently verified.

python3 -m venv .venv
source .venv/bin/activate

On Windows, activate the environment using:

.venv\Scripts\activate

Step 3 — Install Dependencies

python -m pip install -r requirements.txt

The required third-party packages are:

numpy
pandas
requests
streamlit
yfinance

Internet access may be required for installation and for application features that retrieve external market or interest-rate data.

Step 4 — Run the Validation Script

python project2_validation.py

The previously observed result was five passing checks:

Return calculation: PASS
Volatility calculation: PASS
Weights sum to 100%: PASS
Covariance symmetric: PASS
Covariance PSD: PASS

The script also prints stress-test results and the process stop condition.

Step 5 — Run the Historical Comparison

python compare_windows.py

The script prints historical expected-return and volatility estimates for the full available sample and the most recent 36 months.

Step 6 — Launch the Streamlit Application

python -m streamlit run project2_app.py

Streamlit displays a local browser address.

Once the application opens, review the portfolio construction, mandate compliance, point-in-time signal, stress tests, historical comparisons, changed-input results, and investment committee decision.

Step 7 — Reproduce the Changed-Input Test

Begin with the original baseline expected returns:

Asset

Original Return

Changed Return

Treasury bills

3.50%

3.25%

10-year Treasury notes

4.30%

4.05%

Investment-grade bonds

5.00%

4.75%

Global equities

8.00%

7.75%

Run the constrained optimization with the original inputs, then reduce each expected return by 0.25 percentage points and re-optimize.

Compare the resulting portfolio weights, expected return, volatility, and reserve coverage with Section 8.

Reproducibility Limitations

The project scripts and application were run successfully in an existing local Python virtual environment.

A separate clean-environment installation and full end-to-end reproduction have not yet been independently verified.

External data availability, library versions, and historical-data revisions may affect results.

13. AI Use and Independent Review

AI tools assisted with project planning, Python and Streamlit development, debugging, explanations, and documentation.

I ran the application and validation scripts, reviewed the reported outputs, made an AI-off changed-input prediction, and evaluated the observed results against that prediction.

The investment committee recommendation was based on the validation findings and documented model limitations.

AI assistance does not replace independent verification. The repository includes validation documentation and a separate changed-input record.

14. Demonstration Videos

Three demonstration videos are planned for the Project 2 submission.

Video 1 — Application Walkthrough

Covers the investment mandate, portfolio strategies, constrained optimization, and application interface.

YouTube URL: [Add Video 1 URL]

Video 2 — Validation and Stress Testing

Covers independent calculation checks, mandate compliance, stress testing, historical estimation-window sensitivity, and the point-in-time signal.

YouTube URL: [Add Video 2 URL]

Video 3 — Changed-Input Test and Investment Decision

Covers the AI-off prediction, changed-input test, observed portfolio changes, and final investment committee recommendation.

YouTube URL: [Add Video 3 URL]

Transcripts and video links will be added when the recordings are completed.

15. Conclusion

Project 2 demonstrates how Python and Streamlit can support investment management decisions through portfolio construction, quantitative validation, mandate checks, and scenario analysis.

The original constrained portfolio met the foundation's expected-return objective under the initial assumptions. However, the completed validation showed that the result was sensitive to small changes in expected returns, transaction costs, reserve requirements, and historical estimation windows.

Final decision: Defer implementation and provisionally allocate 0% of new capital.

This project illustrates why an investment decision should consider model reliability, robustness, and unresolved constraints rather than relying solely on an optimized portfolio.

Educational disclaimer: This application was developed for FIN 43900 coursework. It is an educational simulation and does not constitute financial or investment advice.