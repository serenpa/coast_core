#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_ngrams
----------------------------------

Tests for `ngrams` module.
"""
import os
import unittest

from coast_core import utils
from coast_core import analyse_ngrams


class TestNgrams(unittest.TestCase):

    def setUp(self):
        self.article = "This text is an example to test the ngrams module."
        self.link = "https://www.joelonsoftware.com/2006/09/01/language-wars/"
        self.file = open(os.path.dirname(__file__) + "/test_data/language_wars.html")
        self.html = self.file.read()


    # def test_get_unigrams(self):
    #     print(self.article)
    #     unigrams = utils.get_ngrams(self.article, 1)
    #     expected_result = [('This',), ('text',), ('is',), ('an',),  ('example',),  ('to',),  ('test',),  ('the',),  ('ngrams',),  ('module',),  ('.',)]
    #
    #     print(unigrams)
    #     self.assertEqual(unigrams, expected_result)
    #
    # def test_get_duograms(self):
    #     print(self.article)
    #     duograms = utils.get_ngrams(self.article, 2)
    #     expected_result = [('This', 'text'), ('text', 'is'), ('is', 'an'), ('an', 'example'), ('example', 'to'),
    #                        ('to', 'test'), ('test', 'the'), ('the', 'ngrams'), ('ngrams', 'module'), ('module', '.')]
    #
    #     print(duograms)
    #     self.assertEqual(duograms, expected_result)
    #
    # def test_get_trigrams(self):
    #     print(self.article)
    #     trigrams = utils.get_ngrams(self.article, 3)
    #     expected_result = [('This', 'text', 'is'), ('text', 'is', 'an'), ('is', 'an', 'example'),
    #                        ('an', 'example', 'to'), ('example', 'to', 'test'), ('to', 'test', 'the'),
    #                        ('test', 'the', 'ngrams'), ('the', 'ngrams', 'module'), ('ngrams', 'module', '.')]
    #
    #     print(trigrams)
    #     self.assertEqual(trigrams, expected_result)
    #
    # def test_get_fourgrams(self):
    #     print(self.article)
    #     fourgrams = utils.get_ngrams(self.article, 4)
    #     expected_result = [('This', 'text', 'is', 'an'), ('text', 'is', 'an', 'example'),
    #                        ('is', 'an', 'example', 'to'), ('an', 'example', 'to', 'test'),
    #                        ('example', 'to', 'test', 'the'), ('to', 'test', 'the', 'ngrams'),
    #                        ('test', 'the', 'ngrams', 'module'), ('the', 'ngrams', 'module', '.')]
    #
    #     print(fourgrams)
    #     self.assertEqual(fourgrams, expected_result)
    #
    # def test_get_fivegrams(self):
    #     print(self.article)
    #     fivegrams = utils.get_ngrams(self.article, 5)
    #     expected_result = [('This', 'text', 'is', 'an', 'example'), ('text', 'is', 'an', 'example', 'to'),
    #                        ('is', 'an', 'example', 'to', 'test'), ('an', 'example', 'to', 'test', 'the'),
    #                        ('example', 'to', 'test', 'the', 'ngrams'), ('to', 'test', 'the', 'ngrams', 'module'),
    #                        ('test', 'the', 'ngrams', 'module', '.')]
    #
    #     print(fivegrams)
    #     self.assertEqual(fivegrams, expected_result)
    #
    # def test_get_sixgrams(self):
    #     print(self.article)
    #     sixgrams = utils.get_ngrams(self.article, 6)
    #     expected_result = [('This', 'text', 'is', 'an', 'example', 'to'),
    #                        ('text', 'is', 'an', 'example', 'to', 'test'),
    #                        ('is', 'an', 'example', 'to', 'test', 'the'),
    #                        ('an', 'example', 'to', 'test', 'the', 'ngrams'),
    #                        ('example', 'to', 'test', 'the', 'ngrams', 'module'),
    #                        ('to', 'test', 'the', 'ngrams', 'module', '.')]
    #
    #     print(sixgrams)
    #     self.assertEqual(sixgrams, expected_result)

    def test_generate_ngrams(self):
        result = analyse_ngrams.generate_ngrams(self.html)
        print(result)
