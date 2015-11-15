"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, render_template

app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

app.config.from_object('config')

import site.controllers
# Import a module / component using its blueprint handler variable (mod_auth)
from app.auth.controllers import mod_auth as auth_module
from app.post.controllers import mod_post as post_module
from app.worship.controllers import mod_worship as worship_module

# Register blueprint(s)
app.register_blueprint(auth_module)
app.register_blueprint(post_module)
app.register_blueprint(worship_module)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
