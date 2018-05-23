"""
    Title:

    Author:

    Description:
"""

from coast_core.code_detection import code_detection


def feature_detection(word):
    return code_detection.feature_detection(word)


def extract_features_from_text(text, print_results=False):
    return code_detection.extract_features_from_text(text, print_results)


def binary_transformation(text_data, print_results):
    return code_detection.binary_transformation(text_data, print_results)


def absolute_transformation(text_data, print_results):
    return code_detection.absolute_transformation(text_data, print_results)


def binary_code_percentage(binary_lines):
    return code_detection.binary_code_percentage(binary_lines)


def absolute_code_percentage(absolute_lines):
    return code_detection.absolute_code_percentage(absolute_lines)


def run_all_detection(text, print_results):
    return code_detection.run_all_detection(text, print_results)
