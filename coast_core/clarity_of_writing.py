"""
A collection of functions that can be used for analysing the clarity of writing within an article
"""

from textstat.textstat import textstat
import nltk
import language_check
from textblob import TextBlob
from langdetect import detect  # breaks the build


def detect_language(text):
    """
    Given a body of text, will use the langdetect library to detect the text language and return.

    :param text: The body of text to analyse.
    :return: The language code (e.g. EN for English).
    """
    lang_code = detect(text)

    return lang_code


def analyse_readability_metrics(article_text):
    """
    Use the textstat library to report multiple readability measures.

    The readability metrics analysed are:
    * The Flesch Reading Ease Score. A score from 100 (very easy to read) to 0 (very confusing).
    * The grade score using the Flesch-Kincaid Grade Formula. For example a score of 9.3 means that a ninth grader would be able to read the document.
    * The FOG index of the given text
    * The SMOG index of the given text
    * The ARI(Automated Readability Index) which outputs a number that approximates the grade level needed to comprehend the text. For example if the ARI is 6.5, then the grade level to comprehend the text is 6th to 7th grade
    * The grade level of the text using the Coleman-Liau Formula
    * The grade level using the Lisear Write Formula
    * The grade level using the New Dale-Chall Formula.



    :param article_text: The article text to operate on.
    :return: An object containing all measures
    """
    sylls = textstat.syllable_count(article_text)
    words = textstat.lexicon_count(article_text)
    sents = textstat.sentence_count(article_text)

    if article_text != "":
        """
            returns the Flesch Reading Ease Score. Following table is helpful to access the ease of readability in a document.

            * 90-100 : Very Easy
            * 80-89 : Easy
            * 70-79 : Fairly Easy
            * 60-69 : Standard
            * 50-59 : Fairly Difficult
            * 30-49 : Difficult
            * 0-29 : Very Confusing
        """
        flesch = textstat.flesch_reading_ease(article_text)

        """
            returns the grade score using the Flesch-Kincaid Grade Formula.
            For example a score of 9.3 means that a ninth grader would be able to read the document.
        """
        flesch_k = textstat.flesch_kincaid_grade(article_text)

        """
            returns the FOG index of the given text.
        """
        fog = textstat.gunning_fog(article_text)

        """
            return the SMOG index of the given text.
        """
        smog = textstat.smog_index(article_text)

        """
            returns the ARI(Automated Readability Index) which outputs a number that approximates the grade level needed to comprehend the text.
            For example if the ARI is 6.5, then the grade level to comprehend the text is 6th to 7th grade
        """
        ari = textstat.automated_readability_index(article_text)

        """
            returns the grade level of the text using the Coleman-Liau Formula
        """
        coleman_l = textstat.coleman_liau_index(article_text)

        """
            returns the grade level using the Lisear Write Formula
        """
        linsear_write = textstat.linsear_write_formula(article_text)

        """
            Different from other tests, since it uses a lookup table of most commonly used 3000 english words.
            Thus it returns the grade level using the New Dale-Chall Formula.
        """
        dale_chall = textstat.dale_chall_readability_score(article_text)

        """
            Based upon all the above tests returns the best grade level under which the given text belongs to.
        """
        overall_consensus = textstat.text_standard(article_text)

        return {
            "syllable_count": sylls,
            "word_count": words,
            "sentence_count": sents,
            "flesch_reading_ease": flesch,
            "flesch_kincaid_grade": flesch_k,
            "gunning_fog": fog,
            "smog_index": smog,
            "automated_readability_index": ari,
            "coleman_liau_index": coleman_l,
            "linsear_write_formula": linsear_write,
            "dale_chall_readability_score": dale_chall,
            "overall_consensus_grade": overall_consensus
        }


def analyse_text_for_grammatical_metrics(article_text):
    """
    Use the language_check library to check a body of text for grammatical issues.

    :param article_text: The text to be analyse.

    :return: The total number of grammatical issues found. A list containing details of each grammatical issue. A list of sentences, tokenized by NLTK.
    """
    try:
        tool = language_check.LanguageTool('en-US')

        sentences = nltk.sent_tokenize(article_text)

        total_grammar_issues = 0
        grammar_issues = []
        for sentence in sentences:
            matches = tool.check(sentence)
            total_grammar_issues += len(matches)

            g_matches = []
            for m in matches:
                sent_match = {
                    'sentence': sentence,
                    'fromy': m.fromy,
                    'fromx': m.fromx,
                    'toy': m.toy,
                    'tox': m.tox,
                    'ruleId': m.ruleId,
                    'msg': m.msg,
                    'replacements': m.replacements,
                    'context': m.context,
                    'contextoffset': m.contextoffset,
                    'offset': m.offset,
                    'errorlength': m.errorlength,
                    'category': m.category,
                    'locqualityissuetype': m.locqualityissuetype
                }
                g_matches.append(sent_match)

            grammar_issues.append(g_matches)

        return {
            "total_grammar_issues": total_grammar_issues,
            "grammar_issues": grammar_issues,
            "sentences": sentences
        }
    except:
        return {
            "total_grammar_issues": -1,
            "grammar_issues": [],
            "sentences": []
        }


def run_sentiment_check(article_text):
    """
    Run sentiment analysis over the article.

    :param article_text: The article text to operate on.

    :return: An object that contain polarity and subjectivity. Polarity, also known as orientation is he emotion expressed in the sentence. It can be positive, neagtive or neutral.
                Subjectivity is when text is an explanatory article which must be analysed in context.
    """
    tb_text = TextBlob(article_text)

    """
        Polarity, also known as orientation is he emotion expressed in the sentence. It can be positive, neagtive or neutral.

        Subjectivity is when text is an explanatory article which must be analysed in context.
    """

    # range [-1.0, 1.0]
    polarity = tb_text.sentiment.polarity

    # range [0.0, 1.0] 0 is objective, 1 is subjective
    subjectivity = tb_text.sentiment.subjectivity

    return {
        "polarity": polarity,
        "subjectivity": subjectivity
    }


def execute_clarity_of_writing_check(article_text):
    """
    Runs a complete end-to-end analysis of clarity of writing using all other functions.

    :param article_text: The article text to operate on.

    :return: An object containing language, readability, grammar and sentiment
    """
    language = detect_language(article_text)
    readability = analyse_readability_metrics(article_text)
    grammar = analyse_text_for_grammatical_metrics(article_text)
    sentiment = run_sentiment_check(article_text)

    return {
        "language": language,
        "readability": readability,
        "grammar": grammar,
        "sentiment": sentiment
    }
