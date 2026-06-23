from ta.trend import SMAIndicator
from ta.momentum import RSIIndicator

df['SMA_20'] = SMAIndicator(
    close=df['Close'],
    window=20
).sma_indicator()
df['SMA_50'] = SMAIndicator(
    close=df['Close'],
    window=50
).sma_indicator()

df['EMA_20'] = SMAIndicator(
    close=df['Close'],
    window=20,
    fillna=True
).sma_indicator()

df['RSI'] = RSIIndicator(
    close=df['Close']
).rsi()

df['MACD'] = df['Close'].ewm(span=12, adjust=False).mean() - df['Close'].ewm(span=26, adjust=False).mean()

df['Bollinger_Band'] = df['Close'].rolling(window=20).mean() + (df['Close'].rolling(window=20).std() * 2)

df['Target'] = df['Close'].shift(-1)

df = df.dropna()