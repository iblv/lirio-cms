from app.core.controllers import *
from app.post.forms import PostForm
from app.post.models import Post, Tag, Category

mod_post = Blueprint('posts', __name__, url_prefix='/posts')

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
    form = PostForm(request.form)
    if form.validate_on_submit():
        post = Post.get_by_id(id)
        post = set_post(post,form)
        post.put()
        flash('Post updated!')
    return render_template("posts/edit.html", form=form, method=method, action=action)


def set_post(post,form):
    post.url=form.url.data
    post.title=form.title.data
    post.description=form.description.data
    post.content=form.content.data
    post.post_type=form.post_type.data
    post.post_status=form.post_status.data
    # post.author=form.author.data
    post.category=Category(name=form.category.data)
    my_tags = []
    for tag in form.tags.data.split(','):
        my_tags.append(Tag(name=tag))
    post.tags=my_tags

    return post
