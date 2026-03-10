# 🔐 AI Phishing Email Detector

An **AI-powered phishing email detection system** that analyzes email text and predicts whether an email is **Safe** or **Phishing** using **Machine Learning and Natural Language Processing (NLP)**.

This project includes a **Flask web interface** where users can paste an email message and instantly detect phishing attempts.

---

## 🚀 Features

* 🤖 AI-based phishing email classification
* 📊 Confidence score prediction
* ⚠️ Phishing risk score (0–100)
* 🔥 Threat level classification (Low / Medium / High)
* 🔎 Suspicious URL detection
* 🧠 Phishing keyword detection
* 🌐 Web interface using Flask

---

## 🛠️ Technologies Used

* Python
* Flask
* Scikit-learn
* TF-IDF Vectorization
* Logistic Regression
* HTML / CSS

---

## 📂 Project Structure

AI-Phishing-Email-Detector
│
├── dataset
│   └── Phishing_Email.csv
│
├── static
│   └── style.css
│
├── templates
│   └── index.html
│
├── app.py
├── train_model.py
├── requirements.txt
└── README.md

---

## ⚙️ Installation

Clone the repository:

git clone https://github.com/Nairayadav/AI-Phishing-Email-Detector.git

Move into the project folder:

cd AI-Phishing-Email-Detector

Install required libraries:

pip install -r requirements.txt

Train the machine learning model:

python train_model.py

Run the Flask application:

python app.py

Open the browser and go to:

http://127.0.0.1:5000

---

## 📧 Example Input

Dear user,

Your bank account has been suspended.
Click the link below to verify immediately.

http://secure-bank-login-update.com

---

## 📊 Example Output

Phishing Email Detected
Confidence: 92%
Risk Score: 91 / 100
Threat Level: HIGH

---

## 🎯 Project Goal

The goal of this project is to demonstrate how **Machine Learning and Cybersecurity techniques** can be used to identify phishing emails and improve email security.

---

## 👩‍💻 Author

**Naira Yadav**
B.Tech CSE (Cyber Security)
