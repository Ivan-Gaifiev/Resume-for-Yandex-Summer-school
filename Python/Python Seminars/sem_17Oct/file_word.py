def read_dict(file_name):
    '''
    Функция, считывающая слова из принятого файла и заносящая их в список
    :param file_name: строка, имя файла, где лежат слова из словаря
    :return: список слов из принятого словаря-файла
    '''
    with open(file_name) as f:
        list_words=f.read().split("\n")
    return list_words