"""
A collection of function that detect and analyse an article
"""
import json
import sys
import re
import os


def features_detection(word):
    """
    Detect features in a word. Features come from the pattern.json in the resources directory

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
                            "expression": word
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


def extract_text_data(text):
    """
    Extract the data of the text : total of characters, total of words, total of lines

    :param text: The text to operate on
    :return: an object containing th text data
    """
    total_char = 0
    total_words = 0
    total_lines = 0

    lines = text.split('\n')

    for line in lines:
        total_lines += 1
        words = line.split()
        for word in words:
            total_words += 1
            total_char += len(word)
        total_char += len(words) - 1

    return {
        "total_char": total_char,
        "total_words": total_words,
        "total_lines": total_lines
    }


def extract_lines_data(text):
    """
    Extract the lines data from a text.

    :param text: The text to operate on
    :return: A list of lines objects
    """
    line_num = 0
    lines_list = []

    lines = text.split('\n')
    for line in lines:
        line_num += 1
        words = line.split()
        line_words = []
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
            features = features_detection(word)
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

            line_words.append(word_data)
        lines_list.append({
            "line_num": line_num,
            "line_length_by_words": line_length_by_words,
            "line_length_by_char": line_length_by_char,
            "first_word": first_word,
            "last_word": last_word,
            "line_words": line_words
        })

    return lines_list


def extract_features_by_words(text):
    """
    Extract the features from words.

    :param text: The text to operate on
    :return: A list of features objects
    """
    features_by_words = []
    words = text.split()
    word_num = 0
    for word in words:
        word_features = features_detection(word)
        for feature in word_features:
            feature = {
                "type": feature['type'],
                "match_num": feature['match_num'],
                "expression": feature['expression'],
                "word_number": word_num
            }
            features_by_words.append(feature)
        word_num += 1

    return features_by_words


def extract_binary_data(lines_list):
    """
    Extract the binary data from lines.

    :param lines_list: The list of line to operate on returned by the extract_lines_data function.
    :return: An object containing the binary data of the lines.
    """
    binary_lines = ''
    binary_list = []
    binary_words = ''
    for line in lines_list:
        line_words = ''
        for word in line['line_words']:
            word_value = ''
            try:
                if word['features']:
                    word_value = '1'
            except:
                word_value = '0'
            line_words += word_value

        binary_line_value = '0'
        if '1' in line_words:
            binary_line_value = '1'

        binary_list.append(line_words)
        binary_words += line_words
        binary_lines += binary_line_value

    # Percentage by lines
    total = len(binary_lines)
    line_percentage = percentage(binary_lines, total)

    # Percentage by words
    total = len(binary_words)
    word_percentage = percentage(binary_words, total)

    binary_data = {
        "lines": binary_lines,
        "words": binary_words,
        "lines_list": binary_list,
        "line_percentage": line_percentage,
        "word_percentage": word_percentage
    }

    return binary_data


def extract_absolute_data(lines_list):
    """
    Extract the absolute data from lines.

    :param lines_list: The list of line to operate on returned by the extract_lines_data function.
    :return: An object containing the binary data of the lines.
    """
    words = ''

    for line in lines_list:
        for word in line['line_words']:
            word_value = ''

            try:
                if word['features']:
                    word_value = str(len(word['features']))
            except:
                word_value = '0'
            words += word_value

    total = len(words)
    word_percentage = percentage(words, total)
    absolute_data = {
        "words": words,
        "word_percentage": word_percentage
    }

    return absolute_data


def percentage(string, total):
    """
    Calculate the percentage of code in an string.
    :param string: The string to operate on
    :param total: The total depending on what you base your percentage
    :return: The percentage of code in the string
    """
    code_presence = 0
    percentage = 0
    for i in range(0, total):
        if string[i] is not '0' or None:
            code_presence += int(string[i])
    if code_presence is not 0:
        percentage = (code_presence / total) * 100

    return percentage


def execute_code_detection(text, granularity='ALL'):
    """
    Execute all the function of code detection analysis. You can choose what to return.
        * ALL will return all the data we can get. This is the default value.
        * BASIC will return the binary and the absolute data.
        * FEATURES will return the detected features in the text
        * LINES will return the lines data.

    :param text: The text to operate on
    :param granularity: Will affect the returned data : ALL BASIC FEATURES LINES
    :return: The return will depend of the granularity
    """
    text_data = extract_text_data(text)
    lines = extract_lines_data(text)
    binary_classification = extract_binary_data(lines)
    absolute_classification = extract_absolute_data(lines)
    features_by_words = extract_features_by_words(text)

    if granularity is 'ALL':
        return {
            "text_data": text_data,
            "lines": lines,
            "binary_classification": binary_classification,
            "absolute_classification": absolute_classification,
            "features_by_words": features_by_words
        }

    if granularity is 'BASIC':
        return {
            "binary_classification": binary_classification,
            "absolute_classification": absolute_classification
        }
    if granularity is 'FEATURES':
        return features_by_words

    if granularity is 'LINES':
        return lines
