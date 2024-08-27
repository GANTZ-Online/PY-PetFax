from flask import Flask
from flask_migrate import Migrate
from . import models

def create_app():
    app = Flask(__name__)

    # Configure the application
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Black*cat!@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize SQLAlchemy with the app
    models.db.init_app(app)

    # Set up Flask-Migrate for database migrations
    migrate = Migrate(app, models.db)

    # Register pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)

    # Register facts blueprint
    from . import facts
    app.register_blueprint(facts.bp)

    @app.route('/')
    def hello():
        return 'Hello, PetFax!'

    return app
