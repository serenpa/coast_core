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
        self.all_uris = ['https://www.joelonsoftware.com/2006/09/01/language-wars/',
                         'https://www.joelonsoftware.com/author/joelonsoftware/',
                         'https://www.joelonsoftware.com/category/news/',
                         'https://www.joelonsoftware.com/articles/lordpalmerston.html',
                         'http://www.projectaardvark.com/',
                         'https://www.copilot.com/',
                         'http://www.squeak.org/',
                         'http://www.findinglisp.com/blog/2005/12/reddit-and-lisp-psychosis.html',
                         'http://www.cabochon.com/~stevey/blog-rants/more-ocaml.html',
                         'https://www.joelonsoftware.com/articles/unicode.html',
                         'http://www.paulgraham.com/avg.html',
                         'http://www.reddit.com/',
                         'http://www.fogcreek.com/fogbugz']

    def test_get_article_domain(self):
        article_domain = citations.get_an_articles_domain(self.link)
        expected_domain = "www.joelonsoftware.com"

        self.assertEqual(article_domain, expected_domain)

    def test_get_all_citations(self):
        actual_all_citations = citations.get_all_citations(self.html)
        self.assertEqual(actual_all_citations, self.all_uris)

    def test_external_citations(self):
        actual_external_citations = citations.select_external_citations(self.link, self.all_uris)
        expected_external_citations = ['http://www.projectaardvark.com/',
                           'https://www.copilot.com/',
                           'http://www.squeak.org/',
                           'http://www.findinglisp.com/blog/2005/12/reddit-and-lisp-psychosis.html',
                           'http://www.cabochon.com/~stevey/blog-rants/more-ocaml.html',
                           'http://www.paulgraham.com/avg.html',
                           'http://www.reddit.com/',
                           'http://www.fogcreek.com/fogbugz']
        self.assertEqual(actual_external_citations, expected_external_citations)

    def tearDown(self):
        self.file.close()
