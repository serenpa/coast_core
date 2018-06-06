# Code for tagging temporal expressions in text

import re
# import string
# import os
# import sys

## Args ##

# Returns list as default, unless:
# set to 'markup' - returns markedup string
returnFormat = ""

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


def tag(text, **kwargs):
    returnFormat = kwargs.get('returnFormat', None)

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

    if returnFormat == "markup":

        # Tag only temporal expressions which haven't been tagged.
        for timex in timex_found:
            text = re.sub(timex + '(?!</TIMEX2>)', '<TIMEX2>' + timex + '</TIMEX2>', text)

        return text
    else:
        return timex_found
