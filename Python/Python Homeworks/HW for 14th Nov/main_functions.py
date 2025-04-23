import re


def create_dict(file):
    """
    Reads a file and creates a dictionary where the key is the line number
    and the value is a list of strings split by '/'

    :param file: path to the file
    :return: dict_lines — dictionary containing the lines from the file
    """
    dict_lines = {}
    num_line = 0
    with open(file, 'r', encoding='utf-8') as text_file:
        our_text = text_file.readlines()
        for lines in our_text:
            dict_lines[num_line] = lines.strip().split('/')
            num_line += 1
    return dict_lines


def check_syllables(line, expected_count, line_num, pattern, result):
    """
    Checks the number of syllables in a line and writes the result to a file.

    :param line: the line to check for syllables
    :param expected_count: the expected number of syllables
    :param line_num: the line number
    :param pattern: the pattern to search for syllables
    :param result: file object to write the result
    :return: True if the number of syllables matches, otherwise False
    """
    match = re.findall(pattern, line)
    if len(match) != expected_count:
        string = f"Not Haiku. In line {line_num} should be {expected_count} syllables, not {len(match)}"
        print(string, '\n')
        result.write(f"{string}\n\n")  # Write the line and result
        return False
    return True


def check_haiku(dict_lines, pattern):
    """
    Checks the lines for the Haiku format and writes the results to a file.

    :param dict_lines: dictionary of lines
    :param pattern: the pattern to search for syllables
    :return: None
    """
    with open('test_haiku.txt', 'w', encoding='utf-8') as result:
        for val in dict_lines.values():
            result.write(f"{'/'.join(val)}\n")  # Write the line in "line1/line2/line3" format

            # Check if the line consists of 3 parts
            if len(val) != 3:
                print('Not haiku. There must be 3 lines', '\n')
                result.write("Not haiku. There must be 3 lines\n\n")
            elif (check_syllables(val[0], 5, 1, pattern, result) and
                  check_syllables(val[1], 7, 2, pattern, result) and
                  check_syllables(val[2], 5, 3, pattern, result)):
                print("Haiku!", '\n')
                result.write("Haiku!\n\n")
