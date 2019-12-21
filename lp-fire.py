
""" CLI program for structuring texts """

import click
from LPL.TextStorage import TextStorage
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


if __name__ == '__main__':
    main()
