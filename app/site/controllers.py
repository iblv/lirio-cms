from app.core.controllers import *
from app import app

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template("site/index.html")

@app.route('/<string:url>')
def find_by_url(url):
    post = Post.query(Post.url==url)
    return render_template("site/post.html")

@app.route('/<string:tag>')
def find_by_tag_name(tag):
    post = Post.query(Tag.name==tag)
    return render_template("site/post_list.html")

@app.route('/contatos')
def contatos():
    """Return a friendly HTTP greeting."""
    return render_template("site/contatos.html")
