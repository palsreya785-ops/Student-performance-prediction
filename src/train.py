import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
import os

os.makedirs("models", exist_ok=True)

df = pd.read_csv("data/students.csv")

X = df.drop(["pass", "final_score"], axis=1)
y = df["pass"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("📊 Model Performance:\n")
print(classification_report(y_test, y_pred))

joblib.dump(model, "models/model.pkl")

print("✅ Model saved!")