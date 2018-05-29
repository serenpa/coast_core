"""
A collection of function that detect and analyse an article
"""
import json
import sys
import re
import os


def feature_detection(word):
    """
    This function will detect features in a word.

    :param word: the word to operate on.
    :return: the list of features of a word.
    """
    features = []
    match_num = 0

    try:
        with open(os.path.dirname(__file__) + "/resources/data/patterns.json") as patterns:
            features_file = json.load(patterns)
            for type, pattern in features_file.items():
                matches = re.finditer(pattern, word)
                if matches:
                    for num, match in enumerate(matches):
                        match_num += 1
                        features.append({
                            "type": type,
                            "match_num": match_num,
                            "expression": match.group()
                        })
    except Exception as e:
        print("\nError: ")
        sys.stdout.write(str(e))

    # Keywords
    try:
        with open(os.path.dirname(__file__) + "/resources/data/keywords.txt") as keywords_file:
            lines = keywords_file.readlines()
            for keyword in lines:
                keyword = keyword.rstrip()
                keyword_rules = "(^|\s)" + keyword + "(\s|\(|\{|:|$)"
                if re.search(keyword_rules, word):
                    match_num += 1
                    features.append(({
                        "type": "KEYWORD",
                        "match_num": match_num,
                        "expression": word
                    }))
    except Exception as e:
        sys.stdout.write(str(e))
        print('\n')

    return features


def extract_features_from_text(text):
    """
    This is the main function of the code detection module. It will split the text by lines and words for analyse.

    :param text: the text to operate on.
    :return: An object containing the number of characters in the text, the number of lines, the number of words and the data of all lines.
    """
    total_char = 0
    total_words = 0
    total_lines = 0

    lines_data = []
    lines = text.split('\n')

    for line in lines:

        total_lines += 1
        words_data = []
        words = line.split()

        line_length_by_words = len(words)
        line_length_by_char = sum(len(word) for word in words)

        try:
            first_word = words[0]
            last_word = words[line_length_by_words - 1]
        except:
            first_word = 'Line is empty'
            last_word = ''

        position = 0
        for word in words:
            word_data = None
            position += 1
            total_char += len(word) + 1
            features = feature_detection(word)
            if features:
                word_data = {
                    "word": word,
                    "position": position,
                    "features": features
                }
            if not features:
                word_data = {
                    "word": word,
                    "position": position
                }

            words_data.append(word_data)
        total_words += position

        lines_data.append({
            "line_num": total_lines,
            "line_length_by_words": line_length_by_words,
            "line_length_by_char": line_length_by_char,
            "first_word": first_word,
            "last_word": last_word,
            "words_data": words_data
        })

    return {
        'total_char': total_char,
        'total_lines': total_lines,
        'total_words': total_words,
        'lines_data': lines_data
    }


def binary_transformation(text_data):
    """
    This function will transform the text into 0 and 1. 0 if there is no code in a line else 1.

    :param text_data: The text data from the extraction of features.
    :return: the text transformed and a list of lines containing the value of each word (0 or 1).
    """
    binary_text = ''
    binary_lines = []

    for line in text_data['lines_data']:
        binary_line = ''
        for word in line['words_data']:

            # Default word value
            word_value = ''
            try:
                if word['features']:
                    word_value = '1'
            except:
                word_value = '0'
            binary_line += word_value
        # Default binary line value
        binary_line_value = '0'
        if '1' in binary_line:
            binary_line_value = '1'
        # Updating the list of lines in the text
        binary_lines.append(binary_line)
        # Updating the string which represent the text
        binary_text += binary_line_value

    return binary_text, binary_lines


def absolute_transformation(text_data):
    """
    This function will transform the text into the number of code detected in a line.

    :param text_data: the text data from the extraction feature.
    :return: a list of lines containing the value of each word, depending of the number of features detected.
    """
    absolute_lines = []

    for line in text_data['lines_data']:
        absolute_line = ''
        absolute_line_value = 0
        for word in line['words_data']:

            # Default word value
            word_value = ''

            try:
                if word['features']:
                    word_value = str(len(word['features']))
            except:
                word_value = '0'
            absolute_line += word_value
            absolute_line_value += int(word_value)
        absolute_lines.append(absolute_line)

    return absolute_lines


def binary_code_percentage(binary_lines):
    """
    Will return the percentage of code in the binary lines by detecting 1.

    :param binary_lines: The article's lines transformed by the binary transformation.
    :return: the binary percentage of code in the text.
    """
    code_presence = 0
    words_nb = 0

    for line in binary_lines:
        words_nb += len(line)
        for i in range(0, len(line)):
            if '0' in line:
                pass
            if '1' in line:
                code_presence += 1

    percentage = (code_presence / words_nb) * 100
    return percentage


def absolute_code_percentage(absolute_lines):
    """
    Will return the percentage of code in the binary lines by detecting anything else than 0 or None.

    :param absolute_lines: The article's lines transformed by the absolute transformation.
    :return: the absolute percentage of code in the text.
    """
    code_presence = 0
    words_nb = 0
    percentage = None

    for line in absolute_lines:
        words_nb += len(line)
        for i, char in enumerate(line):
            if char is not '0' and not None:
                code_presence += int(char)
    if words_nb is not 0:
        percentage = (code_presence / words_nb) * 100
    return percentage


def execute_all_code_detection(text):
    """
    Launch all the detection analysis.

    :param text: the text to operate on.
    :return: An object which contain all the data of the code detection
    """
    text_data = extract_features_from_text(text)

    binary_data = binary_transformation(text_data)
    absolute_lines = absolute_transformation(text_data)

    binary_percentage = binary_code_percentage(binary_data[1])
    absolute_percentage = absolute_code_percentage(absolute_lines)

    return {
        "text_data": text_data,
        "binary_data": binary_data,
        "absolute_data": absolute_lines,
        "binary_percentage": binary_percentage,
        "absolute_percentage": absolute_percentage
    }
