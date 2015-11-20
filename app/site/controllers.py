from app.core.controllers import *
from app.post.models import Post
from app import app

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template("site/index.html")

@app.route('/<string:url>')
def find_by_url(url):
    post = Post.query(Post.url==url, Post.post_status!='draft').get()

    return render_template("site/post.html", post=post)

@app.route('/tag/<string:tag>')
def find_by_tag_name(tag):
    posts = Post.query(Tag.name==tag, Post.post_status!='draft')
    return render_template("site/post_list.html", posts=posts)

@app.route('/contatos')
def contatos():
    """Return a friendly HTTP greeting."""
    return render_template("site/contatos.html")
