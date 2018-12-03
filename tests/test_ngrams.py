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


class TestNgrams(unittest.TestCase):

    def setUp(self):
        self.article = "This text is an example to test the ngrams module."
        self.link = "https://www.joelonsoftware.com/2006/09/01/language-wars/"
        self.file = open(os.path.dirname(__file__) + "/test_data/language_wars.html")
        self.html = self.file.read()

    def test_ngram_frequency(self):
        article = "I I I AM "
        frequency_count = ngram_extraction.calculate_ngram_frequency_count(article, 1)
        sorted_frequencies = sorted(frequency_count["frequency_count"], key=lambda args: args[1])

        expected_count = [(('AM',), 1), (('I',), 3)]
        self.assertEqual(expected_count, sorted_frequencies)
