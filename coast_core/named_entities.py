"""
Title: named_entities.py

Author: Ashley Williams

Description: Extract named entities from text.

This module is called by init, so there is no need to import this module
specifically.
"""
import os

import nltk
from nltk.tag import StanfordNERTagger

from coast_core import utils

try:
    nltk.data.find('chunkers/maxent_ne_chunker')
except LookupError:
    nltk.download('maxent_ne_chunker')

try:
    nltk.data.find('corpora/words')
except LookupError:
    nltk.download('words')


def get_stanford_named_entities(text, exception_list=[]):
    """
    Returns a list of named entities in a given block of text.

    :param text: The text to analyse.
    :param exception_list: A list of named entities to ignore.
    :return: A list of named entities.
    """
    # print(os.path.dirname(__file__) + "\\resources\\stanford\\english.conll.4class.distsim.crf.ser.gz",
    #                        os.path.dirname(__file__) + "\\resources\\stanford/stanford-ner.jar")

    try:
        st = StanfordNERTagger(os.path.dirname(__file__) + "\\resources\\stanford\\english.conll.4class.distsim.crf.ser.gz",
                               os.path.dirname(__file__) + "\\resources\\stanford/stanford-ner.jar", encoding="utf-8")

        named_ents = []

        tokenized_text = nltk.word_tokenize(text)
        tagged = st.tag(tokenized_text)

        for value in tagged:
            if value[1] != 'O':
                if value[0] not in exception_list:
                    named_ents.append(value[0])
        return named_ents
    except:
        return -1


# Global variable Needed for nltk named ents
nltk_named_ents = []


def getNodes(parent):
    """
        Never called externally, used to extract entities using nltk.
    """
    for node in parent:
        if type(node) is nltk.Tree:
            if node.label() == 'NE':
                leaves = node.leaves()
                ne = []
                for leaf in leaves:
                    # print(leaf[0])
                    ne += [leaf[0]]

                global nltk_named_ents
                nltk_named_ents.append(ne)

            getNodes(node)


def get_nltk_named_entities(text, exception_list=[]):
    """
    Returns a list of named entities in a given block of text using NLTK's averaged_perceptron_tagger.

    :param text: The text to analyse.
    :param exception_list: A list of named entities to ignore.
    :return: A list of named entities.
    """
    global nltk_named_ents
    nltk_named_ents = []

    words = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(words)
    chunked = nltk.ne_chunk(tagged, binary=True)

    getNodes(chunked)

    result = []

    for ne_list in nltk_named_ents:
        for ne in ne_list:
            if ne not in exception_list:
                result.append(ne)

    return result


def get_pronouns(text, exception_list=[]):
    """
    Returns a list of personal pronouns in a given block of text
        PRP - Personal pronouns
        PRP$ - Possessive pronoun

    :param text: The text to analyse.
    :param exception_list: A list of named entities to ignore.
    :return: A list of named entities.
    """
    # Personal pronouns
    pronoun_list = ['PRP', 'PRP$']
    result = utils.penn_treebank_filter(text, pronoun_list, exception_list)
    return result


def extract_all_named_entities(article_text):
    """
    Extract the named entities for all extracted articles.

    :param article_text: The article text to operate on.
    :return: An object containing all named entities
    """
    stanford = get_stanford_named_entities(article_text)
    nltk = get_nltk_named_entities(article_text)
    pronouns = get_pronouns(article_text)

    return {
        "standford_named_entities": stanford,
        "nltk_named_entities": nltk,
        "pronouns": pronouns
    }
