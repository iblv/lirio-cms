import pytest
from werkzeug import generate_password_hash
from app.auth.models import User

@pytest.fixture
def test_user():
  user = User(name='Test User', email='test@myemail.com', password=generate_password_hash('secret'))
  user.put()
  return user
