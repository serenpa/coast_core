"""
A collection of functions that can be used for splitting the article into ngrams.
"""

from coast_core import utils
from collections import defaultdict

try:
    from nltk.corpus import stopwords
except ImportError:
    import nltk

    nltk.download('stopwords')
    from nltk.corpus import stopwords


def generate_ngrams(article_text):
    """
    Split the given text into ngrams, returning an object that contains ngrams from one to six.

    :param article_text: the block of text to operate on.
    :return: An object containing all ngrams up to 6 in the following structure:

        .. code-block:: python

          {
              "unigrams": [list of unigrams],
              "bigrams": [list of bigrams],
              "trigrams": [list of trigrams],
              "fourgrams": [list of fourgrams],
              "fivegrams": [list of fivegrams],
              "sixgrams": [list of sixgrams]
          }

    """

    unigrams = utils.get_ngrams(article_text, 1)
    bigrams = utils.get_ngrams(article_text, 2)
    trigrams = utils.get_ngrams(article_text, 3)
    fourgrams = utils.get_ngrams(article_text, 4)
    fivegrams = utils.get_ngrams(article_text, 5)
    sixgrams = utils.get_ngrams(article_text, 6)

    return {
        "unigrams": unigrams,
        "bigrams": bigrams,
        "trigrams": trigrams,
        "fourgrams": fourgrams,
        "fivegrams": fivegrams,
        "sixgrams": sixgrams
    }


def calculate_ngram_frequency_count(article_text, ngram_size, stop_list=None):
    """
    Calculate the frequency of occurances for a given ngram based on an article test
    :param article_text: the block of text to operate on.
    :param ngram_size: the degree of ngmram to be returned (eg 3 would be a tri gram)
    :param stop_list: list of words to be excluded from the frequency count
    :return: An object containing the frequency count of the n grams without ngrams included in the stop list
    """

    if stop_list is None:
        stop_list = set(stopwords.words('english'))
    else:
        stop_list = set(stop_list)

    ngrams = utils.get_ngrams(article_text, ngram_size)
    ngram_frequency_count = defaultdict(int)
    for ngram in ngrams:
        ngram_set = set(ngram)
        intersection = ngram_set.intersection(stop_list)
        ngram_in_stop_list = len(intersection) > 0

        if not ngram_in_stop_list:
            ngram_frequency_count[ngram] += 1

    frequency_count = list(ngram_frequency_count.items())
    return {
        "frequency_count": frequency_count
    }
