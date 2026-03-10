from flask import Flask, render_template, request
import pickle
import re

app = Flask(__name__)

# Load trained model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Suspicious phishing keywords
phishing_keywords = [
    "verify your account",
    "login immediately",
    "password reset",
    "bank account suspended",
    "urgent action required",
    "click here",
    "confirm your identity",
    "update your account",
    "security alert",
    "confirm your password"
]


# Detect phishing keywords
def detect_keywords(text):
    found_keywords = []
    for word in phishing_keywords:
        if word.lower() in text.lower():
            found_keywords.append(word)
    return found_keywords


# Detect URLs in email
def detect_urls(text):
    url_pattern = r'https?://\S+|www\.\S+'
    urls = re.findall(url_pattern, text)
    return urls


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    email = request.form.get("email")

    # Prevent empty input
    if not email:
        return render_template(
            "index.html",
            prediction="Please paste an email message first."
        )

    # Convert email to ML input
    email_vector = vectorizer.transform([email])

    # Machine learning prediction
    prediction = model.predict(email_vector)[0]

    # Probability score
    probability = model.predict_proba(email_vector)[0].max()

    # Confidence %
    confidence = round(probability * 100, 2)

    # Phishing risk score
    risk_score = round(probability * 100)

    # Threat level classification
    if risk_score >= 75:
        threat = "HIGH"
    elif risk_score >= 40:
        threat = "MEDIUM"
    else:
        threat = "LOW"

    # Detect URLs
    urls = detect_urls(email)

    # Detect suspicious keywords
    keywords = detect_keywords(email)

    # Result message
    if prediction == "Phishing Email":
        result = "⚠️ Phishing Email Detected"
    else:
        result = "✅ Safe Email"

    return render_template(
        "index.html",
        prediction=result,
        confidence=confidence,
        risk=risk_score,
        threat=threat,
        urls=urls,
        keywords=keywords
    )


if __name__ == "__main__":
    app.run(debug=True)