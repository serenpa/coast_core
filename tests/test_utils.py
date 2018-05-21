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


class TestUtils(unittest.TestCase):

    def test_get_from_file(self):
        result = utils.get_from_file("test_data/language_wars.html")
        print("Full text", result)

    def test_get_json_from_file(self):
        result = utils.get_json_from_file("test_data/config_file.json")
        print("\nJson", result)
