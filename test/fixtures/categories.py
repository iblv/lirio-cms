import pytest
from app.post.models import Category

@pytest.fixture
def category_sermon():
  cat = Category(name='Sermon')
  cat.put()
  return cat

@pytest.fixture
def category_worship():
  cat = Category(name='Worship')
  cat.put()
  return cat
