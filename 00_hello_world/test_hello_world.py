from unittest import TestCase
import io
import sys


class TestHelloWord(TestCase):
    
    def test_prin_hello_world(self):
        capturedOutput = io.StringIO()                                      # Create StringIO.
        sys.stdout = capturedOutput                                         # Redirect stdout.
        with open("hello_world.py") as f:                                   # Run python code.
            exec(f.read())
        sys.stdout = sys.__stdout__                                         # Reset redirect.
        self.assertEqual('Hello World!\n', capturedOutput.getvalue())       # Assert.
