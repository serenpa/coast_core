"""
    Test script
"""
import os

TEST_DATA_DIR = "/2nddisc/coast_core/test_data/"


def test_citations():
    """
    Citations
    """
    from coast_core import citations

    link = "https://www.joelonsoftware.com/2006/09/01/language-wars/"
    html = open(TEST_DATA_DIR + "language_wars.html").read()
    classification_config_file = os.path.dirname(__file__) + "/test_data/citations_classification.json"

    # test 1
    domain = citations.get_an_articles_domain(link)
    print(link, domain)

    # test 2
    all_citations = citations.get_all_citations(html)
    print(all_citations)

    # test 3
    external_uris = citations.select_external_citations(link, all_citations)
    print(external_uris)

    # test 4
    classified_external_uris = citations.classify_citations(external_uris, classification_config_file)
    print(classified_external_uris)

    # test 5
    classified_citation_binary_counts = citations.compute_citation_binary_counts(classified_external_uris,
                                                                                 classification_config_file)
    print(classified_citation_binary_counts)

    # test 6
    print(citations.execute_full_citation_analysis(html, link, classification_config_file))


def test_markers():
    """
        Markers
    """
    from coast_core import markers

    article_html = open(TEST_DATA_DIR + "language_wars.html").read()
    config_file = TEST_DATA_DIR + "config_file.json"

    print(markers.run_all_markers(article_html, config_file))


def test_ngrams():
    """
        ngrams
    """
    from coast_core import analyse_ngrams

    article_html = open(TEST_DATA_DIR + "language_wars.html").read()

    print(analyse_ngrams.generate_ngrams(article_html))


def test_named_entities():
    """
    named entities
    """
    from coast_core import named_entities

    article_html = open(TEST_DATA_DIR + "language_wars.html").read()

    print(named_entities.extract_all_named_entities(article_html))


def test_clarity_of_writing():
    """
    Clarity of writing
    """
    from coast_core import clarity_of_writing
    article_html = open(TEST_DATA_DIR + "language_wars.html").read()
    print(clarity_of_writing.execute_clarity_of_writing_check(article_html))


def test_events():
    """
    Events
    """
    from coast_core import events
    article_html = open(TEST_DATA_DIR + "language_wars.html").read()
    print(events.run_all_event_analysis(article_html))


def test_extraction():
    """
    extraction
    """
    from coast_core import extraction
    link = "https://www.joelonsoftware.com/2006/09/01/language-wars/"
    print(extraction.full_extraction(link))


if __name__ == '__main__':
    # test_citations()
    # test_markers()
    # test_ngrams()
    # test_named_entities()
    # test_clarity_of_writing()
    # test_events()
    test_extraction()
