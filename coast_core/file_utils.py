"""
A collection of generic utility functions that are used throughout coast_core by various modules relating to reading and writing to files.
"""
import sys
import json


def get_from_file(filename):
    """
    Reads a file and returns each line as a list of strings.
    Notes:

    1. All double quotes are replaced with single quotes.
    2. New line characters are removed.

    :param filename: The path to the file you wish to read.
    :return: A list of strings, where each string is a line in the file.
    """
    ifile = open(filename)
    lines = ifile.readlines()
    ifile.close()

    res = []
    for line in lines:
        res.append(line.replace('"', "'").replace('\n', ''))

    return res


def get_json_from_file(filename):
    """
    Reads a JSON file and returns as an object.
    :param filename: The path to the JSON file you wish to read.
    :return: A JSON object, generated from the contents of the file.
    :return: In the event of an error, the error is printed to the stdout.
    """
    try:
        with open(filename) as ifile:
            res = json.load(ifile)
            return res
    except Exception as e:
        sys.stdout.write(str(e))
