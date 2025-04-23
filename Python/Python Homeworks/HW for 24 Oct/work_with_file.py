def read_file(file_name):
    """
    This function reads lines in file_name and adds them to the dictionary
    First readline() puts this line as the key
    Second readline() creates the list with answers and adds it as the value for the previous key

    :param file_name: text file with questions and answers in correct format (read the instruction)
    :return: quest_ans_dict is the dictionary this function created using information from file_name
    """
    with open(file_name) as f:
        quest_ans_dict = {}
        while True:  # one iteration = two lines read (1 - question, 2 - answers)
            question = f.readline().strip()
            answers = list(f.readline().strip().split(', '))
            if not question:  # end of the text file
                break
            quest_ans_dict[question] = answers  # adds a value (list) by key (string)
        return quest_ans_dict
