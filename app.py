from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello/')
def hello_world():
    return 'Hello, World!'


@app.route('/usr/<username>/')
def show_user_profile(username):
    # show the user profile for that user
    return 'User {0}'.format(username)


@app.route('/post/<int:post_id>/')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post {0}'.format(post_id)


@app.route('/projects/')
# routes with the trailing slash will redirect naked requests to the .../ version
def projects():
    return 'The project page'


@app.route('/about')
# omitting the trailing slash returns a HTTP 404 if the slash is included in the request
def about():
    return "the about page"
