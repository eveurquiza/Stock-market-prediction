import yfinance as yf

ticker = "AAPL"

df = yf.download(
    ticker,
    start="2015-01-01",
    end="2025-01-01"
)

df.to_csv("data/raw/aapl.csv")

print(df.head())