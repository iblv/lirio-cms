from app import app
from google.appengine.ext import ndb

class Base(ndb.Model):
    __abstract__ = True
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    updated_at = ndb.DateTimeProperty(auto_now_add=True)

    before_save_defs = []
    after_save_defs = []
    validation_defs = []
    errors = {}

    @classmethod
    def all(self):
      return self.query()

    def save(self):
      call_defs('validation_defs')
      call_defs('before_save_defs')
      self.put()
      call_defs('after_save_defs')

    def after_save(self, definition_name):
      return after_save_defs.extend(definition_name)

    def before_save(self, definition_name):
      return before_save_defs.extend(definition_name)

    def validates(self, definition_name):
      return validation_defs.extend(definition_name)

    def call_defs(self, definition_block_name):
      for definition in getattr(self, definition_block_name):
        result = getattr(self, definition)()
        if(definition_block_name == 'validation_defs'):
          try:
            result==True
          except:
            print "Validation error:", sys.exc_info()[0]
            raise
