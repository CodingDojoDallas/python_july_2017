import binascii, md5, os, re
from flask import flash, Flask, redirect, render_template, request, session
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = "ThisIsSecret"
mysql = MySQLConnector(app, 'wall')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# HELPER METHODS
# Create a new user
def createUser(form_data):
    salt = binascii.b2a_hex(os.urandom(15))
    password = str(form_data['password'])
    hashed_pw = md5.new(password + salt).hexdigest()

    query = "INSERT INTO users (first_name, last_name, email, salt, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :salt, :password, NOW(), NOW())"
    data = {
        'first_name': form_data['first_name'],
        'last_name': form_data['last_name'],
        'email': form_data['email'],
        'salt': salt,
        'password': hashed_pw,
    }

    return mysql.query_db(query, data)

# Get the current user from database
def getCurrentUser():
    user_id = session['user_id']

    query = "SELECT * FROM users where id = :id LIMIT 1"
    data = {'id': user_id}

    return  mysql.query_db(query, data)[0]

# Get a user based on column data
def getUser(email):
    query = "SELECT * FROM users where email = :email"
    data = {'email': email}

    record = mysql.query_db(query, data)

    return record[0] if record != [] else record 

# Create a new message
def createMessage(form_data, user):
    query = "INSERT INTO messages (content, user_id, created_at, updated_at) VALUES (:content, :user_id, NOW(), NOW())"
    data = {
        'content': form_data['content'],
        'user_id': user['id'],
    }

    return mysql.query_db(query, data)

# Get one message
def getMessage(id):
    query = "SELECT * from messages where id = :id LIMIT 1"
    data = {'id': id}

    return mysql.query_db(query, data)[0]

# Get all messages
def getMessages():
    query = "SELECT messages.*, users.first_name, users.last_name, users.email FROM messages JOIN users on messages.user_id = users.id ORDER BY messages.id DESC"

    return mysql.query_db(query)

# Delete a message
def deleteMessage(id):
    query = "DELETE FROM messages where id = :id"
    data = {'id': id}

    return mysql.query_db(query, data)

# Create a new comment
def createComment(form_data, user, message):
    query = "INSERT INTO comments (content, user_id, message_id, created_at, updated_at) VALUES (:content, :user_id, :message_id, NOW(), NOW())"
    data = {
        'content': form_data['content'],
        'user_id': user['id'],
        'message_id': message['id'],
    }

    return mysql.query_db(query, data)

# Get all comments
def getComments():
    query = "SELECT comments.*, users.first_name, users.last_name, users.email FROM comments JOIN users on comments.user_id = users.id JOIN messages on comments.message_id = messages.id ORDER BY comments.id DESC"

    return mysql.query_db(query)

# Delete comments
def deleteComments(message_id):
    query = "DELETE FROM comments where message_id = :message_id"
    data = {'message_id': message_id}

    return mysql.query_db(query, data)

# Check for register validation errors
def registerValidations(form_data):
    errors = []

    # Check for required inputs
    for key, input in form_data.iteritems():
        if len(input) == 0:
            errors.append("{} is required.".format(key))
    # Valid Email Format
    if not EMAIL_REGEX.match(form_data['email']):
        errors.append("email is not in a valid format.")
    # Unique Email
    if getUser(form_data['email']) != []:
        errors.append("email is already in use.")
    # Password Matches
    if form_data['password'] != form_data['password_confirmation']:
        errors.append("password do not match.")

    return errors

# Check for login validation errors
def loginValidations(form_data, user):
    errors = []
    user_password = ''
    password = str(form_data['password'])

    # Hash the password input
    if user:
        user_password = user['password']
        password = md5.new(password + user['salt']).hexdigest()

    # Check for required fields
    for key, value in form_data.iteritems():
        if len(value) == 0:
            errors.append("{} is required.".format(key))
    # Valid Email Format
    if not EMAIL_REGEX.match(form_data['email']):
        errors.append("email is not in a valid format.")
    # Invalid Email
    if user == []:
        errors.append("email is not registered.")
    # Invalid Password
    if password != user_password:
        errors.append("Incorrect password.")

    return errors

