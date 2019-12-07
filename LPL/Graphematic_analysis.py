""" Функции графематического анализа """
import nltk as nl
import codecs


class Graphematics_analysis:
    def __init__(self, text):
        self.sentences = self.sent_tokenize(text)
        self.tonenized_sentences = [self.word_tokenize(sentence) for sentence in self.sentences]
        self.len_sentences = [len(sentence) for sentence in self.tonenized_sentences]
        self.n_words = sum(self.len_sentences)

    def sent_tokenize(self, text):
        """
        Функция разбиения текста на предложения
        :param text: исходный текст
        :return: список предложений
        """
        return nl.sent_tokenize(text, language="russian")


    def word_tokenize(self, sentence):
        """
        Функция разбиения предложения на слова
        :param sentense(str): исходный текст
        :return: список слов
        Пока все специальные символы - отдельные слова.
        Когда будут инструкции на эту тему исключим.
        """
        return nl.word_tokenize(sentence)

