from flask import Blueprint, render_template, request, redirect, url_for

# Create a Blueprint instance for the facts routes
bp = Blueprint('facts', __name__, url_prefix="/facts")

# Route for displaying the form to submit new facts
@bp.route('/new', methods=['GET'])
def new_fact():
    return render_template('facts/new.html')

# Route for handling form submission (will be implemented later)
@bp.route('/submit', methods=['POST'])
def submit_fact():
    # Process form submission here in future lessons
    # For now, we'll just redirect to the new fact page
    return redirect(url_for('facts/new'))

