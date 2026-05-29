import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# load data
df = pd.read_csv("dataset.csv")

X = df[["glucose", "haemoglobin", "cholesterol"]]
y = df["risk"]

# split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# save model
joblib.dump(model, "health_model.pkl")

print("Model trained and saved!")