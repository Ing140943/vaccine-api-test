"""Module for testing Suchon's Site API"""
import requests
import unittest
import datetime


WEB_URL = "https://suchonsite-server.herokuapp.com/people/"


class SuchonServiceSiteTest(unittest.TestCase):
    """Class for test web application API of Suchon's Site(Vaccine Provider)"""

    def test_can_GET_all_users_path_all(self):
        """ Test Case ID #1

            Test that can get all user information correctly and successful."""
        url = WEB_URL + "all"
        response = requests.get(url)
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.ok)

    def test_get_user_with_valid_date(self):
        """ Test Case ID #2

            Test that can get a user information correctly and successful by provide valid date."""
        pub_date = datetime.date.today()
        url = WEB_URL + "by_date/" + pub_date.strftime('%d-%m-%y')
        response = requests.get(url)
        self.assertEqual(204, response.status_code)
        self.assertTrue(response.ok)

    def test_get_status_code_with_future_date(self):
        """Test Case ID #3

            Test that can get a user information correctly and successful by provide future date."""
        pub_date = datetime.date.today() + datetime.timedelta(days=+10)
        url = WEB_URL + "by_date/" + pub_date.strftime('%d-%m-%yy')
        response = requests.get(url)
        self.assertEqual(204, response.status_code)
        self.assertTrue(response.ok)

    def test_get_status_code_without_num_date(self):
        """Test Case ID #4

            Test that can get a user information correctly and successful by provide empty date."""
        url = WEB_URL + "by_date/"
        response = requests.get(url)
        self.assertEqual(406, response.status_code)
        self.assertFalse(response.ok)
        self.assertEqual("Not Acceptable", response.reason)

    def test_invalid_date_format(self):
        """Test Case ID #5

            Test that can get a user information correctly and successful by provide wrong format date."""
        pub_date = datetime.date.today()
        url = WEB_URL + "by_date/" + str(pub_date)
        response = requests.get(url)
        self.assertEqual(204, response.status_code)


    def test_provide_invalid_month_in_date_format(self):
        """Test Case ID #6

            Test that can get a user information correctly and successful by provide wrong format month."""
        url = WEB_URL + "by_date/" + "23-OCT-2021"
        response = requests.get(url)
        self.assertEqual(204, response.status_code)
        self.assertTrue(response.ok)


    def test_provide_slash_in_date_format(self):
        """Test Case ID #7

            Test that can get a user information correctly and successful by provide '/' in date format."""
        url = WEB_URL + "by_date/" + "23/10/2021"
        response = requests.get(url)
        self.assertEqual(404, response.status_code)
        self.assertFalse(response.ok)
        self.assertEqual("Not Found", response.reason)

    def test_provide_wrong_date_format(self):
        """Test Case ID #8

            Test that can get a user information correctly and successful by provide string in date format."""
        url = WEB_URL + "by_date/" + "always_wrong"
        response = requests.get(url)
        self.assertEqual(204, response.status_code)
        self.assertTrue(response.ok)


    def test_provide_wrong_param(self):
        """Test Case ID #9

            Test that can get a user information correctly and successful by provide wrong param after path."""
        url = WEB_URL + "all" + "23-10-2021"
        response = requests.get(url)
        self.assertEqual(404, response.status_code)
        self.assertFalse(response.ok)
        self.assertEqual("Not Found", response.reason)

    def test_verify_JSON_data_type_format(self):
        """Test Case ID #10

            Test that can get JSON object from our API."""
        url = WEB_URL + "all"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual("application/json; charset=utf-8", response.headers["Content-Type"])

