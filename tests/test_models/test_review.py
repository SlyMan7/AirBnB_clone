#!/usr/bin/python3
"""
Unit tests for the Review class.
"""

import unittest
from models.review import Review
from datetime import datetime
from time import sleep

class TestReview(unittest.TestCase):
    """ Tests for the Review class. """

    def setUp(self):
        """ Set up test case environment. """
        self.review = Review()
        self.review2 = Review()

    def test_id_type(self):
        """ Test id type is a string. """
        self.assertIsInstance(self.review.id, str)

    def test_created_at_type(self):
        """ Test created_at type is datetime. """
        self.assertIsInstance(self.review.created_at, datetime)

    def test_updated_at_type(self):
        """ Test updated_at type is datetime. """
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_unique_id(self):
        """ Test each Review has a unique id. """
        self.assertNotEqual(self.review.id, self.review2.id)

    def test_time_difference(self):
        """ Test created_at and updated_at are different for different reviews. """
        sleep(0.01)
        review3 = Review()
        self.assertNotEqual(self.review.created_at, review3.created_at)
        self.assertNotEqual(self.review.updated_at, review3.updated_at)

    def test_save_method(self):
        """ Test save method updates updated_at. """
        original_updated_at = self.review.updated_at
        sleep(0.01)
        self.review.save()
        self.assertNotEqual(original_updated_at, self.review.updated_at)

    def test_to_dict(self):
        """ Test to_dict method returns a dictionary. """
        self.assertIsInstance(self.review.to_dict(), dict)

    def test_to_dict_content(self):
        """ Test to_dict content is correct. """
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['id'], self.review.id)
        self.assertIn('created_at', review_dict)
        self.assertIn('updated_at', review_dict)

if __name__ == '__main__':
    unittest.main()

