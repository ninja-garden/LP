# -*- coding: utf-8 -*-

""" Функции графематического анализа """

from nltk.tokenize import sent_tokenize as nlt_sent_tokenize
from nltk.tokenize import word_tokenize as nlt_word_tokenize
import re

def sent_tokenize(text):
    """
    Функция разбиения текста на предложения
    :param text: исходный текст
    :return: спискок предложений
    """
    pattern = re.compile(r'([А-ЯA-Z]((т.п.|т.д.|пр.|г.)|[^?!.\(]|\([^\)]*\))*[.?!])')
    return pattern.findall(text)


def main():
    text = 'вы выполняете поиск. Используем Google SSL;'
    tokens = sent_tokenize(text)
    print(tokens)
    print(nlt_sent_tokenize(text))
    print(nlt_word_tokenize(text))


if __name__ == "__main__":
    main()

"""
Как вариант:

from nltk.tokenize import sent_tokenize
sentence = "As the most quoted English writer Shakespeare has more than his share of famous quotes.  Some Shakespare famous quotes are known for their beauty, some for their everyday truths and some for their wisdom. We often talk about Shakespeare’s quotes as things the wise Bard is saying to us but, we should remember that some of his wisest words are spoken by his biggest fools. For example, both ‘neither a borrower nor a lender be,’ and ‘to thine own self be true’ are from the foolish, garrulous and quite disreputable Polonius in Hamlet."

sent_tokenize(sentence)

import nltk
words = nltk.word_tokenize(raw_sentence)
"""