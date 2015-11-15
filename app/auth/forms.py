from app.core.forms import *

class LoginForm(Form):
    email    = TextField('Email Address', [Email(), Required(message='Forgot your email address?')])
    password = PasswordField('Password', [Required(message='Must provide a password. ;-)')])

class AdminForm(Form):
    name     = TextField('Name:', [Required(message="Put a nome for user")])
    email    = TextField('Email Address', [Email(), Required(message='Forgot your email address?')])
    password = PasswordField('Initial Password', [Required(message='Must provide a password. ;-)')])
