import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

import json
import re

from kw import KW
import config


# TODO '''IN PROGRESS''' -> split the sentences and then find the keywords and select around those keywords 
# TODO: Extract gender and age of the subject
# TODO: Remove url and links
# TODO: Remove punctuations -- removed using proxy with min_length filter
# TODO: Correct spellings


def remove_spaces(text):
    text = " ".join(text.split())
    text = text.lower()
    return text


def str_to_int(N):
    """return: int , parameter: str"""
    """ '150cm' to 150 """
    t = ''
    N = N.strip()

    for n in N:
        try:
            t += str(int(n.strip()))
        except:
            break

    return int(t)


def height(text):
    # foot
    ftpt0 = re.compile(r"\d.\d")     # example:  "5'6"
    ftpt1 = re.compile(r"\d.\d\,")
    ftpt2 = re.compile(r"\d.\d\"")

    cmpt = re.compile(r"\d\d\dcm")

    ftpt = [ftpt0, ftpt1, ftpt2, cmpt]

    height = "height"
    split_text = text.split()

    for i, s in enumerate(split_text):
        if height in s:
            return split_text[i+1]

    # for height in foot and inches
    for pt in ftpt:
        for i, s in enumerate(split_text):
            f = pt.finditer(text)
            f = list(f)     # need to convert into list for some wierd reason

            if len(f) == 1:
                return f[0][0]
    
    return 0


def weight(text):
    # lbs and kg

    bspt = re.compile(r"\d\d\d")            # base pattern - to be used after exhausting every pattern
    kgpt = re.compile(r"\d+.kg")            # kilos
    lbpt = re.compile(r"\d+..bs")           # ibs, Ibs, etc 
    pdpt = re.compile(r"\d+.pounds")        # pounds
    lbpt1 = re.compile(r"\d+lb")            # lb
    lbpt2 = re.compile(r"\d+.lb")           # with some special symbols and spaces
    wept0 = re.compile(r"weig\w+..\d+")     # "weigh 123"
    wept1 = re.compile(r"weight..\d\d\d")   # "weight: 149"   TODO: -- doesn't works

    # sequence is important - using bspt first leads to information loss of units
    wtpt = [kgpt, lbpt, lbpt1, lbpt2, pdpt, wept0, wept1, bspt]
    
    weight = "weight:"
    split_text = text.split()

    for i, s in enumerate(split_text):
        if weight in s:
            return split_text[i+1]
            
    for pt in wtpt:
        w = pt.finditer(text)
        w = list(w)

        if len(w) == 1:         # condition to stop from searching for further patterns
            return w[0][0]
    
    return 0    # in case of no weights or unable to match patterns - only for 6% cases - TODO


# TODO >>
def age_gender(text):
    """ return: age and gender of the subject"""
    return


def symptoms(text):
    text = remove_spaces(text)
    syms = {}
    txt = text.split()
    for i, t in enumerate(txt):
        for kw in KW:
            if kw == t:
                temp = txt[i-2: i]
                syms[kw] = temp
    return syms


# remove stop_words and 
def remove_stopwords(text):
    text = remove_spaces(text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tok_list = [w for w in tokens if w not in stop_words]
            
    return tok_list


def tok_sequence(tok_list, min_length, window):
    """
        - takes in tokens list and returns the tokens within a window

        input: ['male', '21', '5"6', 154lbs', 'dull-to', ',', 'severe', 'pain', 'upper', 'lower', 'body', 'lower']
        
        eg: if window == 2 and keyword is 'pain' then

        return: ['dull-to', 'severe', 'pain', 'upper', 'lower']

        eg: if min_length == 3 then len(token) < 3 gets dropped from the list.
    """
    tok_seq = []
    
    for w in tok_list:
        if len(w) > min_length:
            tok_seq.append(w)

    return tok_seq


