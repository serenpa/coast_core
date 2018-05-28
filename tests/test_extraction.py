#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_extraction
----------------------------------

Tests for `extraction` module.
"""
import os
import unittest

from coast_core import extraction


class TestExtraction(unittest.TestCase):

    def setUp(self):
        self.link = "https://www.joelonsoftware.com/2006/09/01/language-wars/"
        self.file = open(os.path.dirname(__file__) + "/test_data/language_wars.html")
        self.html = self.file.read()
        self.classification_config_file = os.path.dirname(__file__) + "/../coast_core/resources/example/citations_classification.json"

    def test_run_all_extraction(self):
        result = extraction.full_extraction(self.link)
        print(result)

    def tearDown(self):
        self.file.close()
