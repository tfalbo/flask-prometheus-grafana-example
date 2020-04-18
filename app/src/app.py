from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app, Counter

# Prometheus Counters
c = Counter('visits', 'Visit Counter')

app = Flask(__name__)

@app.route('/')
def hello_world():
    c.inc()
    return 'Hello, World!'


# Add prometheus wsgi middleware to route /metrics requests
app_dispatch = DispatcherMiddleware(app, {
    '/metrics': make_wsgi_app()
})