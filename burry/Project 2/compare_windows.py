
from pathlib import Path
from project2_portfolio import estimate_from_csv

file = Path(__file__).parent / "monthly_prices.csv"

full = estimate_from_csv(file, last36=False)
recent = estimate_from_csv(file, last36=True)

full_returns, full_vols, full_corr, names = full
recent_returns, recent_vols, recent_corr, _ = recent

print("PROJECT 2 — ESTIMATION WINDOW COMPARISON")
print("=" * 60)

for i, name in enumerate(names):
    print(f"\n{name}")
    print(f"Full-history return: {full_returns[i]:.2%}")
    print(f"Last-36-month return: {recent_returns[i]:.2%}")
    print(f"Full-history volatility: {full_vols[i]:.2%}")
    print(f"Last-36-month volatility: {recent_vols[i]:.2%}")