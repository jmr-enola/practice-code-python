"""Test cases for generator.py
"""

from unittest import TestCase
from .array_generator import generate_array

class TestGenerateArray(TestCase):
    """Test cases for generate_array function"""

    def test_generate_array(self):
        """It should generate an array of integer with correct size."""
        arr = generate_array(5)
        self.assertEqual(len(arr), 5)
        arr = generate_array(1000)
        self.assertEqual(len(arr), 1000)
        arr = generate_array(9999999)
        self.assertEqual(len(arr), 9999999)

    def test_generate_array_type(self):
        """It should raise a TypeError when the size input is not of int data type"""
        self.assertRaises(TypeError, generate_array, "aaa")
        self.assertRaises(TypeError, generate_array, 2.4)

    def test_generate_array_value(self):
        """It should raise a ValueError when the size input is less than or equal to zero"""
        self.assertRaises(ValueError, generate_array, -1)
        self.assertRaises(ValueError, generate_array, -100)