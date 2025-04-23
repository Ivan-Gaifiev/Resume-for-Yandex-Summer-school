def ask_number(s):
    '''
    функция, которая задаёт вопрос пользователю с числовым целым результатом
    :param s: строка с формулировкой вопроса
    :return: целое число - ответ пользователя
    '''
    print(s)
    return int(input())

def ask_answer(question):
    '''
    Функция задаёт пользователю вопрос на да или нет
    :param question: строка с формулировкой вопроса
    :return: булл с ответом пользователя, где True - да, False - нет
    '''
    print(question)
    while True:
        d = input()
        if d.lower() == 'y' or d.lower() == 'n':
            if d == 'y':
                return True
            else:
                return False
        else:
            print("write y or n")
