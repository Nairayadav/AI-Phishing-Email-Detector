from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

bcrypt = Bcrypt()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app():

    app = Flask(__name__)

    # SECRET KEY
    app.config['SECRET_KEY'] = 'secretkey'

    # DATABASE
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    # INITIALIZE EXTENSIONS
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # IMPORT MODELS
    from app.models.user_model import User
    from app.models.prediction_model import Prediction

    # LOAD USER
    @login_manager.user_loader
    def load_user(user_id):

        return User.query.get(int(user_id))

    # IMPORT ROUTES
    from app.routes.prediction_routes import prediction
    from app.routes.auth_routes import auth

    # REGISTER BLUEPRINTS
    app.register_blueprint(prediction)
    app.register_blueprint(auth)

    return app