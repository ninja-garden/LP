import pymorphy2
import re
from .TextStorage import TextStorage

class Semantic_analysis:
    def Find_Collocations(self, sentence):
        '''Функция нахождения словосочетаний по ключевым словам 
        (на входе слова по классам)'''
        separators = ['F','&','V','L','K',',']
        posible_words = ['N','A','0','O','i','g','s','k','K','L','V','F','h','M','I']
        result = [[]]
        for sent in sentence:
            if (sent in separators) or not(sent in posible_words):
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
                if not(result[i][0] in ['.',',']):
                    result[i] = 'I'
                else:
                    result[i] = result[i][0]
                i+=1
            else:
                del result[i]
        return result


    def CollocationType(self, collocation):
        '''Функция определения типа словосочетания'''
        NA = ['N','A','0','O','i','g','s','k']
        VA = ['K','L','V','F','h','M','I']
        for word_type in collocation:
            if word_type in NA:
                return 'NA'
            elif word_type in VA:
                return 'VA'


    def find_the_main_word(self, collocation):
        if len(collocation) == 1:
            return 1
        if self.CollocationType(collocation) == 'NA':
            if 'N' in collocation:
                return collocation.index('N') + 1
        elif self.CollocationType(collocation) == 'VA':
            if 'K' in collocation:
                return collocation.index('K') + 1
            elif 'L' in collocation:
                return collocation.index('L') + 1
            elif 'V' in collocation:
                return collocation.index('V') + 1


    def CollocationsInfo(self, collocations):
        '''Функция вывода информации о совосочетаниях
        (принимает на вход результат функции Collocations)'''
        collocations_info = [[1,len(collocations[0])]]
        for encoding in collocations[1:]:
            
            collocations_info.append([collocations_info[-1][0]+collocations_info[-1][1],len(encoding)])
        for i in range(len(collocations)):
            collocations_info[i].append(self.CollocationType(collocations[i]))
            collocations_info[i].append(self.find_the_main_word(collocations[i]))
            collocations_info[i].append(collocations[i])
        k = 0 
        while k < len(collocations_info):
            if collocations_info[k][1] == 1:
                del collocations_info[k]
            else:
                k+=1
        return [tuple(info) for info in collocations_info]


    def Collocations(self, sent, morf):
        '''функция информация по словосочетаниям'''
        colloc = self.Find_Collocations(sent)
        colloc_info = self.CollocationsInfo(colloc)
        for info in colloc_info:
            print('словосочетание:',info[4])
            print('№ первого слова словосочетания в предложении:',info[0])
            print('длинна словосочетания:', info[1])
            print('Тип словосочетания:', info[2])
            print('номер главного слова:',info[3])
            print()
        return colloc_info


    def class_word(self, word_list):
        '''функция определения класса слов'''
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
                        'NPRO':'i',
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


    def Find_main_word(self, sent):
        '''функция нахождения главных слов в словосочетаниях'''
        coll_info = self.CollocationsInfo(self.Find_Collocations(sent))
        result = []
        for info in coll_info:
            result.append(info[0]+info[3]-2)
        return result


    def find_all_N_morf_info(self, sent, morf):
        main_N = self.Find_main_word(sent)
        result = [(sent[N],N,morf[N]) for N in main_N]
        return result

    def find_all_KLV_morf_info(self, sent, morf):
        result = []
        for i in range(len(sent)):
            if sent[i] in ['K', 'L', 'V']:
                result.append((sent[i], i, morf[i]))
        return result


    #3 и далее. вторая равна, 0 у N,  3 у V
    def equal(self, N, KLV):
        N_morf = N[2].split('/')[2:]
        KLV_morf = KLV[2].split('/')[2:]
        for morf_N_i in N_morf:
            for morf_KLV_i in KLV_morf:
                if KLV[0]=='V' and (morf_N_i[1]==morf_KLV_i[1]) and (morf_N_i[-1]=='0')and(morf_KLV_i[-1]=='3'):
                    return True
                elif (KLV[0] in ['K','L']) and (morf_N_i[:2]==morf_KLV_i[:2]):
                    return True
        return False



    def s_p(self, sent,morf):
        '''функция определения подлежащего и сказуемого'''
        ind,ind_P=None,None
        sent1=sent.copy()
        if 'i' in sent:
            ind = sent.index('i')
            if ('V' in sent):
                ind_P = sent.index('V')
            elif('K' in sent):
                ind_P = sent.index('K')
            elif('L' in sent[ind:]):
                ind_P = sent.index('L')  
            sent1[ind]='S'
            sent1[ind_P]='P'
            return (sent1,ind,ind_P)
        possible_SP=[]
        all_N = self.find_all_N_morf_info(sent, morf)
        all_KLV = self.find_all_KLV_morf_info(sent, morf)
        for N in all_N:
            for KLV in all_KLV:
                if self.equal(N,KLV):
                    possible_SP.append((N[1],KLV[1]))
        true_sp = False
        for SP in possible_SP:
            if SP[0]<SP[1]:
                true_sp = True
        if true_sp:
            i = 0
            while i < len(possible_SP):
                if possible_SP[i][0]>possible_SP[i][1]:
                    del possible_SP[i]
                else:
                    i+=1
        possible_SP[0][0]
        sent1[possible_SP[0][0]]='S'
        sent1[possible_SP[0][1]]='P'
        return (sent1,possible_SP[0][0],possible_SP[0][1])
        #return possible_SP


    def skel_sent(self, sent_sp, ind_main, S,P):
        '''функция определения скелета предложения'''
        sent = sent_sp.copy()
        for i,k in enumerate(sent):
            if not((k =='F') or (i in ind_main+[S,P])or k in[',','.','–',':',';']):
                sent[i] = None
        return sent

    def storage_interface(self, sent, TextStorage):
        morf_class = self.class_word(sent)
        colloc = self.Find_Collocations(morf_class)
        colloc_info = self.CollocationsInfo(colloc)
        first_word_ind = [info[0] for info in colloc_info]
        word_comb_type = [info[2] for info in colloc_info]
        main_word_ind = [info[3] for info in colloc_info]
        return {'first_word_ind':first_word_ind, 'word_comb_type':word_comb_type, 'main_word_ind':main_word_ind}

