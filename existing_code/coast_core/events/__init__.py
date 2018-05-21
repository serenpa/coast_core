"""
        Title: events.py

        Author: Ashley Williams

        Description: Extract event instances from text.

        This module is called by init, so there is no need to import this module
        specifically.

        Refer to the documentation for details of how to use this module
        (<<link>>).
"""
from coast_core.events import events


def get_timex_events(text):
    """
        Given a body of text, returns a list of Timex events.

        Args:
            text: Thedef run_iverb_analysis(db):
    """
    return events.get_timex_events(text)


def get_verb_events(text):
    """
        Given a body of text, returns a list of verb events.

        Args:
            text: The text to analyse.

        Returns:
            verb_events: The list of verb events.
    """
    """
        VB - Verb, base form
        VBD - Verb, past tense
        VBG - Verb, gerund or present participle
        VBN - Verb, past participle - n
        VBP - Verb, non-3rd person singular present - n
        VBZ - Verb, 3rd person singular present - n
    """
    return events.get_verb_events(text)


def get_iverb_bigrams(text):
    """
        Given a body of text, split into bigrams and return all instances of
        bigrams that follow the pattern ("i", <<verb>>).

        Args:
            text: The text to analyse.

        Returns:
            iverb_dict: A dictionary containing 'I verb' bigrams and the total
            number of 'I verb' events.
    """
    return events.get_iverb_bigrams(text)



def run_all_event_analysis(article_text):
    """
        Run all event analysis for all articles.

        Args:
            article_text: The text to analyse.
    """
    return events.run_all_event_analysis(article_text)
