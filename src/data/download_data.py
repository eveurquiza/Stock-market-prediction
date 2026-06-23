import yfinance as yf

ticker = "AAPL"

df = yf.download(
    ticker,
    start="2015-01-01",
    end="2025-01-01",
    auto_adjust=True
)

df.reset_index(inplace=True)

df.to_csv(
    "data/raw/aapl.csv",
    index=False
)