import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# =========================
# LOAD DATA
# =========================

file_path = r"C:\Users\Osinuga Damilola\Downloads\SLU Opportunity Wise Data new.xlsx"
df = pd.read_excel(file_path, sheet_name="Clean Sheet")

print(df.columns)

# =========================
# CREATE CHURN LABEL
# =========================

df["Churn_Participation"] = np.where(
    df["Status Description"].isin(["Dropped Out", "Withdraw", "Withdrawn"]) |
    ((df["Accepted Flag"] == 1) & (df["Participation Flag"] == 0)),
    1,
    0
)

print("\nChurn Distribution:")
print(df["Churn_Participation"].value_counts())

# =========================
# SELECT FEATURES (NO LEAKAGE)
# =========================

features = [
    "Application Month",
    "Application Quarter",
    "Application Year",
    "Opportunity Category"
]

df_model = df[features + ["Churn_Participation"]].dropna()

# One-hot encode
df_model = pd.get_dummies(df_model, drop_first=True)

X = df_model.drop("Churn_Participation", axis=1)
y = df_model["Churn_Participation"]

# =========================
# TRAIN TEST SPLIT
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================
# TRAIN MODEL
# =========================

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# =========================
# EVALUATION
# =========================

print("\nMODEL PERFORMANCE (Participation Churn) - NO LEAKAGE")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# =========================
# FEATURE IMPORTANCE
# =========================

coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_[0]
}).sort_values("Coefficient", ascending=False)

print("\nTop Features Increasing Churn:")
print(coefficients.head(10))

print("\nTop Features Reducing Churn:")
print(coefficients.tail(10))