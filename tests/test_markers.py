#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_markers
----------------------------------

Tests for `markers` module.
"""
import os
import unittest

from coast_core import markers


@unittest.skip('Skipped because Travis cannot find files')
class TestMarkers(unittest.TestCase):

    def setUp(self):
        self.link = "https://www.joelonsoftware.com/2006/09/01/language-wars/"
        self.file = open(os.path.dirname(__file__) + "/test_data/language_wars.html")
        self.html = self.file.read()
        self.config_file = os.path.dirname(__file__) + "/test_data/config_file.json"
        self.classification_config_file = os.path.dirname(__file__) + "/../coast_core/resources/example/citations_classification.json"

    def test_run_all_markers(self):
        result = markers.run_all_markers(self.html, self.config_file)
        print(result)

    def tearDown(self):
        self.file.close()

