# Introduction to Flask Framework (Python 3)

Welcome to the introduction coursework for Flask Framework using Python 3. This guide is designed for Stanford students and focuses on key concepts, each accompanied by at least three examples.

## 1. Flask Application Setup

Flask is a micro web framework that's easy to set up and get started with.

### Examples:

a. Basic Flask application:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
```

b. Flask application with configuration:
```python
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'your-secret-key'
```

c. Flask application factory pattern:
```python
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')

    from .views import main
    app.register_blueprint(main)

    return app
```

## 2. Routing

Routing in Flask maps URLs to specific functions that handle requests.

### Examples:

a. Basic route:
```python
@app.route('/about')
def about():
    return 'About Page'
```

b. Route with variable:
```python
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'
```

c. Route with HTTP methods:
```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic
        pass
    return render_template('login.html')
```

## 3. Templates

Flask uses Jinja2 as its template engine to generate dynamic HTML.

### Examples:

a. Basic template rendering:
```python
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html', title='Home')
```

b. Template with variable:
```html
<!-- templates/greeting.html -->
<h1>Hello, {{ name }}!</h1>
```
```python
@app.route('/greet/<name>')
def greet(name):
    return render_template('greeting.html', name=name)
```

c. Template inheritance:
```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{% endblock %} - My Site</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>

<!-- templates/home.html -->
{% extends "base.html" %}
{% block title %}Home{% endblock %}
{% block content %}
    <h1>Welcome to my site!</h1>
{% endblock %}
```

## 4. Request Handling

Flask provides easy access to request data, including form data, query parameters, and headers.

### Examples:

a. Accessing query parameters:
```python
from flask import request

@app.route('/search')
def search():
    query = request.args.get('q', '')
    return f'Search results for: {query}'
```

b. Handling form data:
```python
@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    # Process form data
    return f'Received: {username}'
```

c. Accessing JSON data:
```python
@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    # Process JSON data
    return jsonify({'status': 'success', 'received': data})
```

## 5. Database Integration

Flask can be easily integrated with various databases, often using Flask-SQLAlchemy for ORM.

### Examples:

a. Setting up SQLAlchemy:
```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
```

b. Defining a model:
```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
```

c. Using the database in a route:
```python
@app.route('/user/<username>')
def user_profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('profile.html', user=user)
```

## 6. Flask Extensions

Flask has a rich ecosystem of extensions that add functionality to your application.

### Examples:

a. Flask-WTF for form handling:
```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
```

b. Flask-Login for user session management:
```python
from flask_login import LoginManager, login_user, login_required, logout_user

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)
```

c. Flask-RESTful for building APIs:
```python
from flask_restful import Resource, Api

api = Api(app)

class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return {'id': user.id, 'username': user.username}

api.add_resource(UserResource, '/api/user/<int:user_id>')
```

## 7. Error Handling

Flask provides ways to handle errors and exceptions gracefully.

### Examples:

a. Basic error handler:
```python
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
```

b. Custom exception handling:
```python
class APIError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

@app.errorhandler(APIError)
def handle_api_error(error):
    response = jsonify({'error': error.message})
    response.status_code = error.status_code
    return response
```

c. Logging errors:
```python
import logging
from logging.handlers import RotatingFileHandler

if not app.debug:
    file_handler = RotatingFileHandler('error.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)

@app.route('/example')
def example():
    app.logger.warning('A warning occurred')
    return 'Check your logs'
```

This introduction covers the fundamental concepts of Flask with multiple examples for each. As you progress through the course, you'll delve deeper into these concepts and learn how to build efficient and scalable web applications using Flask.



I've created an introductory coursework for Flask Framework using Python 3, focusing on key concepts with at least three examples for each. The content is structured as a markdown document, similar to the Django coursework.

The Flask coursework covers seven fundamental concepts:
1. Flask Application Setup
2. Routing
3. Templates
4. Request Handling
5. Database Integration
6. Flask Extensions
7. Error Handling

Each section includes a brief explanation of the concept followed by at least three practical examples. This structure should help students understand both the theory and practical application of Flask concepts.

The main differences you'll notice compared to the Django coursework are:

1. Flask is a micro-framework, so the setup is generally simpler and more lightweight.
2. Routing in Flask is often done using decorators, which is different from Django's URL configuration.
3. Flask uses Jinja2 for templating, which is similar to Django's template language but with some syntax differences.
4. Database integration in Flask often uses Flask-SQLAlchemy, while Django has its own ORM.
5. Flask relies more heavily on extensions for additional functionality, whereas Django includes more features out of the box.

Would you like me to explain or elaborate on any specific part of this Flask coursework? Or perhaps you'd like to see a comparison between specific Flask and Django concepts?
