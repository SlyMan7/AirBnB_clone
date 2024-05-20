#!/usr/bin/python3
"""
Unit tests for the Amenity class.
"""

import unittest
from models.amenity import Amenity
from datetime import datetime
from time import sleep

class TestAmenity(unittest.TestCase):
    """ Tests for the Amenity class. """

    def setUp(self):
        """ Set up test case environment. """
        self.amenity = Amenity()
        self.amenity2 = Amenity()

    def test_id_type(self):
        """ Test id type is a string. """
        self.assertIsInstance(self.amenity.id, str)

    def test_created_at_type(self):
        """ Test created_at type is datetime. """
        self.assertIsInstance(self.amenity.created_at, datetime)

    def test_updated_at_type(self):
        """ Test updated_at type is datetime. """
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_unique_id(self):
        """ Test each Amenity has a unique id. """
        self.assertNotEqual(self.amenity.id, self.amenity2.id)

    def test_time_difference(self):
        """ Test created_at and updated_at are different for different amenities. """
        sleep(0.01)
        amenity3 = Amenity()
        self.assertNotEqual(self.amenity.created_at, amenity3.created_at)
        self.assertNotEqual(self.amenity.updated_at, amenity3.updated_at)

    def test_save_method(self):
        """ Test save method updates updated_at. """
        original_updated_at = self.amenity.updated_at
        sleep(0.01)
        self.amenity.save()
        self.assertNotEqual(original_updated_at, self.amenity.updated_at)

    def test_to_dict(self):
        """ Test to_dict method returns a dictionary. """
        self.assertIsInstance(self.amenity.to_dict(), dict)

    def test_to_dict_content(self):
        """ Test to_dict content is correct. """
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['id'], self.amenity.id)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)

if __name__ == '__main__':
    unittest.main()

