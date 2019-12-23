import pandas as pd
import numpy as np
from tqdm import tqdm
import re
import random
import string


class Morphological_analysis:
    def __init__(self, path_to_flex="./ma_flex.uni", path_to_words="./ma_WORDS.uni", path_to_fk_gi="./table_fk_gi.uni"):
        """
             Создает объект класса Morphological_analysis.
             Валидирует корректность введенных путей.
             Валидирует корректность словарей.
             
             Аргументы:
                 path_to_flex (str): путь до КБС
                 path_to_words (str): путь до СКС
                 path_to_fk_gi (str): путь до ФКГИ
        """
        self.flex = self.read_txt(path_to_flex, ["word", "value"])
        self.words = self.read_txt(path_to_words, ["word", "value"])
        self.fk_gi = self.read_txt(path_to_fk_gi, ["class", "target", "ending"])

    def read_txt(self, file_name: str, cols: []) -> pd.DataFrame:
        """
            Считывает словари по переданным путям.
            Валидирует данные в словарях.
            При необходимости парсит данные сохраняя во временный файл.
            
            Аргументы:
                file_name (str): название словаря, который необходимо считать
                cols (list): список названий колонок, дефотно []
            
            Возвращает:
                считанный словарь в формате DataFrame
        """
        tmp = pd.read_csv(file_name, sep=" ", header=None, names=cols)
        if (tmp.isnull().values.any()):
            tmp = pd.read_csv(self.preprocess(file_name), sep=" ", names=cols)
        return tmp

    @staticmethod
    def format_string(string: str) -> str:
        """
            Статический метод.
            Парсит данные, приводя к виду, необходимому для дальнейшей работы.
            
            Аргументы:
                string (str): строка, предназначенная для парсинга
            
            Возвращает:
                строку в пригодном для работе формате
        """
        for i in range(len(string)):
            if(i < len(string) - 1 and i >= 1):
                if (string[i] == "/"
                    and not string[i - 1].isdigit()
                        and string[i+1].isdigit()):
                    return string[:i] + " /" + string[i+1:]

    def preprocess(self, path_to_file: str) -> str:
        """
            Осуществляет препроцессинг.
            Последовательно применяет функцию препроцессинга к элементам датафрейма.
            Сохраняет данные в файл формата csv.
            
            Аргументы:
                path_to_file (str): путь до файла для препроцессинга
            
            Возвращает:
                имя файла, в который сохраняются данные
        """
        tmp = pd.read_csv(path_to_file, sep="\n",
                          header=None, names=["unprocessed"])
        tmp["processed"] = tmp["unprocessed"].apply(self.format_string)
        tmp.drop("unprocessed", axis=1, inplace=True)
        name = self.randomString() + ".csv"
        tmp.to_csv(name, header=None, index=False)
        return name

    @staticmethod
    def randomString(stringLength: int = 10) -> str:
        """
            Статический метод.
            Создает рандомное название для временного файла.
            
            Аргументы:
                stringLength (int): длина создаваемой строки, дефолтно равна 10
            
            Возвращает:
                сгенерированную строку
        """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))

    def direct_entry(self, word: str) -> int:
        """
            Фнкция выполняет поиск анализируемого слова на полное его совпадение в словаре 
            СКС (ma_WORDS).
            
            Аргументы:
                word (str): анализируемое слово
            
            Возвращает:
                окончание и флективный класс либо None
        """
        try:
            rt = self.words[self.words['word'] == word].values[0]
            split = rt[1].split('/')
            end = rt[0][-int(split[1]):]
            if (split[1] == "00"):
                end = '+'
            fk = split[2]
        except:
            return None
        else:
            return [end, fk]

    def rev_entry(self, word: 'str') -> int:
        """
            Функция производит инверсию буквенного состава анализируемого слова и выполняет 
            поиск конечного буквосочетания анализируемого слова на наибольшее совпадение 
            с одним из элементов словаря КБС (ma_flex).
            
            Аргументы:
                word (str): анализируемое слово
            
            Возвращает:
                окончание, флективный класс и длину окончания либо None

        """
        if (word in string.punctuation):
            return None
        rev_word = ''.join(reversed(word))
        temp_w = rev_word
        df = self.flex
        while True:
            for w in df['word'].values:
                fw = re.match(temp_w, w)
                if fw:
                    temp_asd = df[df['word'] ==
                                  w]['value'].values[0].split('/')
                    temp_asd2 = df[df['word'] == w]['value'].values[0]
                    for i in range(len(temp_asd)):
                        temp_asd[i] = int(temp_asd[i])
                    temp_ret = temp_w[:temp_asd[0]]
                    if len(temp_ret) == 0:
                        temp_ret = '+'
                    return [''.join(reversed(temp_ret)), temp_asd[1], temp_asd2]
            if len(temp_w):
                temp_w = temp_w[:-1]
            else:
                break

    def get_grammar_info(self, word: str):
        """
            Функция определяет грамматическую информацию слова на основании информации о 
            флективном классе и окончании слова по словарю ФКГИ.

            Аргументы:
                word (str): слово, для которого необходимо получить грамматическую информацию
            
            Возвращает:
                строку, набор грамматической информации
        """
        info = self.direct_entry(word)
        df = self.fk_gi
        if (info == None):
            info = self.rev_entry(word)
        if (info != None and info):
            fk = info[1]
            ending = info[0]
            try:
                if int(fk) > 125:
                    return ''.join(f'00/{x}' for x in info[1:2])
                item = df[(df['class'] == int(fk)) & (df["ending"] == ending)]
                if item.empty:
                    return None
                temp_to_return = f'{info[2]}/'
                to_join = f"/".join(str(x) for x in item["target"].values)
                return temp_to_return + to_join
            except:
                return ''.join(f'00/{x}' for x in info[1:2])
        else:
            return None
