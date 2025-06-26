import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
import shap
import joblib
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("data/cleaned_data.csv")
X = df.drop(columns=['high_vulnerability'])
y = df['high_vulnerability']

print("Target distribution:\n", y.value_counts())

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.2, random_state=42
)

# Train model
model = XGBClassifier(eval_metric='logloss')
model.fit(X_train, y_train)

# Evaluation
print(classification_report(y_test, model.predict(X_test)))

# Save model
joblib.dump(model, 'model.pkl')

# SHAP explanation
explainer = shap.Explainer(model)
shap_values = explainer(X_test)
shap.summary_plot(shap_values, X_test, show=False)
plt.savefig("shap_summary.png")
