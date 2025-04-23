# generator easy-remember passwords
#TODO:generator of passwords with parameters, parameter input
#DRY - dont repeat yourself
#code refactoring - причёсывание кода

from sem_17Oct import file_word as f_w, interation as i
import random as r

def many_passwords(num_passwords, num_words, list, diff_reg):
    for i in range(num_passwords):
        generator_password(num_words, list, diff_reg)
def generator_password(num_words, list, diff_reg):
    password=[]
    for i in range(num_words):
        password.append(r.choice(list))
    return password


def main():
    num_passwords = i.ask_number("How many passwords do you want? ")
    num_words = i.ask_number("How many words in the password? ")
    diff_reg = i.ask_answer("Include different case (y/n)? ")
    print(num_passwords, num_words, diff_reg)

    ls_words = f_w.read_dict('dictionary.txt')
    many_passwords(num_passwords, num_words,ls_words,diff_reg)

main()