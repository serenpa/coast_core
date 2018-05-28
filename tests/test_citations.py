#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_citations
----------------------------------

Tests for `citations` module.
"""
import os
import unittest

from coast_core import citations


class TestCitations(unittest.TestCase):

    def setUp(self):
        self.link = "https://www.joelonsoftware.com/2006/09/01/language-wars/"
        self.file = open(os.path.dirname(__file__) + "/test_data/language_wars.html")
        self.html = self.file.read()
        self.classification_config_file = os.path.dirname(__file__) + "/test_data/citations_classification.json"
        self.all_uris = ['https://www.joelonsoftware.com/2006/09/01/language-wars/',
                         'https://www.joelonsoftware.com/author/joelonsoftware/',
                         'https://www.joelonsoftware.com/category/news/',
                         'https://www.joelonsoftware.com/articles/LordPalmerston.html',
                         'http://www.projectaardvark.com/', 'https://www.copilot.com/', 'http://www.squeak.org/',
                         'http://www.findinglisp.com/blog/2005/12/reddit-and-lisp-psychosis.html',
                         'http://www.cabochon.com/~stevey/blog-rants/more-ocaml.html',
                         'https://www.joelonsoftware.com/articles/Unicode.html',
                         'http://www.paulgraham.com/avg.html', 'http://www.reddit.com/',
                         'http://www.fogcreek.com/FogBugz',
                         '/test', '#hello']

    def test_get_article_domain(self):
        result = citations.get_an_articles_domain(self.link)
        expected_result = "www.joelonsoftware.com"

        self.assertEqual(result, expected_result)

    def test_get_all_citations(self):
        result = citations.get_all_citations(self.html)
        print(result)

    def test_external_citations(self):
        result = citations.select_external_citations(self.link, self.all_uris)
        print(result)
        # expected_result = ['http://www.projectaardvark.com/', 'https://www.copilot.com/', 'http://www.squeak.org/',
        #                    'http://www.findinglisp.com/blog/2005/12/reddit-and-lisp-psychosis.html',
        #                    'http://www.cabochon.com/~stevey/blog-rants/more-ocaml.html',
        #                    'http://www.paulgraham.com/avg.html', 'http://www.reddit.com/',
        #                    'http://www.fogcreek.com/FogBugz']
        # self.assertEqual(result, expected_result)

    def tearDown(self):
        self.file.close()
