from pymystem3 import Mystem
#!pip install pymorphy2
import pymorphy2
import re 
#!pip install pymystem3
#!pip install git+https://github.com/nlpub/pymystem3
#Функция нахождения словосочетаний по ключевым словам (на входе слова по классам)
def Collocations(sentence):
    separators = ['F','&','V','L','K']
    result = [[]]
    for sent in sentence:
        if sent in separators:
            result.append([sent])
            result.append([])
        else:
            result[-1].append(sent)
    i = 0
    while i < len(result):
        if len(result[i]) > 1:
            result[i] = tuple(result[i])
            i+=1
        elif len(result[i]) == 1:
            result[i] = 'I'
            i+=1
        else:
            del result[i]
    return result
#Функция определения типа словосочетания
"""Пока тут заглушка, всегда возвращается именное"""
def CollocationType(collocation):
    return 'N'
'''Пока определяет главное слово только в именном словосочетании'''
def find_the_main_word(collocation):
    if CollocationType(collocation) == 'N':
        if 'N' in collocation:
            return collocation.index('N') + 1
        else:
            return None
#Функция вывлда информации о совосочетаниях (принимает на вход результат функции Collocations)
def CollocationsInfo(collocations):
    collocations_info = [[1,len(collocations[0])]]
    for encoding in collocations[1:]:
        collocations_info.append([collocations_info[-1][0]+collocations_info[-1][1],len(encoding)])
    for i in range(len(collocations)):
        collocations_info[i].append(CollocationType(collocations[i]))
        collocations_info[i].append(find_the_main_word(collocations[i]))
    return [tuple(info) for info in collocations_info]

def class_word(word_list):
    dict_class = {'NOUN':'N',
                    'ADJF':'A',
                    'VERB':'V',
                    'PRTS':'K',
                    'INFN':'I',
                    'PRTF':'W',
                    'GRND':'D',
                    'NUMR':'O',
                    'ADVB':'Y',
                    'PREP':'F',
                    'CONJ':'&',
                    'INTJ':'!'}
    morph = pymorphy2.MorphAnalyzer()
    list_punctuation =['.',',','!','–','"','?','(',')','{','}','[',']']
    sens = [morph.parse(word)[0].tag.POS if not(word in list_punctuation) 
            else word  for word in word_list]
    for i,word in enumerate(word_list):
        if (sens[i]=='VERB')and(morph.parse(word)[0].tag.tense=='past'):
            sens[i] = 'L' 
    list_class = [dict_class.get(word) if not(str(word) in list_punctuation) and (word in dict_class.keys())
            else word  for word in sens]
    return list_class
