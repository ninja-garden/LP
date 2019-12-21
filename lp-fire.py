
""" CLI program for structuring texts """

import click
from LPL.TextStorage import TextStorage
from LPL.Semantic_analysis import Semantic_analysis
from LPL.Graphematic_analysis import Graphematic_analysis

GRAPHEMATIC_FILE_NAME = 'graphematic.json'

def graphematic_analysis(text, storage):
    """
    Заполняем хранилище результатами графематического анализа
    :param text: исходный текст
    :param storage: объект хранилища
    :return:
    """
    ga = Graphematic_analysis(text)
    ga_result = {'text': text, 'num_words': ga.n_words, 'words_list': ga.tokenized_sentences,
     'words_len': [], 'num_sents': ga.len_sentences, 'sent_list': ga.sentences,
     'num_syms': None}

    print("ГРАФЕМАТИЧЕСКИЙ АНАЛИЗ")
    print("======================================================")
    print("Исходный текст:")
    print(text)
    print("======================================================")
    print("Число слов:")
    print(ga_result["num_words"])
    print("======================================================")
    print("Список слов:")
    print(ga_result["words_list"])
    print("======================================================")
    print("Число предложений:")
    print(ga_result["num_sents"])
    print("======================================================")
    print("Список предложений:")
    print(ga_result["sent_list"])
    storage.Text = ga_result
    storage.graphematic_to_json(filename=GRAPHEMATIC_FILE_NAME)
    print("======================================================")
    print("======================================================")
    print("Результат в файле {}".format(GRAPHEMATIC_FILE_NAME))

def SSA(text, storage):
    '''CLASS TEST'''
    sent2='Я устал от нашего жалкого существования .'
    sent2_lis=sent2.split()
    ssa = Semantic_analysis()
    morf_klass = ssa.class_word(sent2_lis)
    print(morf_klass)
    morf=[]
    print(ssa.Collocations(morf_klass, morf))
    #поиск индексов главных слов в словосочетаниях
    ind_m = ssa.Find_main_word(morf_klass)
    #получение предложения с подлежащим и сказуемым. Вывод индекса подл. и сказ.
    s_p_sent,S,P = ssa.s_p(morf_klass,morf)
    print(s_p_sent)
    print(ssa.skel_sent(s_p_sent, ind_m, S,P))

    s = 'Он идет гулять в парк'
    s2=s.split()
    morf_klass3 = ssa.class_word(s2)
    print("классы слов:\n"+' '.join(morf_klass3))
    #поиск индексов главных слов в словосочетаниях
    ind_m = ssa.Find_main_word(morf_klass)
    #получение предложения с подлежащим и сказуемым. Вывод индекса подл. и сказ.
    s_p_sent,S,P = ssa.s_p(morf_klass,morf)
    print("предложение с подлежащим:\n"+ " ".join(s_p_sent))
    print("скелет предложения:\n")
    print(ssa.skel_sent(s_p_sent, ind_m, S,P))


@click.command()
@click.argument('input_file')
def main(input_file):
    """
    Главная функция приложения
    :param input_file: исходный текстовый файл
    :return:
    """
    click.echo('CLI interface for language processor library')
    print(input_file)
    with open(input_file, encoding='utf_8_sig') as file:
        text = file.read()
    storage = TextStorage()
    graphematic_analysis(text, storage)
    SSA(text, storage)

if __name__ == '__main__':
    main()