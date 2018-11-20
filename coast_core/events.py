"""
Extract event instances from text.
"""

from coast_core import utils
import nltk
import re

try:
    nltk.data.find('taggers/averaged_perceptron_tagger')
except LookupError:
    nltk.download('averaged_perceptron_tagger')

try:
    nltk.data.find('taggers/punkt')
except LookupError:
    nltk.download('punkt')


def get_timex_events(text):
    """
    Given a body of text, returns a list of Timex events. Timex events are temporal events that are detected using regular expressions.
    Our timex library is a variation of the Timex module in NLTK_contrib: https://github.com/nltk/nltk_contrib/blob/master/nltk_contrib/timex.py

    :param text:  The text to operate on
    :return: return the timex events
    """
    timex_events = timex_tag(text)
    return timex_events


def get_verb_events(text):
    """
    Given a body of text, returns a list of verb events.
        VB - Verb, base form
        VBD - Verb, past tense
        VBG - Verb, gerund or present participle
        VBN - Verb, past participle - n
        VBP - Verb, non-3rd person singular present - n
        VBZ - Verb, 3rd person singular present - n

    :param text: The text to analyse.
    :return: The list of verb events.
    """
    verb_events = []
    verb_list = ['VB', 'VBD', 'VBG']
    verb_events = utils.penn_treebank_filter(text, verb_list)
    return verb_events


def get_iverb_bigrams(text):
    """
    Split a text into bigrams, following the pattern ("i", <<verb>>).
        VB - Verb, base form
        VBD - Verb, past tense
        VBG - Verb, gerund or present participle
        VBN - Verb, past participle - n
        VBP - Verb, non-3rd person singular present - n
        VBZ - Verb, 3rd person singular present - n

    :param text: The text to analyse
    :return: A dictionary containing 'I verb' bigrams and the total number of 'I verb' events.
    """
    bigrams = utils.get_ngrams(text, 2)

    iverb_dict = {
        "total": 0,
        "events": []
    }

    for bigram in bigrams:
        if bigram[0].lower() == "i":
            # Verbs
            iverb_list = ['VBD', 'VBN']
            iverb_events = utils.penn_treebank_filter(bigram[1], iverb_list)

            if len(iverb_events) > 0:
                iverb_dict['total'] += 1
                iverb_dict['events'].append({
                    "bigram": bigram,
                    "verb": iverb_events[0]
                })
    return iverb_dict


def run_all_event_analysis(article_text):
    """
    Run all event analysis for all articles.

    :param article_text: The text to analyse.
    :return: An object containing timex events, verb events and iverb bigrams
    """
    timex = get_timex_events(article_text)
    verbs = get_verb_events(article_text)
    iverbs = get_iverb_bigrams(article_text)

    return {
        "timex_events": timex,
        "verb_events": verbs,
        "iverb_bigrams": iverbs
    }


def timex_tag(text, **kwargs):
    """
        Extract the timex events from a given body of text
        
        :param text: The body of text to operate on
        :return: A list of timex events as default, unless 'markup' argument is
                 given. In which case, returns a markedup string.
        
    """
    return_format = ""

    ## End Args ##

    # Predefined strings.
    numbers = "(^a(?=\s)|one|two|three|four|five|six|seven|eight|nine|ten| \
              eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen| \
              eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty| \
              ninety|hundred|thousand)"
    day = "(monday|tuesday|wednesday|thursday|friday|saturday|sunday)"
    week_day = "(monday|tuesday|wednesday|thursday|friday|saturday|sunday)"
    month = "(January|February|March|April|May|June|July|August|September| \
              October|November|December|january|february|march|april|june| \
              july|october|november|december)"
    dmy = "(year|day|week|month)"
    rel_day = "(today|yesterday|tomorrow|tonight|tonite)"
    exp1 = "(before|after|earlier|later|ago)"
    exp2 = "(this|next|last)"
    iso = "\d+[/-]\d+[/-]\d+ \d+:\d+:\d+\.\d+"
    year = "((?<=\s)\d{4}|^\d{4})"
    regxp1 = "((\d+|(" + numbers + "[-\s]?)+) " + dmy + "s? " + exp1 + ")"
    regxp2 = "(" + exp2 + " (" + dmy + "|" + week_day + "|" + month + "))"

    # Ash Added
    df0 = "((\d+[-|.|/]\d+[-|.|/]\d+)|(\d{1,2}/\d{1,2}))[.\s]"  # 04/04/1992, 04/04, 04-04, 04.04.92 etc
    reyear = "(((in|year)|" + month + ")[,]?\s\d{4})"
    wordyear = "(((nineteen)\s" + numbers + "\s" + numbers + ")|((two)\s(thousand)\s(and)\s" + numbers + "\s?" + numbers + "?))"  # thousand\sand)\s" + numbers + ")"  #"(nineteen\s" + numbers +"\s" + numbers + ")|(two\sthousand\sand\s" + numbers + ")"# + "(\s" + numbers +")?)"
    temporal_phrases = "((since|when|during))"
    remonth = month + "s?(.|,)?\s"

    reg1 = re.compile(regxp1, re.IGNORECASE)
    reg2 = re.compile(regxp2, re.IGNORECASE)
    reg3 = re.compile(rel_day, re.IGNORECASE)
    reg4 = re.compile(iso)
    reg5 = re.compile(reyear, re.IGNORECASE)  # ash modified

    # Ash Added
    reg6 = re.compile(df0)
    reg7 = re.compile(remonth)
    reg8 = re.compile(day, re.IGNORECASE)
    reg9 = re.compile(wordyear, re.IGNORECASE)
    reg10 = re.compile(temporal_phrases, re.IGNORECASE)

    return_format = kwargs.get('return_format', None)

    text = text.lower()

    # Initialization
    timex_found = []

    # re.findall() finds all the substring matches, keep only the full
    # matching string. Captures expressions such as 'number of days' ago, etc.
    found = reg1.findall(text)
    found = [a[0] for a in found if len(a) > 1]
    for timex in found:
        timex_found.append(timex)

    # Variations of this thursday, next year, etc
    found = reg2.findall(text)
    found = [a[0] for a in found if len(a) > 1]
    for timex in found:
        timex_found.append(timex)

    # Year
    found = reg5.findall(text)
    found = [a[0] for a in found if len(a) > 1]  # ash added
    for timex in found:
        timex_found.append(timex)

    # today, tomorrow, etc
    found = reg3.findall(text)
    for timex in found:
        timex_found.append(timex)

    # ISO
    found = reg4.findall(text)
    for timex in found:
        timex_found.append(timex)

    # Ash Added

    # DateFormat
    found = reg6.findall(text)
    found = [a[0] for a in found if len(a) > 1]
    for timex in found:
        timex_found.append(timex)

    # Month
    found = reg7.findall(text)
    found = [a[0] for a in found if len(a) > 1]
    for timex in found:
        timex_found.append(timex)

    # Year
    found = reg8.findall(text)
    for timex in found:
        timex_found.append(timex)

    # WordYear
    found = reg9.findall(text)
    found = [a[0] for a in found if len(a) > 1]
    for timex in found:
        timex_found.append(timex)

    # Temporal Pharses
    found = reg10.findall(text)
    found = [a[0] for a in found if len(a) > 1]
    for timex in found:
        timex_found.append(timex)

    if return_format == "markup":

        # Tag only temporal expressions which haven't been tagged.
        for timex in timex_found:
            text = re.sub(timex + '(?!</TIMEX2>)', '<TIMEX2>' + timex + '</TIMEX2>', text)

        return text
    else:
        return timex_found
