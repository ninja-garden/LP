""" Функции графематического анализа """
import nltk as nl
import codecs


def sent_tokenize(text):
    """
    Функция разбиения текста на предложения
    :param text: исходный текст
    :return: список предложений
    """
    return nl.sent_tokenize(text, language="russian")


def word_tokenize(sentense):
    """
    Функция разбиения предложения на слова
    :param sentense(str): исходный текст
    :return: список слов
    Пока все специальные символы - отдельные слова.
    Когда будут инструкции на эту тему исключим.
    """
    return nl.word_tokenize(sentense)


def main():
    print("Загружаем тестовый файл...")
    file = codecs.open("..\\test.txt", "r", "utf_8_sig")
    text = file.read()

    sentences = sent_tokenize(text)
    print("В тексте " + str(len(sentences)) + " предложения.")
    sen_example_idx = int(input("Введите номер предложения "))
    print(sentences[sen_example_idx])

    words = [word_tokenize(sent) for sent in sentences]
    print(words[sen_example_idx])


if __name__ == "__main__":
    main()
