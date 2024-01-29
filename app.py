import os, copy
from flask import Flask, request, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.user import User
from lib.user_repository import UserRepository
from lib.listing import Listing
from lib.listing_repository import ListingRepository
from lib.availability import Availability
from lib.availability_repository import AvailabilityRepository


# Create a new Flask app
app = Flask(__name__)




########################
# SESSION pass key
#
app.secret_key = b"_5#2LF34nxec]"
########################            


# STRUCTURE
# ==========
# home page menu: about  | login  |  register
# standard menu: spaces | my listings | requests | signout
# forms menu: cancel
#
# HOME ROUTES:
# / GET
#       /<home_page_section>  GET        shows all listings or user listings, nav menu: standard
# ACCOUNT ROUTES:
# /account/<section>  GET    shows login or logout, nav menu: shows only cancel
# /user/<section>  POST     submit form
# SPACES ROUTES:
# /spaces/edit/<id>   GET       allow to list a new space or edit an existing space,  na menu: show only cancel
#       /spaces/add POST        add 1 space (no html) --> /
#       /spaces/update POST        update 1 space (no html) --> /
#



# ==== Home Page - routes
#
#   active_user: None or user_instance
#   index_section_id: .....
#
#
@app.route('/', methods=['GET'])
def index():
    return redirect('/index')

@app.route('/<home_page_section>', methods=['GET'])
def index_subsection(home_page_section):
    if 'id' in session:
        space_repository = SpaceRepository(get_flask_database_connection(app))
        rows = space_repository.all(session['id'])       
    else:
        rows = []
    return render_template('index.html', data=rows)



# ==== Account routes
#
#   GET arg: login
#             register
# 
@app.route('/account/<section>', methods=['GET'])
def login(section):
    if all(['email_address' not in session and
            any([
                section == 'login',
                section == 'register'
                ])
            ]):
        return render_template('account.html', login_status=section)
    elif all([
        section == 'logout',
        'email_address' in session
        ]):
        session.pop('id', None)
        session.pop('fullname', None)
        session.pop('email_address', None)
    return redirect('/')


@app.route('/user/<section>', methods=['POST'])
def user(section):
    query_result = (False, 'Generic Error')
    _connection = get_flask_database_connection(app)
    user_repository = UserRepository(_connection)
    if section == 'login':
        email_address = request.form['email_address']
        password = request.form['passcode']
        query_result = user_repository.find(email_address, password)
        #check for valid user entry
        if query_result[0]:
            session['id'] = query_result[1].id
            session['fullname'] = query_result[1].fullname
            session['email_address'] = query_result[1].email_address
            return redirect('/')
    elif section == 'register':
        name = request.form['name']
        email_address = request.form['email_address']
        password = request.form['passcode']
        query_result = user_repository.add(1, name, email_address, password)
        if query_result[0]:
            return redirect('/')
    return f"WRONG: {query_result[1]}"




# ==== Spaces routes
#
#   
# 
@app.route('/spaces/show/edit/<id>', methods=['GET'])
def edit_spaces(id):
    if 'id' in session:
        if not(int(id) == 0):
            # this will populate the form for us
            space_repo = SpaceRepository(get_flask_database_connection(app))
            space = space_repo.find(id)
            availability_repo = AvailabilityRepository(get_flask_database_connection(app))
            availabilities = availability_repo.find(space.id)
            return render_template("space_edit.html", space=space, availabilities=availabilities)
        else:
            #  this will not fill the form
            #return render_template("space_edit.html", space="", availabilities="")
            return render_template("space_edit.html", space="")
    else:
        return "Not Authorized"


@app.route('/spaces/add', methods=['POST'])
def add_spaces():
    id = request.form['id']
    name = request.form['name']
    desc = request.form['desc']
    price = request.form['price']
    user_id = session['id']

    space = Space(id, name, desc, price, user_id)
    space_repo = SpaceRepository(get_flask_database_connection(app))
    space_repo.add(space)
    
    space_id = space_repo.get_id()
    #date_from = request.form['date_from']
    #date_to = request.form['date_to']

   #availability = Availability(date_from, date_to, space_id)
    availability_repo = AvailabilityRepository(get_flask_database_connection(app))
    #availability_repo.add(availability)

    return redirect('/')


@app.route('/spaces/update', methods=['POST'])
def update_spaces():
    id = request.form['id']
    name = request.form['name']
    desc = request.form['desc']
    price = request.form['price']

    space = Listing(id, name, desc, price)
    space_repo = ListingRepository(get_flask_database_connection(app))
    space_repo.update(space)

    return redirect('/spaces/listings')


@app.route('/spaces/show/add')
def get_add():
     if 'id' in session:
         return render_template("space_add.html")
     else:
         return "Not Authorized"



@app.route('/spaces/show/<id>', methods=['GET'])
def get_space(id):
    space_repo = ListingRepository(get_flask_database_connection(app))
    space = space_repo.find(id)
    if space:
        availability_repo = AvailabilityRepository(get_flask_database_connection(app))
        availabilities = availability_repo.find(space.id)
        return render_template("space_view.html", space=space, availabilities=availabilities)
    #return redirect('/')

@app.route('/spaces/delete/<id>', methods=['GET'])
def delete_space(id):
    space_repo = SpaceRepository(get_flask_database_connection(app))
    space_repo.delete(id)

    return redirect('/spaces/listings')

@app.route('/availability/add', methods=['POST'])
def add_availability():
    space_id = request.form['id']
    date_from = request.form['date_from']
    date_to = request.form['date_to']

    availability = Availability(date_from, date_to, space_id)
    availability_repo = AvailabilityRepository(get_flask_database_connection(app))
    availability_repo.add(availability)
    
    url = '/spaces/show/edit/' + space_id

    return redirect(url)




# @app.route('/mylisting', methods=['GET'])
# def user_listings(id):
#     space_repo = SpaceRepository(get_flask_database_connection(app))
#     space = space_repo.find(id)

#     return render_template("my_listings.html", space=space)

@app.route('/spaces/listings')
def spaces_listings():
    user_id = session['id']
    space_repo = ListingRepository(get_flask_database_connection(app))
    spaces = space_repo.find(user_id, "user_id")
    print(spaces)

    return render_template("space_listings.html", spaces=spaces)




# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))