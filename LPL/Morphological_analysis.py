import pandas as pd
import numpy as np
from tqdm import tqdm
import re
import random
import string

class Morphological_analysis:
    def __init__(self, path_to_flex="./ma_flex.uni", path_to_words="./ma_WORDS.uni", path_to_fk_gi="./table_fk_gi.uni"):
        """
             Создает объект класса Morphology, считывает словари
        """
        self.flex = self.read_txt(path_to_flex, ["word", "value"])
        self.words = self.read_txt(path_to_words, ["word", "value"])
        self.fk_gi = self.read_txt(path_to_fk_gi, ["class", "target","ending"])
        
    def read_txt(self, file_name: str, cols: []):
        tmp =  pd.read_csv(file_name, sep=" ", header=None, names=cols)
        if (tmp.isnull().values.any()):
            tmp = pd.read_csv(self.preprocess(file_name), sep=" ", names=cols)
        return tmp                              
            
    
    def format_string(self, string):
            for i in range(len(string)):
                if(i < len(string) - 1 and i >= 1):
                    if (string[i] == "/"\
                        and not string[i - 1].isdigit()\
                        and string[i+1].isdigit()):
                            return string[:i] + " /" + string[i+1:]
                            
    def preprocess(self, path_to_file):
        tmp = pd.read_csv(path_to_file, sep="\n", header=None, names=["unprocessed"])
        tmp["processed"] = tmp["unprocessed"].apply(self.format_string)
        tmp.drop("unprocessed", axis=1,inplace=True)
        name = self.randomString() +".csv"
        tmp.to_csv(name, header=None, index=False)
        return name
        
                              
    def randomString(self,stringLength=10):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))
                              
                              
    def direct_entry(self, word: str) -> int:
        try:
            rt = self.words[self.words['word'] == word].values[0]
            split = rt[1].split('/')
            end = rt[0][-int(split[1]):]
            if (split[1] == "00"):
                end = '+'
            fk = split[2]
        except:
            return 'NILL'
        else:
            return [end, fk]
        
    def rev_entry(self, word: 'str') -> int:
        if (word in string.punctuation):
            return None
        rev_word = ''.join(reversed(word))
        temp_w = rev_word
        df = self.flex
        while True:
            for w in df['word'].values:
                fw = re.match(temp_w, w)
                if fw:
                    temp_asd = df[df['word'] == w]['value'].values[0].split('/')
                    temp_asd2 = df[df['word'] == w]['value'].values[0]
                    for i in range(len(temp_asd)):
                        temp_asd[i] = int(temp_asd[i])
                    temp_ret = temp_w[:temp_asd[0]]
                    if len(temp_ret) == 0:
                        temp_ret = '+'
                    return [temp_ret, temp_asd[1], temp_asd2]
                    break
            if len(temp_w):
                temp_w = temp_w[:-1]
            else:
                break
                
    def get_grammar_info(self, word: str):
        info = self.direct_entry(word)
        df = self.fk_gi
        if (info == 'NILL'):
            info = self.rev_entry(word)
        if (info != 'NILL' and info):
            fk = info[1]
            ending = info[0]
            try:
                if int(fk) > 125:
                    return(''.join(f'00/{x}' for x in info[1:2]))
                item = df[(df['class'] == int(fk)) & (df["ending"] == ending)]
                if item.empty:
                    return None
                temp_to_return = f'{info[2]}/'
                to_join = f"/".join(str(x) for x in item["target"].values)
                return temp_to_return + to_join
            except:
                return None
        else:
            return None