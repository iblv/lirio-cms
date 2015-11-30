import pytest
from app.worship.models import Worship

@pytest.fixture
def worship1():
  worship = Worship(name='Worship Test',week_day='sunday', schedule='09:00',pastor='Abriran Abilu')
  worship.put()
  return worship
