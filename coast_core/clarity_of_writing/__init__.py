"""
    Title: clarity_of_writing.py

    Author: Ashley Williams

    Description: A collection of functions that can be used for analysing the
    clarity of writing within results.

    This module is called by init, so there is no need to import this module
    specifically.

    Refer to the documentation for details of how to use this module
    (<<link>>).
"""
from coast_core.clarity_of_writing import clarity_of_writing


def detect_language(text):
	"""
	    Given a body of text, will use the langdetect library to detect the
	    text language and return.

	    Args:
	        text: The body of text to analyse.

	    Returns:
	        lang_code: The language code (e.g. EN for English).
	"""
	return clarity_of_writing.detect_language(text)



def analyse_readability_metrics(article_text):
	"""
	    Use the textstat library to report multiple readability measures.

	    Refer to the documentation for details of what each measure means
	    (<<link>>).

	    Args:
	        article_text: The article text to operate on.
	"""
	return clarity_of_writing.analyse_readability_metrics(article_text)



def analyse_text_for_grammatical_metrics(article_text):
	"""
	    Use the language_check library to check a body of text
	    for grammatical issues.

	    Args:
	        article_text: The text to be analyse.

	    Returns:
	        total_grammar_issues: The total number of grammatical issues found.
	        grammar_issues: A list containing details of each grammatical issue.
	        sentences: A list of sentences, tokenized by NLTK.
	"""
	return clarity_of_writing.analyse_text_for_grammatical_metrics(article_text)



def run_sentiment_check(article_text):
	"""
	    Run sentiment analysis over all articleself.

	    Args:
	        article_text: The article text to operate on.
	"""
	return clarity_of_writing.run_sentiment_check(article_text)



def execute_clarity_of_writing_check(article_text):
	"""
	    Runs a complete end-to-end analysis of clarity of writing using all
	    other functions.

	    Refer to the documentation for usage guidelines and descriptions of
	    how the config file should be structured (<<link>>).

	    Args:
	        article_text: The article text to operate on.
	"""
	return clarity_of_writing.execute_clarity_of_writing_check(article_text)
