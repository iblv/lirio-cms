from app.core.controllers import *
from app import app

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template("site/index.html")

@app.route('/contatos')
def contatos():
    """Return a friendly HTTP greeting."""
    return render_template("site/contatos.html")
