"""
A collection of functions that can be used for analysing the citations within results to other resources.

-------------

See the documentation and sample_data for examples (https://coast-core.readthedocs.io).
"""
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

from bs4 import BeautifulSoup
import sys

from coast_core import utils


def get_an_articles_domain(link):
    """
    For a given URL, parse and return the articles TLDN as a string.

    :param link: The link to parse.

    :return: The domain of the link.
    """
    parsed_uri = urlparse(link)
    domain = parsed_uri.netloc
    return domain


def get_all_citations(html):
    """
    Extract citations from a single articles HTML.

    :param html: The html to operate on.

    :return: A list of all URI's found in the article.
    """
    soup = BeautifulSoup(html, "html5lib")

    all_uris = []

    try:
        for uri in soup.find_all("a"):
            all_uris.append(uri.get("href"))
    except Exception as e:
        sys.stdout.write(e)
        return None
    else:
        return all_uris


def select_external_citations(link, all_uris):
    """
    From a list of uri's, return those that are external to the domain of the link.

    :param link: The link of the article being analysed.
    :param all_uris: A list of all URI's found in the article.

    :return: A list of uris that are external to the domain of the link being analysed.
    """
    domain = get_an_articles_domain(link)

    external_uris = []

    for uri in all_uris:
        if not uri.startswith('#') and not uri.startswith('/'):
            uri_domain = get_an_articles_domain(uri)
            if domain != uri_domain:
                external_uris.append(uri)

    return external_uris


def classify_citations(external_uris, classification_config_file):
    """
    Given a file containing a JSON object of key value {classification:[patterns]} pairs.
    Classify each of the citations for each article.

    For example, given the following JSON:

    {
      "research": ["reseaerchgate", "ieee.", "dx.doi.", "acm", "sciencedirect"]
    }

    All citations that contain any sub-string within the list will be classified as 'research' citations. A
    more detailed JSON example can be found in our test_data: https://github.com/zedrem/coast_core/blob/master/tests/test_data/citations_classification.json

    :param external_uris: A list of uris to classify.
    :param classification_config_file: A config file containing all classifications.

    :return: A list of objects containing all classifications.
    """

    classifications = utils.get_json_from_file(classification_config_file)

    classified_external_uris = []

    for uri in external_uris:
        uri_domain = str(get_an_articles_domain(uri))
        uri_classifications = []
        for key in classifications.keys():
            patterns = classifications[key]

            for pattern in patterns:
                pattern = str(pattern)
                # print(pattern, uri_domain)
                if pattern in uri_domain:
                    uri_classifications.append((key.upper(), pattern))
        # print(uri_classifications)

        classified_external_uris.append({
            "uri": uri,
            "domain": uri_domain,
            "classifications": uri_classifications
        })

    return classified_external_uris


def compute_citation_binary_counts(classified_external_uris, classification_config_file):
    """
    Take binary counts of each citation type.

    :param classified_external_uris: a list of objects containing all classifications.
    :param classification_config_file: A config file containing all classifications.

    :return: An object containing a binary count of each classification type.
    """
    classifications = utils.get_json_from_file(classification_config_file)
    classification_types = [x.upper() for x in classifications.keys()]

    contains_dict = {}

    for cl_type in classification_types:
        contains_dict[cl_type] = False

    for uri in classified_external_uris:
        classifications = uri["classifications"]

        if classifications:
            for classification in classifications:
                # for pattern in classification:
                contains_dict[classification[0]] = True

    return contains_dict


def execute_full_citation_analysis(html, link, classification_config_file):
    """
    Runs a complete end-to-end analysis of citations using all other functions.

    :param html: The html to operate on.
    :param link: The link of the article being analysed.
    :param classification_config_file: A config file containing all classifications.

    :return: An object containing all analysis.
    """
    domain = get_an_articles_domain(link)
    all_uris = get_all_citations(html)
    external_uris = select_external_citations(link, all_uris)
    classified_external_uris = classify_citations(external_uris, classification_config_file)
    citation_binary_counts = compute_citation_binary_counts(classified_external_uris, classification_config_file)

    return {
        "domain": domain,
        "all_uris": all_uris,
        "external_uris": external_uris,
        "classified_external_uris": classified_external_uris,
        "classified_citation_binary_counts": citation_binary_counts
    }
