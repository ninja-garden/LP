class TextStorage():
    
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(TextStorage, self).__new__(self)
        return self.instance
    
    def __init__(self):
        self.text = self.Text()
        self.sentence = self.Sentence()
        self.simplesent = self.SimpleSentence()
        self.wordcomb = self.WordCombination()
        self.word = self.Word()
        
    class Text:
        """
        Метаинформация о тексте
        """
        def __init__(self):
            """
            Инициализация метаинформации о тексте
            :param text:
            """
            self.num_words = None 
            self.words_list = []
            self.words_len = []
            self.num_sents = None
            self.sent_list = []
            self.simpSent_list = []
            self.first_simpSent_idx = []
            self.num_words_simpSent = []
            self.num_syms = None
    
    
    class Sentence:
        """
        Предложение
        """
        def __init__(self):
            pass
    
    
    class SimpleSentence(Sentence):
        """
        Простое предложение
        """
        def __init__(self):
            pass

    
    class WordCombination(Sentence):

        def __init__(self):
            pass
    
    
    class Word(Sentence):
        
        def __init__(self):
            pass
