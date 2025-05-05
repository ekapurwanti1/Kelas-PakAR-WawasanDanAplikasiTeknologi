import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Load dataset
data = pd.read_csv("dataset/diabetes.csv")

# Pisahkan fitur dan label
X = data.drop("Outcome", axis=1)
y = data["Outcome"]

# Bagi data latih dan uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inisialisasi dan latih model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluasi model
y_pred = model.predict(X_test)
print("=== Hasil Evaluasi Model ===")
print(classification_report(y_test, y_pred))