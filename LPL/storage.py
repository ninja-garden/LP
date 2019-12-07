from .Graphematic_analysis import Graphematics_analysis
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

class SimpleSentence(Sentence):
    """
    Простое предложение
    """
    def __init__(self):
        pass

class Meta_info:
    """
    Метаинформация о тексте
    """
    def __init__(self, graph_res):
        """
        Инициализация метаинформации о тексте
        :param graph_res:
        """
        self.n_words = graph_res.n_words
        self.n_sentences = len(graph_res.sentences)
        self.len_sentences = graph_res.len_sentences

class TextStorage:
    """
    Класс хранилища
    """
    def __init__(self, text):
        """
        Инициализация хранилища
        :param text: текст
        """
        self.text = text
        graphematic_result = Graphematics_analysis(text)
        self.meta_info = Meta_info(graphematic_result)


