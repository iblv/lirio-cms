from app.core.controllers import *
from app.post.forms import PostForm
from app.auth.models import User
from app.post.models import Post, Tag, Category

mod_post = Blueprint('posts', __name__, url_prefix='/posts')

@mod_post.before_request
def before_request():
    if 'user_id' not in session:
        return redirect('/auth/login/')

@mod_post.route('/new/', methods=['GET', 'POST'])
def new():
    method = 'POST'
    action = '.'
    form = PostForm(request.form)
    if form.validate_on_submit():
        post = Post()
        post = set_post(post,form)
        print(post)
        post.put()
        flash('Post created!')
        return redirect(url_for('.index'))
    return render_template("posts/new.html", form=form, method=method, action=action)

@mod_post.route('/')
def index():
    posts = Post.query().order(-Post.created_at)
    return render_template("posts/index.html", posts=posts)

@mod_post.route('/<int:id>/edit/', methods=['GET', 'POST'])
def edit(id):
    method = 'POST'
    action = '.'
    post = Post.get_by_id(id)
    form = PostForm(request.form, post)
    form.category.data = post.category.name
    tags = []
    for tag in post.tags:
        tags.append(tag.name)
    form.tags.data = ','.join(tags)
    if form.validate_on_submit():
        post = set_post(post,form)
        post.put()
        flash('Post updated!')
    return render_template("posts/edit.html", form=form, method=method, action=action)


def set_post(post,form):
    post.title=form.title.data
    if(post.url==None or post.url==''):
        post.url=post.slugify(post.title)
    else:
        post.url=post.slugify(post.url)
    post.description=form.description.data
    post.content=form.content.data
    post.post_type=form.post_type.data
    post.post_status=form.post_status.data
    post.author=User.get_by_id(session['user_id'])
    post.category=Category(name=form.category.data)
    my_tags = []
    for tag in form.tags.data.lower().split(','):
        my_tags.append(Tag(name=tag))
    post.tags=my_tags

    return post
