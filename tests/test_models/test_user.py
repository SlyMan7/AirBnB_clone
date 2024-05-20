#!/usr/bin/python3
"""
Unit tests for the User class.
"""

import unittest
from models.user import User
from datetime import datetime
from time import sleep

class TestUser(unittest.TestCase):
    """ Tests for the User class. """

    def setUp(self):
        """ Set up test case environment. """
        self.user = User()
        self.user2 = User()

    def test_id_type(self):
        """ Test id type is a string. """
        self.assertIsInstance(self.user.id, str)

    def test_created_at_type(self):
        """ Test created_at type is datetime. """
        self.assertIsInstance(self.user.created_at, datetime)

    def test_updated_at_type(self):
        """ Test updated_at type is datetime. """
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_unique_id(self):
        """ Test each User has a unique id. """
        self.assertNotEqual(self.user.id, self.user2.id)

    def test_time_difference(self):
        """ Test created_at and updated_at are different for different users. """
        sleep(0.01)
        user3 = User()
        self.assertNotEqual(self.user.created_at, user3.created_at)
        self.assertNotEqual(self.user.updated_at, user3.updated_at)

    def test_save_method(self):
        """ Test save method updates updated_at. """
        original_updated_at = self.user.updated_at
        sleep(0.01)
        self.user.save()
        self.assertNotEqual(original_updated_at, self.user.updated_at)

    def test_to_dict(self):
        """ Test to_dict method returns a dictionary. """
        self.assertIsInstance(self.user.to_dict(), dict)

    def test_to_dict_content(self):
        """ Test to_dict content is correct. """
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['id'], self.user.id)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)

if __name__ == '__main__':
    unittest.main()

