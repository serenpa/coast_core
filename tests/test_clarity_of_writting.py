#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_clarity_of_writing
----------------------------------

Tests for `clarity_of_writing` module.
"""
import os
import unittest

from coast_core import clarity_of_writing


class TestClarityWriting(unittest.TestCase):

    def setUp(self):
        self.link = "https://www.joelonsoftware.com/2006/09/01/language-wars/"
        self.file = open(os.path.dirname(__file__) + "/test_data/language_wars.html")
        self.html = self.file.read()

    def test_execute(self):
        result = clarity_of_writing.execute_clarity_of_writing_check(self.html)
        # expected_result = {'grammar': {'grammar_issues': [], 'sentences': [], 'total_grammar_issues': -1},
        #                    'language': 'en',
        #                    'readability': {'automated_readability_index': 17.1,
        #                                    'coleman_liau_index': 17.29,
        #                                    'dale_chall_readability_score': 7.88,
        #                                    'flesch_kincaid_grade': 10.3,
        #                                    'flesch_reading_ease': 58.72,
        #                                    'gunning_fog': 18.495593220338986,
        #                                    'linsear_write_formula': 7.642857142857142,
        #                                    'overall_consensus_grade': '7th and 8th grade',
        #                                    'sentence_count': 62,
        #                                    'smog_index': 11.9,
        #                                    'syllable_count': 1973,
        #                                    'word_count': 1298},
        #                    'sentiment': {'polarity': 0.13284393625697974,
        #                                  'subjectivity': 0.5022550348202524}}
        print(result)
        # self.assertEqual(result, expected_result)

    def tearDown(self):
        self.file.close()
