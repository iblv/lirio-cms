from app.core.models import *

class Worship(Base):
    name = ndb.StringProperty()
    schedule = ndb.StringProperty()
    week_day = ndb.StringProperty()
    pastor = ndb.StringProperty()

    def get_week_day(self):
        week_days = {
            'sunday': 'Sunday',
            'monday': 'Monday',
            'thursday': 'Thursday',
            'wednesday': 'Wednesday',
            'thursday': 'Thursday',
            'friday': 'Friday'
        }
        return week_days[self.week_day]
