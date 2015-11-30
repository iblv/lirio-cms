import unittest
from test.fixtures.posts import *

class TestPost(unittest.TestCase):
  def test_slugfy(self):
    p = Post()
    p.title = 'My Title Post'
    p.url = p.slugify(p.title)
    assert p.url == 'my-title-post'

  def test_get_post_status(self):
    p = post_test()
    assert p.get_post_status() == 'Published'

  def test_get_post_type(self):
    p = post_test()
    assert p.get_post_type() == 'Post'
