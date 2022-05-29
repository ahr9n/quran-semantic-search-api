import re
import numpy as np
from nltk import ngrams

# Clean/Normalize Arabic Text


def clean_str(text):
    search = ["أ", "إ", "آ", "ة", "_", "-", "/", ".", "،", " و ", " يا ",
              '"', "ـ", "'", "ى", "\\", '\n', '\t', '&quot;', '?', '؟', '!', '»', '«']
    replace = ["ا", "ا", "ا", "ه", " ", " ", "", "", "", " و", " يا",
               "", "", "", "ي", "", ' ', ' ', ' ', ' ? ', ' ؟ ', ' ! ', '', '']

    # remove tashkeel
    p_tashkeel = re.compile(r'[\u0617-\u061A\u064B-\u0652]')
    text = re.sub(p_tashkeel, "", text)

    # remove longation
    p_longation = re.compile(r'(.)\1+')
    subst = r"\1\1"
    text = re.sub(p_longation, subst, text)

    text = text.replace('وو', 'و')
    text = text.replace('يي', 'ي')
    text = text.replace('اا', 'ا')

    for i in range(0, len(search)):
        text = text.replace(search[i], replace[i])

    # trim/strip whitespaces
    text = text.strip()

    return text


def get_verse_frequency_score(query_word, verse_text, model):
    '''
    Calculate the frequency score of a verse with a given word
    '''

    freq = 0
    for verse_word in verse_text.split():
        if verse_word not in model:
            continue
        score = model.similarity(query_word, verse_word)
        if score > 0.3:
            freq += 1
    return freq


def get_most_similar_verses(query_word, model):
    '''
    Get the most similar verses to the query word based on the frequency score
    '''

    # Prepare/Read Quran data
    quran_clean_text = open("data/quran-simple-clean.txt").readlines()

    # Maybe use this instead to display well-formed verses
    quran = open("data/quran-simple-min.txt").readlines()

    verse_scores, index = [], 0
    for verse in quran_clean_text:
        score = get_verse_frequency_score(query_word, verse, model)
        verse_scores.append((score, index))
        index += 1

    verse_scores.sort(reverse=True)

    # TODO: check max length of verses_scores
    most_similar_verses = [quran_clean_text[index][:-1] for score, index in verse_scores[:10]]
    return most_similar_verses
