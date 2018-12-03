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
        self.file.close()

    def test_ngram_frequency(self):
        article = "i i i am"
        frequency_count = ngram_extraction.calculate_ngram_frequency_count(article, 1, [])
        sorted_frequencies = sorted(frequency_count["frequency_count"], key=lambda args: args[1])

        expected_count = [(('am',), 1), (('i',), 3)]
        self.assertEqual(expected_count, sorted_frequencies)

    def test_ngram_frequency_with_stop_words(self):
        stop_words = ["I"]
        article = "I I I am well"
        frequency_count = ngram_extraction.calculate_ngram_frequency_count(article, 2, stop_words)
        sorted_frequencies = sorted(frequency_count["frequency_count"], key=lambda args: args[1])

        expected_count = [(('am', 'well',), 1)]
        self.assertEqual(expected_count, sorted_frequencies)

    def test_ngram_frequency_is_not_case_sensitive(self):
        stop_words = ["b"]
        article = "I i am well, b"
        frequency_count = ngram_extraction.calculate_ngram_frequency_count(article, 2, stop_words)
        sorted_frequencies = sorted(frequency_count["frequency_count"], key=lambda args: args[1])

        expected_count = [(('i', 'i'), 1), (('i', 'am'), 1), (('am', 'well'), 1)]
        self.assertEqual(sorted_frequencies, expected_count)

    def test_ngram_freq_removes_punctuation(self):
        stop_words = []
        article = "lots, of, commas!"

        frequency_count = ngram_extraction.calculate_ngram_frequency_count(article, 2, stop_words)
        sorted_frequencies = sorted(frequency_count["frequency_count"], key=lambda args: args[1])

        expected_count = [(('lots', 'of'), 1), (('of', 'commas'), 1)]
        self.assertEqual(sorted_frequencies, expected_count)
