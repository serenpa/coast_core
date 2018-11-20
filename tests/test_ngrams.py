#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_ngrams
----------------------------------

Tests for `ngrams` module.
"""
import os
import unittest

from coast_core import ngram_extraction


@unittest.skip("Not implemented yet")
class TestNgrams(unittest.TestCase):

    def setUp(self):
        self.article = "This text is an example to test the ngrams module."
        self.link = "https://www.joelonsoftware.com/2006/09/01/language-wars/"
        self.file = open(os.path.dirname(__file__) + "/test_data/language_wars.html")
        self.html = self.file.read()
