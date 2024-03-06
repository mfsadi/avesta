import json
from tqdm import tqdm
from avesta.preprocess.preprocessing import persian_character_normalizer
from avesta.resources.stopwords import PERSIAN_STOPWORDS
from avesta.tools.stemmers import ps

term_1 = ''
term_2 = ''
to_stem = False


def normal(term):
    term = persian_character_normalizer(term).lower().replace("-", ' ').replace("_", ' ').replace("(", ' ').replace(")",
                                                                                                                    ' ')
    for i in PERSIAN_STOPWORDS:
        if ' ' + i + ' ' in term:
            term = term.replace(' ' + i + ' ', ' ')
    if to_stem:
        if ' ' in term_1 and ' ' in term_2:
            term = ''.join(sorted([ps.run(i) for i in term.split()]))
        else:
            if ' ' not in term_1 and ' ' not in term_2:
                term = "".join([ps.run(i) for i in term.split()])
            elif ' ' in term:
                term = "".join([ps.run(i) for i in term.split()])
    else:
        if ' ' in term_1 and ' ' in term_2:
            term = ''.join(sorted(term.split()))
        else:
            term = "".join(term.split())
    return term


def lexical_synonym_checker(phrase_1, phrase_2):
    global to_stem, term_1, term_2
    term_1 = phrase_1
    term_2 = phrase_2
    result = 'No'
    if normal(term_1) == normal(term_2):
        result = 'Yes'
    if result == 'No':
        to_stem = True
        if normal(term_1) == normal(term_2):
            result = 'Yes'
    to_stem = False
    return result
