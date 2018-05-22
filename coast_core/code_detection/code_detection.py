"""
    Title: code_detection

    Author: Yann Le Norment

    Description: Find code in articles
"""
import json
import sys
import re


def feature_detection(word):
    features = []
    match_num = 0

    try:
        with open("patterns.json") as patterns:
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
        with open("keywords.txt") as keywords_file:
            lines = keywords_file.readlines()
            for keyword in lines:
                keyword = keyword.rstrip()
                keyword_rules = "(^| )" + keyword + "( |\(|\{|:|$)"
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


def extract_features_from_article(article):

    article_data = []

    total_char = 0
    total_words = 0
    total_lines = 0

    lines_data = []
    lines = article.split('\n')
    line_num = 0

    for line in lines:

        words_data = []
        words = line.split()

        line_length_by_words = len(words)
        line_length_by_char = sum(len(word) for word in words)

        position = 0
        for word in words:

            word_data = []
            position += 1
            features = feature_detection(word)
            if features:
                word_data.append({
                    "word": word,
                    "position": position,
                    "features": features
                })
            if not features:
                word_data.append({
                    "word": word,
                    "position": position
                })
            words_data.append(word_data)
        total_words = position

        try:
            first_word = words_data[0]
            first_char = list(first_word)[0]
            last_word = words_data[line_length_by_words - 1]
            last_char = list(last_word)[len(last_word) - 1]

            lines_data.append({
                "line_num": line_num,
                "line_length_by_words": line_length_by_words,
                "line_length_by_char": line_length_by_char,
                "first_word": first_word,
                "first_char": first_char,
                "last_word": last_word,
                "last_char": last_char,
                "words": words_data
            })
        except Exception as e:
            first_word = str(e)
            first_char = str(e)
            last_word = str(e)
            last_char = str(e)

            lines_data.append({
                "line_num": line_num,
                "line_length_by_words": line_length_by_words,
                "line_length_by_char": line_length_by_char,
                "first_word": first_word,
                "first_char": first_char,
                "last_word": last_word,
                "last_char": last_char,
                "words_data": words_data
            })

    article_data.append({
        "total_char": total_char,
        "total_lines": total_lines,
        "total_words": total_words,
        "lines_data": lines_data
    })

    return article_data


def binary_transformation(article_data):

    lines_data = article_data['lines_data']

    binary_article = ''
    binary_lines = []

    for line in lines_data:

        binary_line = ''

        for words_data in line['words_data']:
            for word in words_data:

                # Default word value
                word_value = '0'

                if word['features']:
                    word_value = '1'

                binary_line += word_value

        # Default line value
        binary_line_value = '0'

        if '1' in binary_line:
            binary_line_value = '1'
        # Updating the list of lines in the article
        binary_lines.append(binary_line_value)
        # Updating the string which represent the article
        binary_article += binary_line_value

    return binary_article, binary_lines


def absolute_transformation(article_data):

    lines_data = article_data['lines_data']

    absolute_article = ''
    absolute_lines = []

    for line in lines_data:

        absolute_line = ''

        for words_data in line['words_data']:
            for word in words_data:

                # Default word value
                word_value = '0'
                if word['features']:
                    word_value = str(len(word['features']))

                absolute_line += word_value
        # Default line value
        absolute_line_value = '0'

        for num in absolute_line:
            if num is not '0':
                absolute_line_value += int(num)
        # Updating the list of lines in the article
        absolute_lines.append(absolute_line_value)
        # Updating the string which represent the article
        absolute_article += absolute_line_value

    return absolute_article, absolute_lines


def binary_code_percentage(binary_lines):

    code_presence = 0
    words_nb = 0
    percentage = None

    for line in binary_lines:
        words_nb = len(line)
        for i in range(0, words_nb):
            if '0' in line:
                pass
            if '1' in line:
                code_presence += 1

    if words_nb is not '0':
        percentage = (code_presence / words_nb) * 100

    return percentage

