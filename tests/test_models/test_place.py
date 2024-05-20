#!/usr/bin/python3
"""
Unit tests for the Place class.
"""

import unittest
from models.place import Place
from datetime import datetime
from time import sleep

class TestPlace(unittest.TestCase):
    """ Tests for the Place class. """

    def setUp(self):
        """ Set up test case environment. """
        self.place = Place()
        self.place2 = Place()

    def test_id_type(self):
        """ Test id type is a string. """
        self.assertIsInstance(self.place.id, str)

    def test_created_at_type(self):
        """ Test created_at type is datetime. """
        self.assertIsInstance(self.place.created_at, datetime)

    def test_updated_at_type(self):
        """ Test updated_at type is datetime. """
        self.assertIsInstance(self.place.updated_at, datetime)

    def test_unique_id(self):
        """ Test each Place has a unique id. """
        self.assertNotEqual(self.place.id, self.place2.id)

    def test_time_difference(self):
        """ Test created_at and updated_at are different for different places. """
        sleep(0.01)
        place3 = Place()
        self.assertNotEqual(self.place.created_at, place3.created_at)
        self.assertNotEqual(self.place.updated_at, place3.updated_at)

    def test_save_method(self):
        """ Test save method updates updated_at. """
        original_updated_at = self.place.updated_at
        sleep(0.01)
        self.place.save()
        self.assertNotEqual(original_updated_at, self.place.updated_at)

    def test_to_dict(self):
        """ Test to_dict method returns a dictionary. """
        self.assertIsInstance(self.place.to_dict(), dict)

    def test_to_dict_content(self):
        """ Test to_dict content is correct. """
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['id'], self.place.id)
        self.assertIn('created_at', place_dict)
        self.assertIn('updated_at', place_dict)

if __name__ == '__main__':
    unittest.main()

