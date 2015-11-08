from app.core.models import Base

class Post(Base):
    tags = ndb.StringProperty(repeated=True)
