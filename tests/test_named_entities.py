#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_named_entities
----------------------------------

Tests for `named_entities` module.
"""
import os
import unittest

from coast_core import named_entities


@unittest.skip("Work for Python 3.5 but not with pypi3 (on 3.5-5.8) on Travis")
class TestNamedEntities(unittest.TestCase):

    def setUp(self):
        self.link = "https://www.joelonsoftware.com/2006/09/01/language-wars/"
        self.file = open(os.path.dirname(__file__) + "/test_data/language_wars.html")
        self.html = self.file.read()

    def test_extract_all(self):
        result = named_entities.extract_all_named_entities(self.html)
        print(result)

    def tearDown(self):
        self.file.close()
