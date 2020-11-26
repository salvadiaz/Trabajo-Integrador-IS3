from app import app, count_vote, get_redis
import requests
import unittest

class UnitTest(unittest.TestCase):
    
  url = 'https://is3-vote.herokuapp.com/'

  def test_get_status_200(self):
    app.testing = True  
    tester = app.test_client(self)
    response = tester.get(self.url)
    self.assertEqual(response.status_code, 200)

  def test_post_status_200(self):
    payload={'vote': 'a'}
    headers = {
      'Cookie': 'voter_id=39e29be59e1d5c6'
    }
    response = requests.post(self.url, headers=headers, data=payload)
    self.assertEqual(response.status_code, 200)

  def test_post_status_400(self):
    app.testing = True  
    tester = app.test_client(self)
    response = tester.post(self.url)
    self.assertEqual(response.status_code, 400)

  def test_get_voter_id_cookie(self):
    validCookie='39e29be59e1d5c6'
    payload={'vote': 'a'}
    headers = {
      'Cookie': 'voter_id=39e29be59e1d5c6'
    }
    response = requests.post(self.url, headers=headers, data=payload)
    self.assertEqual(response.cookies["voter_id"], validCookie)

  def test_set_new_cookie(self):
    payload={'vote': 'a'}
    response = requests.post(self.url, data=payload)
    assert response.cookies["voter_id"] is not None
