"""Test cases for bubble_sort.py
"""

from unittest import TestCase
from .bubble_sort import bubble_sort
from __generators.array_generator import generate_array

class TestBubbleSort(TestCase):
    """Test cases for bubble_sort function"""

    def test_bubble_sort(self):
        """It should sort the elements of an array from lowest to highest."""
        arr = [8, 2, 15, 6, 0]
        self.assertEqual (bubble_sort(arr), [0, 2, 6, 8, 15])
        arr = [8, 2, 15, 6, 0]
        self.assertEqual (bubble_sort(arr), sorted(arr))
        arr = generate_array(100)
        self.assertEqual (bubble_sort(arr), sorted(arr))
        arr = generate_array(999)
        self.assertEqual (bubble_sort(arr), sorted(arr))
        