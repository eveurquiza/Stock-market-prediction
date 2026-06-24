import yfinance as yf

options = {'01': 'AAPL', '02': '^GSPC', '03': 'GOOGL', '04': 'AMZN', '05': 'TSLA'}
print(f"Available options: {list(options.values())}")
ticker = input("Enter the ticker symbol you want to download (e.g., AAPL, GSPC, GOOGL, AMZN, TSLA): ").upper()

df = yf.download(
    ticker,
    start="2015-01-01",
    end="2025-01-01",
    auto_adjust=True
)

df.reset_index(inplace=True)

df.to_csv(
    f"data/raw/{ticker.lower()}.csv",
    index=False
)