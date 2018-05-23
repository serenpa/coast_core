"""
    Title:

    Author:

    Description:
"""
import unittest

from coast_core import extraction, code_detection


class TestCodeDetection(unittest.TestCase):

    def setUp(self):
        self.text = """Here is a false text. Let's try the code detection module.
        The setUp function initialize variables:
        def setUp(self):
            self.my_var = 200
            """

    def test_run_code_detection(self):
        code_detection.run_all_detection(self.text, False)
