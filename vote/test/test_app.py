import requests
import unittest
import xmlrunner


class UnitTest(unittest.TestCase):
    url = 'https://vote-is3.herokuapp.com/'

    def test_get_status_200(self):
        response = requests.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_incomplete_vote_status_400(self):
        response = requests.post(self.url)
        self.assertEqual(response.status_code, 400)  # Bad Req

    def test_set_new_cookie(self):
        payload = {'vote': 'a'}
        response = requests.post(self.url, data=payload)
        assert response.cookies["voter_id"] is not None


if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        # these make sure that some options that are not applicable
        # remain hidden from the help menu.
        failfast=False, buffer=False, catchbreak=False)
