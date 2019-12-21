""" Функции графематического анализа """
import nltk as nl
import codecs


class Graphematic_analysis:
    def __init__(self, text):
        """
        Инициализация класса графематического анализа
        :param text: исходный текст который необходимо разобрать
        """
        self._sentences = self.sent_tokenize(text)
        self._tokenized_sentences = [self.word_tokenize(sentence) for sentence in self.sentences]
        self._len_sentences = [len(sentence) for sentence in self.tokenized_sentences]
        self._n_words = sum(self.len_sentences)

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

    @property
    def sentences(self):
        """
        getter для _sentences
        :return: self._sentences
        """
        return self._sentences

    @property
    def tokenized_sentences(self):
        """
        getter для _tokenized_sentences
        :return: self._tokenized_sentences
        """
        return self._tokenized_sentences

    @property
    def len_sentences(self):
        """
        getter для _len_sentences
        :return: self._len_sentences
        """
        return self._len_sentences

    @property
    def n_words(self):
        """
        getter для _n_words
        :return: self._n_words
        """
        return self._n_words

