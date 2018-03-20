from flask import Flask, url_for, Request, render_template
import test_calculation
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


def results():
    exit_price = Request.form['exit_price']

    return exit_price


# @app.route('/hello')
# def hello_world():
#     return 'Hello, World!'
#
# @app.route('/user/<username>')
# def show_user_profile(username):
#     return 'User %s' %username
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return 'Post %d' %post_id


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
