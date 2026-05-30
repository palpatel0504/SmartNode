import joblib

model = joblib.load("model/call_classifier.pkl")


def classify_text(text):
    """
    Returns:
    label -> Closed/Open/Urgent
    confidence -> prediction confidence %
    """

    prediction = model.predict([text])[0]

    probabilities = model.predict_proba([text])[0]

    confidence = float(max(probabilities) * 100)

    return prediction, confidence