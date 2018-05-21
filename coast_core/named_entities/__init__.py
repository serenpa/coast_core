"""
        Title: named_entities.py

        Author: Ashley Williams

        Description: Extract named entities from text.

        This module is called by init, so there is no need to import this module
        specifically.

        Refer to the documentation for details of how to use this module
        (http://coast.readthedocs.io/).
"""
from coast_core.named_entities import named_entities


def get_stanford_named_entities(text, exception_list=[]):
    """
        Returns a list of named entities in a given block of text.

        Args:
            text: The text to analyse.
            exception_list: A list of named entities to ignore.


        Returns:
            named_ents: A list of named entities.
    """
    return named_entities.get_stanford_named_entities(text, exception_list=[])



def get_nltk_named_entities(text, exception_list=[]):
    """
        Returns a list of named entities in a given block of text using NLTK's
        averaged_perceptron_tagger.

        Args:
            text: The text to analyse.
            exception_list: A list of named entities to ignore.


        Returns:
            result: A list of named entities.
    """
    return named_entities.get_nltk_named_entities(text, exception_list=[])



def get_pronouns(text, exception_list=[]):
    """
        Returns a list of personal pronouns in a given block of text

        Args:
            text: The text to analyse.
            exception_list: A list of named entities to ignore.


        Returns:
            result: A list of named entities.
    """
    return named_entities.get_pronouns(text, exception_list=[])



def extract_all_named_entities(article_text):
    """
        Extract the named entities for all extracted articles.

        Args:
            article_text: The article text to operate on.

        Returns:
            result: An object containing all named entities
    """
    return named_entities.extract_all_named_entities(article_text)
