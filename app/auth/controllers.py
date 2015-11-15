from app.core.controllers import *
from app.auth.forms import LoginForm, AdminForm
from app.auth.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

@mod_auth.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    # Verify the sign in form
    if form.validate_on_submit():
        user = User.query(User.email == form.email.data).get()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            flash('Welcome %s' % user.name)
            return redirect(url_for('auth.home'))

        flash('Invalid email or password', 'error')

    return render_template("auth/signin.html", form=form)


@mod_auth.route('/admin/', methods=['GET','POST'])
def admin():
    logged_user = google_users.get_current_user()
    form = AdminForm(request.form)
    if form.validate_on_submit():
        user = User()
        user.email = form.email.data
        user.name = form.name.data
        user.password = generate_password_hash(form.password.data)
        user.put()
        return redirect(url_for('auth.admin'))


    users = User.query().order(-User.created_at)
    return render_template("auth/admin.html", form=form, users=users, logged_user=logged_user, google_users=google_users)
