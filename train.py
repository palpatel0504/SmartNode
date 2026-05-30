import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

df = pd.read_csv("data/labeled_dataset.csv")
X = df["text"]
y = df["label"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression(max_iter=1000))
])


model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("\nModel Evaluation:\n")
print(classification_report(y_test, predictions))

joblib.dump(
    model,
    "model/call_classifier.pkl"
)

print("\nModel saved successfully!")