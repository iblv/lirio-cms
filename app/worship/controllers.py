from app.core.controllers import *
from app.worship.forms import WorshipForm
from app.worship.models import Worship

mod_worship = Blueprint('worships', __name__, url_prefix='/worships')

@mod_worship.before_request
def before_request():
    if 'user_id' not in session:
        return redirect('/auth/login/')

@mod_worship.route('/')
def index():
    worships = Worship.query()
    return render_template("worships/index.html",worships=worships)

@mod_worship.route('/new/', methods=['GET', 'POST'])
def new():
    method = 'POST'
    action = '.'
    form = WorshipForm(request.form)
    if form.validate_on_submit():
        worship = Worship()
        form.populate_obj(worship)
        worship.put()
        flash('Worship created!')
        return redirect(url_for('.index'))
    return render_template("worships/new.html", form=form, method=method, action=action)

@mod_worship.route('/<int:id>/edit/',methods=['GET','POST'])
def edit(id):
    method = 'POST'
    action = '.'
    worship = Worship.get_by_id(id)
    form = WorshipForm(request.form, worship)
    if form.validate_on_submit():
        worship = Worship.get_by_id(id)
        form.populate_obj(worship)
        worship.put()
        flash('Worship updated!')
    return render_template("worships/edit.html", form=form, method=method, action=action)
