#!/usr/bin/python3
"""
Unit tests for the FileStorage class.
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime
from time import sleep

class TestFileStorage(unittest.TestCase):
    """ Tests for the FileStorage class. """

    def setUp(self):
        """ Set up test case environment. """
        self.storage = FileStorage()
        self.model = BaseModel()

    def test_instantiation(self):
        """ Test instantiation of FileStorage object. """
        self.assertIsInstance(self.storage, FileStorage)

    def test_file_path(self):
        """ Test file path is a string. """
        self.assertIsInstance(self.storage._FileStorage__file_path, str)

    def test_objects(self):
        """ Test objects is a dictionary. """
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all_method(self):
        """ Test all method returns a dictionary. """
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_method(self):
        """ Test new method adds an object. """
        self.storage.new(self.model)
        self.assertIn("BaseModel." + self.model.id, self.storage.all())

    def test_save_method(self):
        """ Test save method saves to file. """
        self.storage.new(self.model)
        self.model.save()
        with open(self.storage._FileStorage__file_path, 'r') as f:
            self.assertIn("BaseModel." + self.model.id, f.read())

    def test_reload_method(self):
        """ Test reload method reloads from file. """
        self.storage.new(self.model)
        self.model.save()
        self.storage.reload()
        self.assertIn("BaseModel." + self.model.id, self.storage.all())

if __name__ == '__main__':
    unittest.main()

