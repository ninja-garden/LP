import json
import copy

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class WordCombinations:
    """
    Класс содержит информацию по словосочетаниям для каждого предложения
    """
    def __init__(self):
        self.combinations = []

    def add_combination(self, first_word_ind, word_comb_type,
                        main_word_ind, word_comb_len):
        d = dict()
        d['first_word_ind'] = first_word_ind
        d['word_comb_type'] = word_comb_type
        d['main_word_ind'] = main_word_ind
        d['word_comb_len'] = word_comb_len
        self.combinations.append(d)

    def get_combinations(self):
        return self.combinations

class Sentences:
    """
    Класс содержит информацию по всем сложным предложениям
    """
    def __init__(self, sent_type, first_simp_sent_ind, num_words_simp_sent):
        """
        :param sent_type: тип предложения
        :param first_simp_sent_ind: индекс вхождения первого простого предложения
        :param num_words_simp_sent:
        """
        self.sentences = []
        self.sent_type = sent_type
        self.first_simp_sent_ind = first_simp_sent_ind
        self.num_words_simp_sent = num_words_simp_sent

    def add_sentence(self, sent):
        """
        Добавление предложения в список
        :param simp_sent: сложное предложение
        :return:
        """
        self.sentences.append()

    def get_sentences(self):
        """
        Получение списка сложных предложение
        :return: сложное предложение
        """
        return self.sentences

class SimpleSentence:
    """
    Класс простого предложения
    """
    def __init__(self, word_comb, words, simp_sent_type):
        """
        :param word_comb: список словосочетаний
        :param words: список слов
        :param simp_sent_type: тип простого предложения
        """
        self.word_comb = word_comb
        self.words = words
        self.simp_sent_type = simp_sent_type

class Word:
    """
    Класс слова
    """
    def __init__(self, gramm_class, flect_class, ending_len):
        """
        :param gramm_class: Грамматический класс
        :param flect_class: Флективный класс
        :param ending_len: Длина окончания
        """
        self.gramm_class = gramm_class
        self.flect_class = flect_class
        self.ending_leng = ending_len


class TextStorage(metaclass=Singleton):
    def __init__(self):
        # Содержит общую информацию о тексте (результат графематического анализа)
        self._Text = {'text': None, 'num_words': 0, 'words_list': [],
                       'words_len': [], 'num_sents': None, 'sent_list': None,
                       'num_syms': None}  # Метаинформация о тексте

        self._word_combinations = []

        self._sentences = Sentences()

        self._simple_sentences = []

        #_Morph - результат морфологии
        # sents_morph_classes содержит список предложений - каждый
        #  элемент списка - список морфологических классов
        self._Morph = {'sents_morph_classes':[]}

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, value):
        self._Text = value
        # При изменении текста добавляем каждому предложению список словосочетаний
        for i in range(self._Text["num_sents"]):
            self._word_combinations.append(WordCombinations())

    @property
    def Sent(self):
        return self._Sentence

    @Sent.setter
    def Sent(self, value):
        self._Sentence = value

    @property
    def SimpSent(self):
        return self._SimpleSentence

    @SimpSent.setter
    def SimpSent(self, value):
        self._SimpleSentence = value

    @property
    def Word_combinations(self):
        return self._word_combinations

    @Word_combinations.setter
    def Word_combinations(self, value):
        self._word_combinations = value

    @property
    def Word(self):
        return self._Word

    @Word.setter
    def Word(self, value):
        self._Word = value

    def graphematic_to_json(self, filename):
        """
        Сохраняем результаты графематического анализа в json файл
        :return:
        """
        with open(filename, "w") as json_file:
            json.dump(self._Text, json_file, indent=4, sort_keys=True, ensure_ascii=False)
