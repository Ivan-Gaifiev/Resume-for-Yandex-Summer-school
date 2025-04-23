# GENERATOR OF PASSWORDS
import random, string

# Initialization of some helpful variables
let_to_dig_dict = {'i': 1, 'f': 4, 'o': 0, 's': 2, 't': 3, 'g': 5, 'c': 6, 'w': 7, 'p': 8,
                   'a': 9}  # dictionary for 4th question
special_symbols = list("""!"#$%&'()*+,-./:;<=>?@[]^_{|}~`""")  # list for 3rd question
diff_reg, digits, spec_symbols, let_to_dig = '', '', '', ''  # variables where we save user's answers to 4 questions
questions = ["Should I use different letter case (y/n)? ", "Should I use digits (y/n)? ",
             "Should I use special symbols (y/n)? ", "Should I substitute some letters with digits (y/n)? "]
user_answers = [diff_reg, digits, spec_symbols, let_to_dig]

# User's input
num_passwords = int(input("How many passwords do you want? "))
num_symbols = int(input("How many symbols in your password? "))
for question in range(4):  # asking 4 questions and putting answers into the list 'user_answer'
    print(questions[question])
    while True:  # fool-test
        user_answers[question] = input().lower()
        if user_answers[question] == 'y' or user_answers[question] == 'n':
            break
        else:
            print('You are only allowed to answer by using "y" or "n"')
            continue


# Function that initializes password with numbers+letters or only letters (according to what the user answered)
def initializing_password(num_symbols, ls_answers):
    password = [0] * num_symbols

    if ls_answers[1] == 'y':  # initialization with random numbers and letters with random cases on random positions
        num_rand_letters = random.randint(1, round(num_symbols * 0.6))  # random number of letters
        letter_positions = random.sample(range(num_symbols), num_rand_letters)  # unique random positions for letters
        for i in range(num_symbols):
            if i in letter_positions:
                password[i] = random.choice(string.ascii_letters)
            else:
                password[i] = str(random.randint(0, 9))

    else:  # initialization with random letters
        for i in range(len(password)):
            password[i] = random.choice(string.ascii_letters)

    return password


# Function that changes the initialized password according to user's answers to 1st, 3rd and 4th questions
def make_password(password, ls_answers):
    if ls_answers[2] == 'y':
        num_sp_symb = random.randint(1, round(len(password) * 0.2))  # random number of special symbols
        special_positions = random.sample(range(len(password)), num_sp_symb)  # unique positions for special symbols
        for pos in special_positions:
            password[pos] = random.choice(special_symbols)

    if ls_answers[3] == 'y':
        for i in range(len(password)):  # substituting letters from the dictionary with digits
            if password[i].lower() in let_to_dig_dict.keys():
                password[i] = str(let_to_dig_dict[password[i].lower()])

    if ls_answers[0] == 'n':
        return ''.join(password).lower()  # bringing all letters to one case
    return ''.join(password)  # returning created password as a string


# Main part where we launch the functions as many times as number of passwords user entered
for i in range(num_passwords):
    password = initializing_password(num_symbols, user_answers)
    result = make_password(password, user_answers)
    print(result)
