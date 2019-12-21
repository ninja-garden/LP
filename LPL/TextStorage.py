import json

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class TextStorage(metaclass=Singleton):
    def __init__(self):
        self._Text = {'text': None, 'num_words': 0, 'words_list': [],
                       'words_len': [], 'num_sents': None, 'sent_list': None,
                       'num_syms': None}  # Метаинформация о тексте

        self._Sentence = {'simp_sent_list': [], 'sent_type': [], 'first_simp_sent_ind': [],
                           'num_words_simp_sent': []
                           }  # Информация о сложном предложении

        self._SimpleSentence = {'word_comb': [], 'word': [], 'simp_sent_type': []
                                 }  # Инф о простом предложении

        self._WordCombination = {'first_word_ind': [], 'word_comb_type': [],
                                  'main_word_ind': []
                                  }  # Инф о словосочетаниях

        self._Word = {'gramm_class': [], 'flect_class': [], 'ending_len': [],
                       '4': [], '5': []}  # Инф о словах

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, value):
        self._Text = value

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
    def WordComb(self):
        return self._WordCombination

    @WordComb.setter
    def WordComb(self, value):
        self._WordCombination = value

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
