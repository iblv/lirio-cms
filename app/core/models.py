from app import app
from google.appengine.ext import ndb

class Base(ndb.Model):
    __abstract__ = True

    id = ndb.IntegerProperty(indexed=False)
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    updated_at = ndb.DateTimeProperty(auto_now_add=True)
