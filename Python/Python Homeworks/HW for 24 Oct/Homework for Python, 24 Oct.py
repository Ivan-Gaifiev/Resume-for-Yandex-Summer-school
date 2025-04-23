import interaction as inter
import work_with_file as wwf


def main():
    quest_ans_dict = wwf.read_file("Tests-questions.txt")
    # creating the dictionary, where the key is a question and the value is a list of answers
    num_r, num_w = inter.user_input(quest_ans_dict)
    print("Number of right answers =", num_r, ',', "Number of wrong answers =", num_w)
    # asking a user questions from the dictionary, counting his right and wrong answers and outputting them


main()
