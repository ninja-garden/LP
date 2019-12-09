class TextStorage():
    
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.inst = super(TextStorage, self).__new__(self)
        return self.inst
    
    def __init__(self):

        
        self._Text = { 'raw_text': None ,'num_words' : 15 , 'words_list' : [],
                        'words_len': [], 'num_sents':None, 'sent_list':None,
                     'simpSent_list':[],'first_simpSent_idx':[],'num_words_simpSent':[],
                     'num_syms':None}   # Метаинформация о тексте
        
        self._Sentence = {} 
        
        self._SimpleSentence = {}
        
        self._WordCombination = {}
        
        self._Word = {}

    
    @property  # getter
    def Text(self): 
        print("getter method called")   
        return self._Text

    
    @Text.setter #setter
    def Text(self, value,a):   
        self._Text[a] = value
    
            
s = TextStorage()
print("Object created", s)
