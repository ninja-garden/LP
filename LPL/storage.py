# -*- coding: utf-8 -*-

""" Храниище данных ЛП """


class Sentence:
    """
    Предложение
    """
    def __init__(self):
        pass


class ComplexSentence(Sentence):
    """
    Сложное предложение
    """
    def __init__(self):
        pass

class SImpleSentence(Sentence):
    """
    Простое предложение
    """
    def __init__(self):
        pass

class Text:
    """
    Метаинформация о тексте
    """
    def __init__(self, text=''):
        """
        Инициализация метаинформации о тексте
        :param text:
        """
        self.num_words = 0
        self.words = none
        self.num_sents = 0
        self.sents = []
        self.num_sym = 0

class TextStorage:
    """
    Класс хранилища
    """
    def __init__(self, text):
        """
        Инициализация хранилища
        :param text: объект класса Text с метаинформацией о тексте
        """
        self.text = Text
