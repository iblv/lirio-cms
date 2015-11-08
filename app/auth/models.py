from app.core.models import Base, ndb

class User(Base):
    name = ndb.StringProperty(indexed=True)
    email = ndb.StringProperty(indexed=True)
    password = ndb.StringProperty(indexed=True)
