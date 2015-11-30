# import pytest
from test.fixtures.categories import *
from test.fixtures.tags import *
from test.fixtures.users import *
from app.post.models import Post

@pytest.fixture
def post_test():
  tags = [tag_pastor(),tag_computer()]
  post = Post(title='My Test Post',
                    description='My Test Description',
                    content='My test content',
                    post_type='post',
                    post_status='published',
                    author=test_user(),
                    category=category_sermon(),
                    tags=tags)
  post.url = post.slugify(post.title)
  post.put()
  return post

@pytest.fixture
def page_test():
  tags = [tag_event]
  page = Post(title='My Test Page',
                    description='My Test Page Description',
                    content='My test page content',
                    post_type='page',
                    post_status='publisehd',
                    author=test_user,
                    category=category_worship,
                    tags=tags)
  page.url = page.slugify(page.title)
  page.put()
  return page
