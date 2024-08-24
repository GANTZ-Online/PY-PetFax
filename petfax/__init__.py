from flask import Flask 

def create_app(): 
    app = Flask(__name__, template_folder='templates')

 # register pet blueprint 
    from . import pet
    app.register_blueprint(pet.bp)

    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'

    from . import facts
    app.register_blueprint(facts.bp)

    return app



