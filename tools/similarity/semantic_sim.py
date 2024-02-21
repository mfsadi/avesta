import json
import warnings
import pandas as pd
from pathlib import Path
from avesta.preprocess.preprocessing import persian_character_normalizer
from avesta.resources.stopwords import PERSIAN_STOPWORDS
from avesta.tools.stemmers import ps

warnings.simplefilter('ignore', category=UserWarning)
syn_data_path = Path(__file__).parent.parent.parent / "resources" / "synonym"
ecom_synonyms = pd.read_csv(Path.joinpath(syn_data_path, "ecom_synonyms.csv"))
ecom_synonyms_dict = ecom_synonyms.set_index('two').T.to_dict('list')
ecom_synonyms_dict_rev = ecom_synonyms.set_index('two').T.to_dict('list')

term_1 = ''
term_2 = ''
to_stem = False
is_synonym_affected = False


def normal(term):
    term = persian_character_normalizer(term).lower().replace("-", ' ').replace("_", ' ').replace("(", ' ').replace(")",
                                                                                           ' ')
    for i in PERSIAN_STOPWORDS:
        if ' ' + i + ' ' in term:
            term = term.replace(' ' + i + ' ', ' ')
    if ' ' in term_1 and ' ' in term_2:
        term = ''.join(sorted("".join((term.split()))))
    else:
        term = "".join(term.split())
    return term


def semantic_synonym_checker(phrase_1, phrase_2):
    global term_1, term_2, is_synonym_affected
    term_1 = phrase_1
    term_2 = phrase_2
    result = 'No'
    for word in phrase_1.split():
        for token in ecom_synonyms_dict.keys():
            if token.lower() == word.lower():
                phrase_1 = phrase_1.replace(token, ecom_synonyms_dict[token][0])
                is_synonym_affected = True
    for word in phrase_2.split():
        for token in ecom_synonyms_dict.keys():
            if token.lower() == word.lower():
                phrase_2 = phrase_2.replace(token, ecom_synonyms_dict[token][0])
                is_synonym_affected = True
    if is_synonym_affected:
        phrase_1 = normal(phrase_1)
        phrase_2 = normal(phrase_2)
    if phrase_1 == phrase_2:
        result = 'Yes'
    is_synonym_affected = False
    return result