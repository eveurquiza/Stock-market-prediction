from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import pandas as pd
import joblib

df = pd.read_csv("data/processed/aapl.csv")

df["Return_1"] = df["Close"].pct_change()

# LAGS
df["Close_lag1"] = df["Close"].shift(1)
df["Close_lag2"] = df["Close"].shift(2)
df["Return_lag1"] = df["Return_1"].shift(1)

# ROLLING
df["Rolling_mean_5"] = df["Close"].rolling(5).mean()
df["Rolling_std_10"] = df["Close"].rolling(10).std()

# TARGET
df["Target"] = df["Return_1"].shift(-1)

df = df.dropna()

X = df.drop(["Date", "Close", "Target"], axis=1)
y = df["Target"]

# Split temporal
train_size = int(len(df) * 0.8)

X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

model = RandomForestRegressor(
    n_estimators=500,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("MAE:", mean_absolute_error(y_test, predictions))
print("R²:", r2_score(y_test, predictions))

joblib.dump(model, "models/random_forest.pkl")