from flask import Blueprint, render_template
import json

# Create a Blueprint instance for the pet routes
bp = Blueprint('pet', __name__, url_prefix="/pets")

# Load the JSON data from 'pets.json' file
pets = json.load(open('pets.json'))
print(pets)

@bp.route('/')
def index():
    return render_template('index.html', pets=pets)
