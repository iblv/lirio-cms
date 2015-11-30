from app.core.models import *
from app.auth.models import User
import re
from unidecode import unidecode

class Category(Base):
    name = ndb.StringProperty()

class Tag(Base):
    name = ndb.StringProperty()

class Post(Base):
    url = ndb.StringProperty()
    title = ndb.StringProperty()
    description = ndb.StringProperty()
    content = ndb.TextProperty()
    post_type = ndb.StringProperty()
    post_status = ndb.StringProperty()
    author = ndb.StructuredProperty(User)
    category = ndb.StructuredProperty(Category)
    tags = ndb.StructuredProperty(Tag, repeated=True)

    def get_post_type(self):
        if(self.post_type=='page'):
            type = 'Page'
        elif(self.post_type=='post'):
            type = 'Post'
        else:
            type = ''

        return type


    def get_post_status(self):
        if(self.post_status=='draft'):
            status = 'Draft'
        elif(self.post_status=='published'):
            status = 'Published'
        else:
            status = ''

        return status

    def slugify(self, text, delim=u'-'):
        """Generates an ASCII-only slug."""
        _punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')
        result = []
        for word in _punct_re.split(text.lower()):
            result.extend(unidecode(word).split())
        return unicode(delim.join(result))


class PostTag(Base):
    post = ndb.StructuredProperty(Post)
    tag = ndb.StructuredProperty(Tag)
