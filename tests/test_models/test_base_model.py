#!/usr/bin/python3
"""
Unit tests for the BaseModel class.
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
from time import sleep

class TestBaseModel(unittest.TestCase):
    """ Tests for the BaseModel class. """

    def setUp(self):
        """ Set up test case environment. """
        self.model = BaseModel()
        self.model2 = BaseModel()

    def test_id_type(self):
        """ Test id type is a string. """
        self.assertIsInstance(self.model.id, str)

    def test_created_at_type(self):
        """ Test created_at type is datetime. """
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_type(self):
        """ Test updated_at type is datetime. """
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_unique_id(self):
        """ Test each BaseModel has a unique id. """
        self.assertNotEqual(self.model.id, self.model2.id)

    def test_time_difference(self):
        """ Test created_at and updated_at are different for different models. """
        sleep(0.01)
        model3 = BaseModel()
        self.assertNotEqual(self.model.created_at, model3.created_at)
        self.assertNotEqual(self.model.updated_at, model3.updated_at)

    def test_save_method(self):
        """ Test save method updates updated_at. """
        original_updated_at = self.model.updated_at
        sleep(0.01)
        self.model.save()
        self.assertNotEqual(original_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """ Test to_dict method returns a dictionary. """
        self.assertIsInstance(self.model.to_dict(), dict)

    def test_to_dict_content(self):
        """ Test to_dict content is correct. """
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

if __name__ == '__main__':
    unittest.main()

