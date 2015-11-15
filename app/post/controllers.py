from app.core.controllers import *
from app.post.forms import PostForm
from app.post.models import Post

mod_post = Blueprint('posts', __name__, url_prefix='/posts')

@mod_post.route('/new/', methods=['GET', 'POST'])
def new():
    method = 'POST'
    action = '/posts'
    form = PostForm(request.form)
    return render_template("posts/new.html", form=form, method=method, action=action)

@mod_post.route('/')
def index():
    posts = Post.query().order(-Post.created_at)
    return render_template("posts/index.html", posts=posts)

@mod_post.route('/<int:id>/edit/', methods=['GET', 'POST'])
def edit(id):
    method = 'PUT'
    action = '/posts/'+str(id)
    form = PostForm(request.form)
    return render_template("posts/edit.html", form=form, method=method, action=action)
