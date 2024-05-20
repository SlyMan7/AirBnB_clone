#!/usr/bin/python3
"""
Unit tests for the State class.
"""

import unittest
from models.state import State
from datetime import datetime
from time import sleep

class TestState(unittest.TestCase):
    """ Tests for the State class. """

    def setUp(self):
        """ Set up test case environment. """
        self.state = State()
        self.state2 = State()

    def test_id_type(self):
        """ Test id type is a string. """
        self.assertIsInstance(self.state.id, str)

    def test_created_at_type(self):
        """ Test created_at type is datetime. """
        self.assertIsInstance(self.state.created_at, datetime)

    def test_updated_at_type(self):
        """ Test updated_at type is datetime. """
        self.assertIsInstance(self.state.updated_at, datetime)

    def test_unique_id(self):
        """ Test each State has a unique id. """
        self.assertNotEqual(self.state.id, self.state2.id)

    def test_time_difference(self):
        """ Test created_at and updated_at are different for different states. """
        sleep(0.01)
        state3 = State()
        self.assertNotEqual(self.state.created_at, state3.created_at)
        self.assertNotEqual(self.state.updated_at, state3.updated_at)

    def test_save_method(self):
        """ Test save method updates updated_at. """
        original_updated_at = self.state.updated_at
        sleep(0.01)
        self.state.save()
        self.assertNotEqual(original_updated_at, self.state.updated_at)

    def test_to_dict(self):
        """ Test to_dict method returns a dictionary. """
        self.assertIsInstance(self.state.to_dict(), dict)

    def test_to_dict_content(self):
        """ Test to_dict content is correct. """
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['id'], self.state.id)
        self.assertIn('created_at', state_dict)
        self.assertIn('updated_at', state_dict)

if __name__ == '__main__':
    unittest.main()

