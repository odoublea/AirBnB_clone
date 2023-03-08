#!/usr/bin/python3
"""Unittest for the Base model class"""


import unittest
from models import base_model
from models.base_model import BaseModel
from uuid import uuid4
from datetime import datetime
from time import sleep
Base = BaseModel


class TestBaseClass(unittest.TestCase):

    """The test suite for Base Model class documentation"""

    def test_documentation(self):
        """Test documentation"""

        self.assertTrue(len(base_model.__doc__) > 0)

    def test_class_doc(self):
        """Test documentation"""

        self.assertTrue(len(Base.__doc__) > 0)


class TestBaseModel(unittest.TestCase):
    """
    The test suite for models.base_model
    """

    def test_if_BaseModel_instance_has_id(self):
        """
        Checks the test suite for models.base_model.BaseModel
        """
        b = BaseModel()
        self.assertTrue(hasattr(b, "id"))  # add assertion here

    def test_str_rep(self):
        """
        Checks if the str rep is appropriate
        """
        b = BaseModel()
        self.assertNotEqual(str(b),
                            "[BaseModel] ({}) {}".format(b.id, b.__dict__))

    def test_ids_unique(self):
        """
        Checks if ids generated are unique
        """
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_type_of_id(self):
        """
        Checks if the id is a str
        """
        b = BaseModel()
        self.assertTrue(type(b.id) is str)

    def test_updated_at(self):
        """
        Checks attribute for `updated_at` is a datetime
        """
        b = BaseModel()
        self.assertTrue(type(b.updated_at) is datetime)

    def test_created_at(self):
        """
        Checks the attribute for `created_at` is a datetime
        """
        b = BaseModel()
        self.assertTrue(type(b.created_at) is datetime)

    def test_two_different_created_at(self):
        """
        Tests for the different created_at attributes
        """
        b1 = BaseModel()
        sleep(0.03)
        b2 = BaseModel()
        sleep(0.03)
        self.assertLess(b1.created_at, b2.created_at)

    def test_args_unused(self):
        """
        Checks that args is not used
        """
        b = BaseModel(None)
        self.assertNotIn(None, b.__dict__.values())

    def test_created_at_eq_updated_at(self):
        """
        Tests the created at for the initialization
        """
        b = BaseModel()
        self.assertEqual(b.created_at, b.updated_at)

    def test_save_function(self):
        """
        Test the save function if it works
        """
        b = BaseModel()
        b.save()
        self.assertNotEqual(b.created_at, b.updated_at)
        self.assertGreater(b.updated_at.microsecond,
                           b.created_at.microsecond)

    def test_dict_function(self):
        """
        Test the BaseModel.to_dict() returns a __dict__
        """
        b = BaseModel()
        self.assertTrue(type(b.to_dict()) is dict)

    def test_if_class_in_dict(self):
        """
        Test the presence of `__class__`
        """
        b = BaseModel()
        self.assertTrue("__class__" in b.to_dict())

    def test_dict_created_at_to_iso(self):
        """
        Test for dict to Iso
        """
        b = BaseModel()
        self.assertEqual(b.to_dict()["created_at"], b.created_at.isoformat())

    def test_dict_updated_at_to_iso(self):
        """
        Test for dict to Iso
        """
        b = BaseModel()
        self.assertEqual(b.to_dict()["updated_at"], b.created_at.isoformat())

    def test_dict_length_is_accurate(self):
        """
        Test the accurate length of the dict
        """
        b = BaseModel()
        p_exp = {k: v for k, v in b.__dict__.items()
                 if not k.startswith("_")}
        self.assertEqual(len(b.to_dict()), len(p_exp) + 1)

    def test_empty_kwargs(self):
        """
        Test for empty kwargs
        """
        my_dict = {}
        b = BaseModel(**my_dict)
        self.assertTrue(type(b.id) is str)
        self.assertTrue(type(b.created_at) is datetime)
        self.assertTrue(type(b.updated_at) is datetime)

    def test_non_empty_kwargs(self):
        """
        Test for non-empty kwargs
        """
        my_dict = {
            "id": uuid4(), "created_at": datetime.utcnow().isoformat(),
            "updated_at": datetime.utcnow().isoformat()
        }
        b = BaseModel(**my_dict)
        self.assertEqual(b.id, my_dict["id"])
        self.assertEqual(b.created_at,
                         datetime.strptime(my_dict["created_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(b.updated_at,
                         datetime.strptime(my_dict["updated_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertTrue(type(b.updated_at) is datetime)

    def test_passing_kwargs(self):
        """
        Tests the args and kwargs
        """
        dt = datetime.now()
        dt_iso = dt.isoformat()
        b = BaseModel("09876", id="467", created_at=dt_iso, name="Daniel")
        self.assertEqual(b.id, "467")
        self.assertEqual(b.created_at, dt)
        self.assertEqual(b.name, "Daniel")

    def test_when_kwargs_passed_is_more_than_default(self):
        """
        Checks BaseModel does not break when kwargs contains more than
        the default attributes
        """
        my_dict = {"id": uuid4(), "created_at": datetime.utcnow().isoformat(),
                   "updated_at": datetime.utcnow().isoformat(),
                   "name": "Firdaus"}
        b = BaseModel(**my_dict)
        self.assertTrue(hasattr(b, "name"))

    def test_that_save_method_updates_updated_at_attr(self):
        """
        Checks that save() method updates 'updated_at' attribute
        """
        b = BaseModel()
        sleep(0.02)
        temp_update = b.updated_at
        b.save()
        self.assertLess(temp_update, b.updated_at)

    def test_that_save_can_update_two_or_more_times(self):
        """
        Tests that the save method updates 'updated_at' two times
        """
        b = BaseModel()
        sleep(0.02)
        temp_update = b.updated_at
        b.save()
        sleep(0.02)
        temp1_update = b.updated_at
        self.assertLess(temp_update, temp1_update)
        sleep(0.01)
        b.save()
        self.assertLess(temp1_update, b.updated_at)

    def test_that_to_dict_contains_correct_keys(self):
        """
        Checks whether to_dict() returns the expected key
        """
        b_dict = BaseModel().to_dict()
        attrs = ("id", "created_at", "updated_at", "__class__")
        for attr in attrs:
            self.assertIn(attr, b_dict)

    def test_to_dict_contains_added_attributes(self):
        """
        Checks that new attributes are also returned by to_dict()
        """
        b = BaseModel()
        attrs = ["id", "created_at", "updated_at", "__class__"]
        b.name = "Firdaus"
        b.email = "firduas@gmail.com"
        attrs.extend(["name", "email"])
        for attr in attrs:
            self.assertIn(attr, b.to_dict())

    def test_to_dict_output(self):
        """
        Checks the output returned by to_dict()
        """
        b = BaseModel()
        dt = datetime.now()
        b.id = "12345"
        b.created_at = b.updated_at = dt
        test_dict = {
            'id': "12345",
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertDictEqual(test_dict, b.to_dict())

    def test_to_dict_with_args(self):
        """
        Checks that TypeError is returned when argument is passed to to_dict()
        """
        b = BaseModel()
        with self.assertRaises(TypeError):
            b.to_dict(None)

    def test_to_dict_not_dunder_dict(self):
        """Checks that to_dict() is a dict object not equal to __dict__"""
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)


if __name__ == '__main__':
    unittest.main()
