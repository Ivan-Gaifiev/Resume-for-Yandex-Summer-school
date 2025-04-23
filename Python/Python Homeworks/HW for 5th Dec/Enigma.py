import sys

conn_panel_d = {}
counts = [0, 0, 0]
rotors = []
reflector = {}
alphabet_rus = [" ", "А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С",
                    "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ь", "Ы", "Ъ", "Э", "Ю", "Я"] # 34 symbols (particularly for the reflector (as it requires even number)

# INTERACTION
def settings_cmd(rotors_settings, conn_panel):
    """
    This is an interaction function that takes 2 parameters either from
    or from python console or from command line.
    The function changes conn_panel_d as a global variable
    :return: string in format "AAA"
    """
    for i in range(len(conn_panel)):
        conn_panel_d[conn_panel[i]] = conn_panel[(i + 1) % 2]  # connecting panel swaps two any letters
    return rotors_settings


def my_text_cmd(text):
    """
    The function asks user for the text he wants to encrypt
    :return: string - text (symbol/word/sentence/text) user entered
    """
    return text


# WORK WITH FILE
def get_configurations():
    """
    The function takes configuration for rotors and the reflector from text file
    and writes it to global variables

    """
    with open("Machine configuration.txt", 'r', encoding="utf-8") as f:
        global rotors, reflector
        rotor1, rotor2, rotor3, = [], [], []
        lines = f.readlines()
        rotor1.append([lines[2][17:][i] for i in range(len(lines[2][17:])) if i % 2 == 0])
        rotor1.append([lines[3][13:][i] for i in range(len(lines[3][13:])) if i % 2 == 0])
        rotor2.append(rotor1[0])
        rotor2.append([lines[5][14:][i] for i in range(len(lines[5][14:])) if i % 2 == 0])
        rotor3.append(rotor1[0])
        rotor3.append([lines[7][13:][i] for i in range(len(lines[7][13:])) if i % 2 == 0])
        reflector = dict(zip(rotor1[0], reversed(rotor1[0])))  # dictionary where keys - letters in alphabet order and
        # values - letters in reverse order
        rotors = [rotor1, rotor2, rotor3]


# CALCULATING
def change_rot_sett(init_sett):
    """
    This function sets the beginning state of rotors
    :param init_sett: string in format "AAA"
    :return: rotors with correct start state (according to the user's beginning configuration)
    """
    global rotors
    for i in range(len(init_sett)):
        ind = alphabet_rus.index(init_sett[i])
        rotors[i][0] = [*rotors[i][0][ind:len(rotors[i][0])],
                        *rotors[i][0][0:ind]]  # Set the position of the input signal depending on the settings
    # return rotors


def lett_to_conn(letter):
    """
    This function changes the letter by passing it through the connecting panel
    :param letter: user's letter, string
    :return: string
    """
    global conn_panel_d
    if letter in conn_panel_d.keys():
        letter = conn_panel_d[letter]
    return letter  # letter after connecting panel


def rotors_f(letter):
    """
    In this function the process of rotors' work is implemented
    :param letter: string, letter after the panel
    :return:
    """
    global counts, alphabet_rus, rotors
    for i in range(len(rotors)):
        letter = rotors[i][1][rotors[i][0].index(letter)]  # letter after the first rotor
        if i == 0:
            rotors[0][1] = [*rotors[0][1][1:], rotors[0][1][0]]
            counts[0] += 1  # move first rotor to 1 step
            if counts[0] == len(alphabet_rus):  # if first rotor made full cycle
                counts[0] = 0
                rotors[1][1] = [*rotors[1][1][1:], rotors[1][1][0]]  # move second rotor
                counts[1] += 1

        elif i == 1:
            if counts[1] == len(alphabet_rus):  # if second rotor made full cycle
                counts[1] = 0
                rotors[2][1] = [*rotors[2][1][1:], rotors[2][1][0]]
                counts[2] += 1  # move third rotor
    return letter  # letter after the panel (forward path)


def reflector_f(reflect, letter):
    """
    The function changes the letter after rotors according the reflector settings
    :param reflect: dictionary with reflector settings
    :param letter: string, after rotors
    :return:
    """
    return reflect[letter]  # letter after the reflector


def back_signal(letter):
    """
    This function passes the letter after the reflector through the rotors in reverse order
    :param letter: string
    :return:
    """
    global rotors
    for i in range(2, -1, -1):
        letter = rotors[i][0][rotors[i][1].index(letter)]
    return alphabet_rus[(alphabet_rus.index(letter) + 1) % len(alphabet_rus)]  # letter after backward pass through rotors


def main(my_text, rot_sett, conn_panel):
    global rotors
    encrypted = ''
    rot_setts = settings_cmd(rot_sett, conn_panel)
    get_configurations()
    change_rot_sett(rot_setts)
    for letter in my_text:
        # passes each symbol of the text trough all the machine parts step by step and adds result letter to the string 'encrypted'
        letter = lett_to_conn(letter)
        letter = rotors_f(letter)
        letter = reflector_f(reflector, letter)
        letter = back_signal(letter)
        letter = lett_to_conn(letter)
        encrypted += letter
    return encrypted  # resulted text after Enigma




