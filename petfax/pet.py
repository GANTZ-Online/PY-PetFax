from flask import Blueprint, render_template
import json

# Create a Blueprint instance for the pet routes
bp = Blueprint('pet', __name__, url_prefix="/pets")

# Load the JSON data from 'pets.json' file
with open('pets.json') as f:
    pets = json.load(f)
print(pets)

@bp.route('/')
def index():
    return render_template('pets/index.html', pets=pets)

@bp.route('/<int:id>')
def show(id):
    pet = pets[id - 1]
    if pet is None:
        return "Pet not found", 404
    return render_template('pets/show.html', pet=pet)