# Check for message validation errors
def messageValidations(form_data):
    errors = []

    content_length = len(form_data['content'])

    if content_length < 1:
        errors.append("Message content is required.")
    if content_length > 300:
        errors.append("Message content length requirement is 300 characters.")

    return errors

# Check for comment validation errors
def commentValidations(form_data):
    errors = []

    content_length = len(form_data['content'])

    if content_length < 1:
        errors.append("Comment content is required.")
    if content_length > 150:
        errors.append("Comment content length requirement is 150 characters.")

    return errors

# Add errors to flash
def flashErrors(errors, category):
    for error in errors:
        flash(error, category)

# Add messages to flash
def flashMessages(messages):
    for message in messages:
        flash(message)
# END HELPER METHODS

# Landing Page
@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/wall')

    return render_template('index.html')

# Wall Page
@app.route('/wall')
def wall():
    if 'user_id' in session:
        user = getCurrentUser()
        messages = getMessages()
        comments = getComments()

        return render_template('wall.html', user=user, messages=messages, comments=comments)

    flashErrors(['Please register or login first.'], 'register')

    return redirect('/')

# SESSION ROUTES
# Process Registration Data
@app.route('/register', methods=['post'])
def register():
    # Check for registration errors
    errors = registerValidations(request.form)

    # If no errors exist
    if not errors:
        user_id = createUser(request.form)
        session['user_id'] = user_id

        notification = "Weclome {}!".format(request.form['first_name'])
        flashMessages([notification])

        return redirect('/wall')

    # Errors are present
    flashErrors(errors, 'register')

    return redirect('/')

# Process Login Data
@app.route('/login', methods=['post'])
def login():
    # Check for login validation errors
    user = getUser(request.form['email'])
    errors = loginValidations(request.form, user)

    # If no errors exist
    if not errors:
        session['user_id'] = user['id']

        notification = "Welcome back {}".format(user['first_name'])
        flashMessages([notification])

        return redirect('/wall')

    # Errors are preset
    flashErrors(errors, 'login')

    return redirect('/')

# Logout Current User
@app.route('/logout')
def logout():
    if 'user_id' in session:
        session.pop('user_id')

    return redirect('/')
# END SESSION ROUTES

# MESSAGE ROUTES
@app.route('/message-create', methods=['post'])
def messageCreate():
    if 'user_id' in session:
        # Check for message validation errors
        errors = messageValidations(request.form)

        # If no errors exist
        if not errors:
            current_user = getCurrentUser()
            message_id = createMessage(request.form, current_user)

            notification = "Message successfully created!"
            flashMessages([notification])

            return redirect('/wall')

        # Errors exist
        flashErrors(errors, 'post')

    return redirect('/wall')

@app.route('/message-delete/<message_id>', methods=['post'])
def messageDelete(message_id):
    if 'user_id' in session:
        user = getCurrentUser()
        message = getMessage(message_id)

        if user['id'] == message['user_id']:
            deleteComments(message_id)
            deleteMessage(message_id)

            notification = "Message successfully deleted."
            flashMessages([notification])

            return redirect('/wall')

        error = "You are not authorized to delete that message." 
        flashErrors([errors], 'post')

    return redirect('/wall')
# END MESSAGE ROUTES

# COMMENT ROUTES
@app.route('/comment-create/<message_id>', methods=['post'])
def commentCreate(message_id):
    if 'user_id' in session:
        # Check for comment validation errors
        errors = commentValidations(request.form)

        # If no errors exist
        if not errors:
            current_user = getCurrentUser()
            message = getMessage(message_id)
            comment_id = createComment(request.form, current_user, message)

            notification = "Comment successfully created!"
            flashMessages([notification])

            return redirect('/wall')

        # Errors exist
        flashErrors(errors, 'comment') 

    return redirect('/wall')
# END COMMENT ROUTES

if __name__ == '__main__':
    app.run(debug=True)
app.run()