import json

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class TextStorage(metaclass=Singleton):
    __metaclass__ = Singleton

    def __init__(self):
        self.__Text = {'text': None, 'num_words': 0, 'words_list': [],
                       'words_len': [], 'num_sents': None, 'sent_list': None,
                       'num_syms': None}  # Метаинформация о тексте

        self.__Sentence = {'simp_sent_list': [], 'sent_type': [], 'first_simp_sent_ind': [],
                           'num_words_simp_sent': []
                           }  # Информация о сложном предложении

        self.__SimpleSentence = {'word_comb': [], 'word': [], 'simp_sent_type': []
                                 }  # Инф о простом предложении

        self.__WordCombination = {'first_word_ind': [], 'word_comb_type': [],
                                  'main_word_ind': []
                                  }  # Инф о словосочетаниях

        self.__Word = {'gramm_class': [], 'flect_class': [], 'ending_len': [],
                       '4': [], '5': []}  # Инф о словах

    @property
    def Text(self):
        return self.__Text

    @Text.setter
    def Text(self, value):
        self.__Text = value

    @property
    def Sent(self):
        return self.__Sentence

    @Sent.setter
    def Sent(self, value):
        self.__Sentence = value

    @property
    def SimpSent(self):
        return self.__SimpleSentence

    @SimpSent.setter
    def SimpSent(self, value):
        self.__SimpleSentence = value

    @property
    def WordComb(self):
        return self.__WordCombination

    @WordComb.setter
    def WordComb(self, value):
        self.__WordCombination = value

    @property
    def Word(self):
        return self.__Word

    @Word.setter
    def Word(self, value):
        self.__Word = value

    def graphematic_to_json(self, filename):
        """
        Сохраняем результаты графематического анализа в json файл
        :return:
        """
        with open(filename, "w") as json_file:
            json.dump(self.__Text, json_file, indent=4, sort_keys=True)
