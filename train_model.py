import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.model_selection import train_test_split

from sklearn.naive_bayes import MultinomialNB

from sklearn.metrics import accuracy_score

import joblib


# DATASET
data = {

    'email': [

        'Your bank account is suspended click here',

        'Win money now claim reward',

        'Verify your password immediately',

        'Meeting scheduled tomorrow',

        'Project submission deadline extended',

        'Lunch at 2 PM today',

        'Congratulations you won lottery',

        'Reset your account password now'
    ],

    'label': [

        'phishing',

        'phishing',

        'phishing',

        'safe',

        'safe',

        'safe',

        'phishing',

        'phishing'
    ]
}


df = pd.DataFrame(data)


# FEATURES
X = df['email']

y = df['label']


# VECTORIZATION
vectorizer = TfidfVectorizer()

X_vectorized = vectorizer.fit_transform(X)


# TRAIN TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(

    X_vectorized,
    y,
    test_size=0.2,
    random_state=42
)


# MODEL
model = MultinomialNB()

model.fit(X_train, y_train)


# ACCURACY
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy * 100:.2f}%")


# CREATE FOLDER
import os

os.makedirs('ml_model', exist_ok=True)


# SAVE MODEL
joblib.dump(model, 'ml_model/model.pkl')

joblib.dump(vectorizer, 'ml_model/vectorizer.pkl')


print("Model and vectorizer saved successfully!")