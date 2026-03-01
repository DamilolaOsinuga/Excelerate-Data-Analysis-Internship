import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# =========================
# LOAD DATA
# =========================

file_path = r"C:\Users\Osinuga Damilola\Downloads\SLU Opportunity Wise Data new.xlsx"
df = pd.read_excel(file_path, sheet_name="Clean Sheet")

# =========================
# CREATE MONTHLY AGGREGATION
# =========================

df['Apply Date'] = pd.to_datetime(df['Apply Date'], errors='coerce')
df = df.dropna(subset=['Apply Date'])

monthly = df.groupby([
    df['Apply Date'].dt.year.rename("Year"),
    df['Apply Date'].dt.month.rename("Month")
]).size().reset_index(name="Application_Count")

monthly = monthly.sort_values(["Year", "Month"]).reset_index(drop=True)
monthly["Date"] = pd.to_datetime(monthly[["Year", "Month"]].assign(DAY=1))
monthly["Month_Index"] = np.arange(1, len(monthly) + 1)

# =========================
# CREATE SEASONAL DUMMIES
# =========================

month_dummies = pd.get_dummies(monthly["Month"], prefix="Month", drop_first=True)
monthly = pd.concat([monthly, month_dummies], axis=1)

# =========================
# MODEL A – TREND ONLY
# =========================

X_trend = monthly[["Month_Index"]]
y = monthly["Application_Count"]

model_A = LinearRegression()
model_A.fit(X_trend, y)

pred_A = model_A.predict(X_trend)

print("\nMODEL A: Linear Regression (Trend Only)")
print("MAE:", mean_absolute_error(y, pred_A))
print("RMSE:", np.sqrt(mean_squared_error(y, pred_A)))
print("R2:", r2_score(y, pred_A))

# =========================
# MODEL B – TREND + SEASONALITY
# =========================

X_season = monthly[["Month_Index"] + list(month_dummies.columns)]

model_B = LinearRegression()
model_B.fit(X_season, y)

pred_B = model_B.predict(X_season)

print("\nMODEL B: Linear Regression (Trend + Seasonality)")
print("MAE:", mean_absolute_error(y, pred_B))
print("RMSE:", np.sqrt(mean_squared_error(y, pred_B)))
print("R2:", r2_score(y, pred_B))

# =========================
# MODEL C – RANDOM FOREST
# =========================

model_C = RandomForestRegressor(n_estimators=100, random_state=42)
model_C.fit(X_season, y)

pred_C = model_C.predict(X_season)

print("\nMODEL C: Random Forest")
print("MAE:", mean_absolute_error(y, pred_C))
print("RMSE:", np.sqrt(mean_squared_error(y, pred_C)))
print("R2:", r2_score(y, pred_C))

# =========================
# FEATURE IMPORTANCE
# =========================

importances = pd.DataFrame({
    "Feature": X_season.columns,
    "Importance": model_C.feature_importances_
}).sort_values("Importance", ascending=False)

print("\nTop Features:")
print(importances.head(10))

# =========================
# VISUALIZATION
# =========================

plt.figure(figsize=(10,5))
plt.plot(monthly["Date"], y, label="Actual")
plt.plot(monthly["Date"], pred_B, label="Model B Prediction")
plt.legend()
plt.title("Actual vs Predicted (Model B)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()