from app.core.models import *
from app.auth.models import User

class Category(Base):
    name = ndb.StringProperty()

class Tag(Base):
    name = ndb.StringProperty()

class Post(Base):
    url = ndb.StringProperty()
    title = ndb.StringProperty()
    description = ndb.StringProperty()
    content = ndb.TextProperty()
    author = ndb.StructuredProperty(User)
    category = ndb.StructuredProperty(Category)
    tags = ndb.StructuredProperty(Tag, repeated=True)
    post_type = ndb.StringProperty()
    post_status = ndb.StringProperty()

    
class PostTag(Base):
    post = ndb.StructuredProperty(Post)
    tag = ndb.StructuredProperty(Tag)
