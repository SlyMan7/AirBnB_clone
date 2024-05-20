#!/usr/bin/python3
"""
Unit tests for the City class.
"""

import unittest
from models.city import City
from datetime import datetime
from time import sleep

class TestCity(unittest.TestCase):
    """ Tests for the City class. """

    def setUp(self):
        """ Set up test case environment. """
        self.city = City()
        self.city2 = City()

    def test_id_type(self):
        """ Test id type is a string. """
        self.assertIsInstance(self.city.id, str)

    def test_created_at_type(self):
        """ Test created_at type is datetime. """
        self.assertIsInstance(self.city.created_at, datetime)

    def test_updated_at_type(self):
        """ Test updated_at type is datetime. """
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_unique_id(self):
        """ Test each City has a unique id. """
        self.assertNotEqual(self.city.id, self.city2.id)

    def test_time_difference(self):
        """ Test created_at and updated_at are different for different cities. """
        sleep(0.01)
        city3 = City()
        self.assertNotEqual(self.city.created_at, city3.created_at)
        self.assertNotEqual(self.city.updated_at, city3.updated_at)

    def test_save_method(self):
        """ Test save method updates updated_at. """
        original_updated_at = self.city.updated_at
        sleep(0.01)
        self.city.save()
        self.assertNotEqual(original_updated_at, self.city.updated_at)

    def test_to_dict(self):
        """ Test to_dict method returns a dictionary. """
        self.assertIsInstance(self.city.to_dict(), dict)

    def test_to_dict_content(self):
        """ Test to_dict content is correct. """
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['id'], self.city.id)
        self.assertIn('created_at', city_dict)
        self.assertIn('updated_at', city_dict)

if __name__ == '__main__':
    unittest.main()

