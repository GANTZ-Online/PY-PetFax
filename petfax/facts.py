from flask import Blueprint, render_template, request, redirect, url_for

# Create a Blueprint instance for the facts routes
bp = Blueprint('facts', __name__, url_prefix="/facts")

# Route for displaying the form to submit new facts
@bp.route('/new', methods=['GET'])
def new_fact():
    return render_template('facts/new.html')

# Route for handling form submission
@bp.route('/submit', methods=['POST'])
def submit_fact():
    print(request.form)  # Output form data to the console
    return redirect(url_for('facts.new_fact'))

# Route for displaying a thank you message
@bp.route('/', methods=['POST'])
def index_post():
    return 'Thanks for submitting a fun fact!'

# Route for displaying a facts index page (GET and POST)
@bp.route('/', methods=['GET', 'POST'])
def index_get_post():
    if request.method == 'POST':
        print(request.form)
        return redirect('/facts')
    
    return 'This is the facts index'
