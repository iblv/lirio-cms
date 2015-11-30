# -*- coding: utf-8 -*-
import unittest
import os
from app import app as site
from test.fixtures.users import *
from test.fixtures.posts import *
from test.fixtures.worships import *

class IntegrationTestCase(unittest.TestCase):
  def setUp(self):
    site.config.from_object('app.config')
    site.config['TESTING'] = True
    site.config['WTF_CSRF_ENABLED'] = False
    self.app = site.test_client()

  def login(self, email, password):
    return self.app.post('/auth/login/', data=dict(email=email, password=password), follow_redirects=True)

  def logout(self):
      return self.app.get('/auth/logout', follow_redirects=True)

  def test_home(self):
    response = self.app.get('/')
    assert '<title>Lírio CMS</title>' in response.data

  def test_contacts(self):
    response = self.app.get('/contacts')
    assert 'Contatos' in response.data

  def test_about(self):
    response = self.app.get('/about')
    assert 'About' in response.data

  def test_auth_login(self):
    response = self.app.get('/auth/login', follow_redirects=True)
    assert 'Please sign in' in response.data

  def test_failed_authentication(self):
    response = self.login('test@myemail.com', 'secrets')
    assert 'Invalid email or password' in response.data

  def test_authentication(self):
    response = self.login('test@myemail.com', 'secret')
    assert '<div class="alert alert-success">Welcome Test User</div>' in response.data

  def test_show_post(self):
    p = post_test()
    response = self.app.get('/'+p.url)
    assert p.content in response.data

  def test_list_post_by_tag_name(self):
    p = post_test()
    tag = p.tags[0].name
    response = self.app.get('/tag/'+tag)
    assert p.description in response.data

  def test_worship_list(self):
    w = worship1()
    response = self.app.get('/worships')
    assert w.name in response.data
    assert w.schedule in response.data


if __name__ == '__main__':
  unittest.main()
