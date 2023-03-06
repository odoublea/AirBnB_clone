#!/usr/bin/python3
"""Unittest for the Base class file"""


import unittest
from models import base_model
from models.base_model import BaseModel
Base = BaseModel


class TestBaseClass(unittest.TestCase):

    """Class for unittest of Base class"""

    def test_documentation(self):
        """Test documentation"""

        self.assertTrue(len(base_model.__doc__) > 0)

    def test_class_doc(self):
        """Test documentation"""

        self.assertTrue(len(Base.__doc__) > 0)

if __name__ == '__main__':
    unittest.main()
