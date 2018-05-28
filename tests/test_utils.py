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


class TestFileUtils(unittest.TestCase):

    def setUp(self):
        self.file = os.path.dirname(__file__) + "/test_data/language_wars.html"
        self.config_file = os.path.dirname(__file__) + "/../coast_core/resources/example/config_file.json"

    def test_get_from_file(self):
        result = utils.get_from_file(self.file)
        print("Full text", result)

    def test_get_json_from_file(self):
        result = utils.get_json_from_file(self.config_file)
        print("\nJson", result)
