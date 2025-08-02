import joblib
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, '..', 'data', 'spirit_animal_dataset.csv')

df = pd.read_csv(data_path)


# Separate features and target
X = df.drop("animal", axis=1)
y = df["animal"]

# One-hot encode features (fit on all features)
encoder = OneHotEncoder(sparse_output=False)
X_encoded = encoder.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.2, random_state=42
)

print(f"Training samples: {len(X_train)}")
print(f"Test samples: {len(X_test)}")


model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

print("Model training complete!")

# Predict on the test set
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Detailed report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# Save model
joblib.dump(model, "animal_model.pkl")
print("✅ Model saved as animal_model.pkl")

# Save encoder
joblib.dump(encoder, "animal_encoder.pkl")
print("✅ Encoder saved as animal_encoder.pkl")
