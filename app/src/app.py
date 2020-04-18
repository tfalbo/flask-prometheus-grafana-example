from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app, Counter

#prometheus
visitCounter = Counter('visits', 'Visit Counter')
userCounter = Counter('user', 'User Counter', ['username'])
postCounter = Counter('post', 'Post Counter', ['post_id'])

app = Flask(__name__)

@app.route('/')
def hello_world():
    visitCounter.inc(1)
    return 'Hello, World!'

@app.route('/user/<username>')
def show_user_profile(username):
    userCounter.labels(username).inc()
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    postCounter.labels(post_id).inc()
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

# Add prometheus wsgi middleware to route /metrics requests
app_dispatch = DispatcherMiddleware(app, {
    '/metrics': make_wsgi_app()
})