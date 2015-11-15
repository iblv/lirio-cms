from app.core.forms import *

week_days = [
    ('sunday','Sunday'),
    ('monday','Monday'),
    ('thursday','Thursday'),
    ('wednesday','Wednesday'),
    ('thursday','Thursday'),
    ('friday','Friday')
]

class WorshipForm(Form):
    name = TextField('Name',[Required(message='Name required')])
    schedule = TextField('Schedule',[Required(message='Schedule required')])
    week_day = SelectField('Day of the week',[Required(message='Schedule required')], choices=week_days)
    pastor = TextField('Pastor')
