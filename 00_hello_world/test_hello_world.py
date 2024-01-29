"""Test cases for hello_world.py
"""

from unittest import TestCase
import io
import sys
import hello_world

class TestHelloWolrd(TestCase):
    """TestCase Class for hello_world.py
    """
    def test_prin_hello_world(self):
        """It should print 'Hello World!'"""
        captured_output = io.StringIO()                                      # Create StringIO.
        sys.stdout = captured_output                                         # Redirect stdout.
        hello_world.print_msg()                                              # Print message.
        sys.stdout = sys.__stdout__                                          # Reset redirect.
        self.assertEqual('Hello World!\n', captured_output.getvalue())       # Assert.
