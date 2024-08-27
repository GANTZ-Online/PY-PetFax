from flask import Blueprint, render_template, request, redirect, url_for
from . import models

# Create a Blueprint instance for the facts routes
bp = Blueprint('facts', __name__, url_prefix="/facts")

# Route for displaying the form to submit new facts
# @bp.route('/new', methods=['GET'])
# def new_fact():
#     return render_template('facts/new.html')

# # Route for handling form submission
# @bp.route('/submit', methods=['POST'])
# def submit_fact():
#     print(request.form)  # Output form data to the console
#     return redirect(url_for('facts.new_fact'))

# # Route for displaying a thank you message
# @bp.route('/', methods=['POST'])
# def index_post():
#     return 'Thanks for submitting a fun fact!'

# # Route for displaying a facts index page and handling form submission
# @bp.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         submitter = request.form['submitter']
#         fact = request.form['fact']

#         new_fact = models.Fact(submitter=submitter, fact=fact)
#         models.db.session.add(new_fact)
#         models.db.session.commit()

#         return redirect('/facts')
    
#     # Retrieve and print all facts
#     results = models.Fact.query.all()
#     for result in results:
#         print(result)

#     # Render the facts index page
#     return render_template('facts/index.html')

@bp.route('/', methods=['GET', 'POST'])
def index(): 
    if request.method == 'POST':
        submitter = request.form['submitter']
        fact = request.form['fact']

        new_fact = models.Fact(submitter=submitter, fact=fact)
        models.db.session.add(new_fact)
        models.db.session.commit()

        return redirect('/facts')
    
    results = models.Fact.query.all()
    for result in results:
        print
    return render_template('facts/index.html', facts=results)



@bp.route('/new', methods=['GET', 'POST'])
def new_fact():
    return render_template('facts/new.html')
    
