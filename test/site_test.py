import sys
import unittest
# sys.path.append('../app')

import app

class SiteTestCase(unittest.TestCase):
  def setUp(self):
    site.app.config['TESTING'] = True
    self.app = site.app.test_client()

  def test_home(client):
    response = client.get('/')
    print(response.data)

if __name__ == '__main__':
  unittest.main()
