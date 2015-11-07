from app.core.models import Base, ndb

class User(Base):
    name = ndb.StringProperty(indexed=True)
    email = ndb.StringProperty(indexed=True)
    password = ndb.StringProperty(indexed=True)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)
