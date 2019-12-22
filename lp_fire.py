
""" CLI program for structuring texts """

import click
from LPL.TextStorage import TextStorage
from LPL.Semantic_analysis import Semantic_analysis
from LPL.Graphematic_analysis import Graphematic_analysis
from LPL.Morphological_analysis import Morphological_analysis

GRAPHEMATIC_FILE_NAME = 'graphematic.json'
MORPH_FILE_NAME = 'morph.json'
SSA_FILE_NAME = 'ssa.json'

def graphematic_analysis(text, storage):
    """
    Заполняем хранилище результатами графематического анализа
    :param text: исходный текст
    :param storage: объект хранилища
    :return:
    """
    ga = Graphematic_analysis(text)
    ga_result = {'text': text, 'num_words': ga.n_words, 'words_list': ga.tokenized_sentences,
                 'words_len': [], 'num_sents': len(ga.sentences), 'sent_list': ga.sentences,
                 'num_syms': sum(ga.len_sentences)}

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
    print()

def morph(text, storage):
    """
    Заполняем хранилище результатами морфологического анализа
    :param text: исходный текст
    :param storage: объект хранилища
    :return:
    """
    morph = Morphological_analysis()
    morph_res = [[morph.get_grammar_info(word) for word in sent] for sent in storage.Text['words_list']]
    print("МОРФОЛОГИЧЕСКИЙ АНАЛИЗ")
    print("======================================================")
    for i in range(len(morph_res)):
        print("Предложение №{}".format(i))
        print(morph_res[i])
    print("======================================================")
    storage.Morph = morph_res
    storage.morphology_to_json(MORPH_FILE_NAME)

def SSA(text, storage):
    """
    Заполняем хранилище результатами ССА
    :param text: исходный текст
    :param storage: объект хранилища
    :return:
    """
    ssa = Semantic_analysis()
    print("СЕМАНТИКО-СИНТАКСИЧЕСКИЙ АНАЛИЗ")
    print("======================================================")
    # Далее для каждого предложения
    for i, sent in enumerate(storage.Text["words_list"]):
        print("Предложение №{}".format(i))
        print("======================================================")
        print(sent)
        morf_klass = ssa.class_word(sent)
        print(morf_klass)
        # информация о словосочетаниях
        print("======================================================")
        print('Словосочетание | № перв.слв словосоч в предл. | Длина Словосоч | Тип словосоч | № главн. слова')
        morf = []
        coll_info = ssa.Collocations(morf_klass, morf)
        wrd_comb = storage.Word_combinations[i]
        for info in coll_info:
            print(info[4], info[0], info[1], info[2], info[3])
            wrd_comb.add_combination(first_word_ind=info[0], word_comb_type=info[2],
                                     main_word_ind=info[3], word_comb_len=info[1])

        # поиск индексов главных слов в словосочетаниях
        ind_m = ssa.Find_main_word(morf_klass)
        # получение предложения с подлежащим и сказуемым. Вывод индекса подл. и сказ.
        print("======================================================")
        print("Получение предложения с подлежащим и сказуемым, вывод подлежащего и сказуемого")
        try:
            s_p_sent, S, P = ssa.s_p(morf_klass, morf)
        except:
            pass
        # Добавляем результаты в хранилище
        sp_skel = {}
        sp_skel["s_p_sent"] = s_p_sent
        sp_skel["S"] = S
        sp_skel["P"] = P
        print(s_p_sent)
        print(S)
        print(P)
        print("======================================================")
        print("Скелет предложения")
        skel = ssa.skel_sent(s_p_sent, ind_m, S, P)
        sp_skel["skel"] = skel
        storage.SSA_sents.append(sp_skel)
        print(skel)
        print()
    storage.ssa_to_json(SSA_FILE_NAME)

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
    morph(text, storage)
    SSA(text, storage)


if __name__ == '__main__':
    main()
