from app.core.forms import *

class PostForm(Form):
    url = TextField('URL')
    title = TextField('Title',[Required(message='Title required')])
    content = TextAreaField('Content')
    description = TextAreaField('Description',[Length(max=100)])
    category = TextField('Category')
    tags = TextField('Tags')
    post_type = SelectField('Post Type', choices=[('page','Page'),('post','Post')])
    post_status = SelectField('Status', choices=[('draft','Draft'),('published','Published')])
