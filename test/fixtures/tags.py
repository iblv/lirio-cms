import pytest
from app.post.models import Tag

@pytest.fixture
def tag_pastor():
  tag = Tag(name='pastor')
  tag.put()
  return tag

@pytest.fixture
def tag_computer():
  tag = Tag(name='computer')
  tag.put()
  return tag

@pytest.fixture
def tag_event():
  tag = Tag(name='event')
  tag.put()
  return tag
