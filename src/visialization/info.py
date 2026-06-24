from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

base_dir = Path(__file__).resolve().parents[2]
df = pd.read_csv(base_dir / "data" / "raw" / "gspc.csv")

df["Date"] = pd.to_datetime(df["Date"])
df = df.set_index("Date")

print(df.head())

ax = df["Close"].plot(
    title="S&P 500 Closing Prices",
    ylabel="Price (USD)",
    xlabel="Date",
)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()