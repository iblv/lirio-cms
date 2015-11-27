"""
`appengine_config.py` is automatically loaded when Google App Engine
starts a new instance of your application. This runs before any
WSGI applications specified in app.yaml are loaded.
"""

from google.appengine.ext import vendor
from google.appengine.api import namespace_manager

# Third-party libraries are stored in "lib", vendoring will make
# sure that they are importable by the application.
vendor.add('lib')

# Called only if the current namespace is not set.
def namespace_manager_default_namespace_for_request():
    return 'default'
