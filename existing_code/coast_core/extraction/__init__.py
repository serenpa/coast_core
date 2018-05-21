"""
    Title: extraction_command.py

    Author: Ashley Williams

    Description: A collection of functions that can be used for extracting
    information from the results of the searchs.

    This module is called by init, so there is no need to import this module
    specifically.

    Refer to the documentation for details of how to use this module
    (<<link>>).
"""
from coast_core.extraction import extraction


def get_html(url):
    """
        Given a URL, will return the HTML using urllib3.

        Args:
            url: The url to extract the HTML from

    """
    return extraction.get_html(url)




def pattern_article_extraction(uri):
    """
        Extract the article using Pattern. Pattern uses the url, not the HTML
        Add to the articles_pattern collection.

        Args:
            uri: The url to extract the HTML from

    """
    return extraction.pattern_article_extraction(uri)



def full_extraction(url):
    """
        Runs a complete end-to-end extraction using all other functions.

        Refer to the documentation for usage guidelines and descriptions of
        how the config file should be structured (<<link>>).

        Args:
            url: The url to extract the HTML from

    """
    return extraction.full_extraction(url)
