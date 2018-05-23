"""
    Title:

    Author:

    Description:
"""
import unittest

from coast_core import extraction, code_detection


class TestCodeDetection(unittest.TestCase):

    def setUp(self):
        link = "https://www.joelonsoftware.com/2006/09/01/language-wars/"
        article = extraction.pattern_article_extraction(link)
        self.text = article['article_text']

    def test_run_code_detection(self):
        code_detection.run_all_detection(self.text, False)
