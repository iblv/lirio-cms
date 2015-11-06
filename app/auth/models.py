from app.core.models import Base

class User(Base):
    name = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)
    password = ndb.StringProperty(indexed=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)
