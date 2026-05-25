from flask import Blueprint, render_template, request

from flask_login import login_required, current_user

from app.models.prediction_model import Prediction

from app import db

import joblib


# BLUEPRINT
prediction = Blueprint('prediction', __name__)


# LOAD MODEL
model = joblib.load('ml_model/model.pkl')

vectorizer = joblib.load('ml_model/vectorizer.pkl')


# HOME ROUTE
@prediction.route('/', methods=['GET', 'POST'])
@login_required
def home():

    prediction_result = None
    confidence = None

    try:

        if request.method == 'POST':

            email = request.form['email']

            # EMPTY INPUT CHECK
            if not email.strip():

                prediction_result = "Please enter email text"

            else:

                # VECTORIZE EMAIL
                vector = vectorizer.transform([email])

                # PREDICT
                result = model.predict(vector)

                # PREDICTION PROBABILITY
                probability = model.predict_proba(vector)

                confidence = round(
                    max(probability[0]) * 100,
                    2
                )

                prediction_result = result[0]

                # SAVE TO DATABASE
                new_prediction = Prediction(

                    email_text=email,

                    prediction_result=str(prediction_result),

                    user_id=current_user.id
                )

                db.session.add(new_prediction)

                db.session.commit()

        return render_template(

            'index.html',

            prediction=prediction_result,

            confidence=confidence,

            user=current_user
        )

    except Exception as e:

        return f"Error: {str(e)}"


# HISTORY ROUTE
@prediction.route('/history')
@login_required
def history():

    try:

        # GET USER HISTORY
        history_data = Prediction.query.filter_by(
            user_id=current_user.id
        ).order_by(
            Prediction.timestamp.desc()
        ).all()

        return render_template(
            'history.html',
            history=history_data
        )

    except Exception as e:

        return f"Error: {str(e)}"


# DASHBOARD ROUTE
@prediction.route('/dashboard')
@login_required
def dashboard():

    try:

        # TOTAL SCANS
        total_scans = Prediction.query.filter_by(
            user_id=current_user.id
        ).count()

        # PHISHING COUNT
        phishing_count = Prediction.query.filter(
            Prediction.user_id == current_user.id,
            Prediction.prediction_result == 'phishing'
        ).count()

        # SAFE EMAIL COUNT
        safe_count = total_scans - phishing_count

        # RECENT SCANS
        recent_scans = Prediction.query.filter_by(
            user_id=current_user.id
        ).order_by(
            Prediction.timestamp.desc()
        ).limit(5).all()

        return render_template(

            'dashboard.html',

            total_scans=total_scans,

            phishing_count=phishing_count,

            safe_count=safe_count,

            recent_scans=recent_scans
        )

    except Exception as e:

        return f"Error: {str(e)}"