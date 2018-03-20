from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' %username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' %post_id


# @app.route('/login')
# def login(): pass
#
# @app.route('/user/<username>')
# def profile(username): pass
#
# with app.test_request_context():
# print(url_for('login'))
# print(url_for('login', next='/'))
# print(url_for('profile', username='John Doe'))
