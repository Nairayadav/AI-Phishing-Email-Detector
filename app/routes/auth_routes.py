from flask import Blueprint, request, jsonify, render_template, redirect
from app.models.user_model import User
from app import db, bcrypt
from flask_login import login_user

auth = Blueprint('auth', __name__)


# REGISTER ROUTE
@auth.route('/register', methods=['GET', 'POST'])
def register():

    try:

        # Show register page
        if request.method == 'GET':

            return render_template('register.html')

        # Get form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if email already exists
        existing_user = User.query.filter_by(email=email).first()

        if existing_user:

            return """
            <h2>Email already registered</h2>
            <a href="/register">Try Again</a>
            """

        # Hash password
        hashed_password = bcrypt.generate_password_hash(
            password
        ).decode('utf-8')

        # Create new user
        user = User(
            username=username,
            email=email,
            password=hashed_password
        )

        # Save user to database
        db.session.add(user)
        db.session.commit()

        return """
        <h2>User registered successfully</h2>
        <a href="/login">Login Now</a>
        """

    except Exception as e:

        return f"Error: {str(e)}"


# LOGIN ROUTE
@auth.route('/login', methods=['GET', 'POST'])
def login():

    try:

        # Show login page
        if request.method == 'GET':

            return render_template('login.html')

        # Get form data
        email = request.form['email']
        password = request.form['password']

        # Find user
        user = User.query.filter_by(email=email).first()

        # Check password
        if user and bcrypt.check_password_hash(
            user.password,
            password
        ):

            # Login user
            login_user(user)

            return """
            <h2>Login Successful</h2>
            <a href="/">Go To Home</a>
            """

        return """
        <h2>Invalid Email or Password</h2>
        <a href="/login">Try Again</a>
        """

    except Exception as e:

        return f"Error: {str(e)}"