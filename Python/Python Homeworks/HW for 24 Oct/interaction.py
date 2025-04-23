import string  # for using alphabet (type of the variable is string)


def user_input(dict_quest):
    """
    This function reads "key: value" step by step, prints it and asks user's answer.
    Then counts right and wrong answers and prints them.
    :param dict_quest: dictionary with questions as keys and lists of answers as values
    :return: number of right answers, number of wrong answers user chose
    """

    num_right = 0  # initializing variables-counters for right and wrong answers
    num_wrong = 0
    for question in dict_quest.keys():  # iterating by every key
        print(question)
        answers = ''
        for index in range(len(dict_quest[question]) - 1):  # goes through each elem of the list excepting the last one
            answers += string.ascii_lowercase[index] + '.' + dict_quest[question][index] + ', '
            # creating composite string with answers user will see
        print(answers)
        # Fool-test. User is only allowed to use letters that were already presented
        while True:
            user_answer = input('Enter the letter of the right answer to this question: ').lower()
            if user_answer not in list(string.ascii_lowercase)[:len(dict_quest[question])-1]:
                print('You are only allowed to choose any letter from presented answers!', '\n')
            else:
                break

        letter_to_ind = string.ascii_lowercase.index(user_answer)  # what index does the user's letter correspond to
        if dict_quest[question][letter_to_ind] == dict_quest[question][-1]:  # checks if user's choice == right answer
            num_right += 1
        else:
            num_wrong += 1
        print('\n')
    return num_right, num_wrong
