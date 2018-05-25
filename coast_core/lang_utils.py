"""
A collection of generic utility functions that are used throughout coast by various modules relating to NLP tasks.
"""
import nltk
from nltk.util import ngrams
from nltk import word_tokenize


def import_punkt():
    """
        Import punkt
    """
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')


def penn_treebank_filter(article_text, filter_list, exception_list=[]):
    """
    Returns a list of tuples that are tagged with any penn treebank tag from the filter list.

    :param article_text: The text to analyse.
    :param filter_list: The tags to return.
    :param exception_list: A list of exception.
    :return: A list of words containing any of the tags in the filter list.
    """
    words = nltk.word_tokenize(article_text)
    tagged = nltk.pos_tag(words)

    result = []

    for tag in tagged:
        word, tag_type = tag
        if word not in exception_list:
            if tag_type in filter_list:
                result.append(tag)

    return result


def get_ngrams(text, number):
    """
    Split a given body of text into ngrams.

    :param text: The body of text to operate on.
    :param number: Specify the size of the ngram (e.g unigram, bigram etc).
    :return: A list of ngrams.
    """
    import_punkt()
    tokens = word_tokenize(text)
    text_ngrams = ngrams(tokens, number)
    return list(text_ngrams)
