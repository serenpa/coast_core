"""
    Title: citation.py

    Author: Ashley Williams

    Description: A collection of functions that can be used for analysing the
    citations within results to other resources.

    This module is called by init, so there is no need to import this module
    specifically.

    Refer to the documentation for details of how to use this module
    (<<link>>).
"""

from coast_core.citations import citations as c


def get_an_articles_domain(link):
    """
        For a given URL, parse and return the articles TLDN as a string.

        Args:
            link: The link to parse

        Returns:
            domain: The domain of the link.
    """
    return c.get_an_articles_domain(link)


def get_all_citations(html):
    """
        Extract citations from a single articles HTML.

        Args:
            html: The html to operate on.
    """
    return c.get_all_citations(html)


def select_external_citations(link, all_uris):
    """
        From a list of uri's, return those that are external to the domain of
        the link.

        Args:
            link: The link of the article being analysed.
            all_uris: A list of all URI's found in the article.

        Returns:
            external_uris: A list of uris that are external to the domain of the
            link being analysed.
    """
    return c.select_external_citations(link, all_uris)


def classify_citations(external_uris, classification_config_file):
    """
        Given a file containing a JSON object of key value
        {classification:[patterns]} pairs.
        Classify each of the citations for each article.

        Args:
            external_uris: A list of uris to classify.
            classification_config_file: A config file containing all
            classifications. See the documentation and sample_data for examples.
            (<<link>>)

        Returns:
            classified_external_uris: a list of objects containing all
            classifications.
    """
    return c.classify_citations(external_uris, classification_config_file)



def compute_citation_binary_counts(classified_external_uris, classification_config_file):
    """
        Take binary counts of each citation type.

        Args:
            classified_external_uris: a list of objects containing all
            classifications.
            classification_config_file: A config file containing all
            classifications. See the documentation and sample_data for examples.
            (<<link>>)

        Returns:
            contains_dict: an object containing a binary count of each
            classification type.
    """
    return c.compute_citation_binary_counts(classified_external_uris, classification_config_file)



def execute_full_citation_analysis(html, link, classification_config_file):
    """
        Runs a complete end-to-end analysis of citations using all other
        functions.

        Args:
            html: The html to operate on.
            link: The link of the article being analysed.
            classification_config_file: A config file containing all
            classifications. See the documentation and sample_data for examples.
            (<<link>>)

        Returns:
            Result: an object containing all analysis.
    """
    return c.execute_full_citation_analysis(html, link, classification_config_file)
