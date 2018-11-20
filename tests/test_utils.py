#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_coast
----------------------------------

Tests for `coast` module.
"""
import os
import unittest

from coast_core import utils


@unittest.skip("Not implemented yet")
class TestFileUtils(unittest.TestCase):

    def setUp(self):
        self.file = os.path.dirname(__file__) + "/test_data/language_wars.html"
        self.config_file = os.path.dirname(__file__) + "/../coast_core/resources/example/config_file.json"
