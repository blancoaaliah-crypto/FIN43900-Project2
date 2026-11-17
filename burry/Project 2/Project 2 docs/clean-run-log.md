Project 2 — Clean-Environment Reproduction Log

Course: FIN 43900 — AI-Augmented Finance
Project: Meridian Foundation Reserve
Test Date: November 17, 2026
Repository: https://github.com/blancoaaliah-crypto/FIN43900-Project2
Operating System: macOS
Python Version: 3.14
Test Environment: Fresh GitHub clone and newly created Python virtual environment
Overall Result: PASS — Application and validation scripts successfully reproduced

1. Purpose

The purpose of this test was to determine whether another user could reproduce the Project 2 application from the GitHub repository without relying on my original development environment.

This test specifically evaluated:

Repository accessibility

Dependency installation

Mathematical validation

Portfolio stress testing

Historical estimation-window calculations

Streamlit application startup and functionality

The test was performed in a separate directory using a newly created Python virtual environment.

2. Fresh Repository Clone

I opened a terminal and executed:

cd ~
git clone https://github.com/blancoaaliah-crypto/FIN43900-Project2.git FIN43900-Project2-CleanTest
cd "FIN43900-Project2-CleanTest/burry/Project 2"

Observed result: PASS

The repository cloned successfully. Git reported that all 687 objects were received and all deltas were resolved.

3. Independent Python Environment

I created a new virtual environment inside the fresh repository clone:

python3 -m venv .venv-clean
source .venv-clean/bin/activate

I then installed the required dependencies:

python -m pip install -r requirements.txt

The installation included:

numpy

pandas

requests

streamlit

yfinance

Observed result: PASS

The terminal reported successful installation of the required packages and their dependencies.

No dependency installation errors were reported.

4. Mathematical Validation

I executed:

python project2_validation.py

The validation script produced:

PROJECT 2 — VALIDATION
=======================================================

Return calculation: PASS
Volatility calculation: PASS
Weights sum to 100%: PASS
Covariance symmetric: PASS
Covariance PSD: PASS

Result: 5 of 5 automated checks passed.

These checks confirm that the tested expected-return calculation, portfolio-volatility calculation, portfolio weights, and covariance-matrix properties satisfied the implemented validation tests.

They do not independently establish that all market assumptions or mandate interpretations are correct.

5. Stress-Test Reproduction

The validation script also produced the following stress-test results:

Scenario

Net Return

Volatility

Reserve

Verdict

Baseline

6.51%

9.44%

20%

PASS CHECKABLE RULES

Returns −0.25 pp

6.26%

9.44%

20%

FAIL

Returns −0.50 pp

6.01%

9.44%

20%

FAIL

Volatility +25%

6.51%

11.80%

20%

PASS CHECKABLE RULES

Transaction cost 10 bps

6.41%

9.44%

20%

FAIL

Transaction cost 25 bps

6.26%

9.44%

20%

FAIL

Reserve minimum 25%

6.51%

9.44%

20%

FAIL

Observed process stop condition:

Stop: True
Reason: At least one stress scenario fails a checkable rule.

Five of seven scenarios failed at least one currently checkable mandate requirement.

These results support the decision to defer implementation rather than rely solely on the original optimized portfolio.

6. Historical Estimation-Window Reproduction

I executed:

python compare_windows.py

The script completed successfully and returned:

Asset

Full-History Return

Last-36-Month Return

Full-History Volatility

Last-36-Month Volatility

Treasury bills

3.25%

4.69%

0.61%

0.20%

10-year Treasury notes

−1.30%

2.45%

7.62%

6.73%

Investment-grade bond fund

−0.07%

4.47%

9.63%

7.86%

Global equity index fund

10.89%

16.33%

14.31%

11.62%

Observed result: PASS

The script reproduced the historical asset-level return and volatility estimates.

The substantial differences between estimation windows demonstrate sensitivity to the historical sample used.

7. Streamlit Application Test

I launched the application from the clean environment using:

python -m streamlit run project2_app.py

Observed result: PASS

The Streamlit application launched successfully, and I confirmed that it worked in the newly created environment.

This demonstrated that the application could start without relying on the original development environment.

8. Reproduction Limitations

Although the clean-environment test succeeded, the following limitations remain:

The test was performed on macOS using Python 3.14. Other operating systems and Python versions were not independently tested.

Successful execution does not independently validate every financial assumption or data source.

External market-data services and historical-data revisions may affect future results.

The ETF historical proxy dataset has not been established as a fully point-in-time backtest.

The CIO's calendar-year loss rule remains unresolved, preventing full mandate certification.

This test was performed by the project developer in a separate environment, not independently by an external reviewer.

9. Final Reproduction Conclusion

Overall Result: PASS

The clean-environment test demonstrated that the GitHub repository could be cloned, dependencies could be installed, mathematical validation and historical comparison scripts could be executed, and the Streamlit application could be launched successfully.

All five mathematical validation checks passed, and the stress-testing results reproduced the process stop condition.

This provides evidence of technical reproducibility and improves confidence that another user can run the submitted application.

However, successful reproduction does not eliminate the financial and data limitations identified in the investment committee memo.

Final Investment Recommendation: DEFER IMPLEMENTATION.