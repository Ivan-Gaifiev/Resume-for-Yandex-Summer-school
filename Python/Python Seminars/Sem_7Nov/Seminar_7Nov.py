# import time
# import colorama
# from colorama import init
# from colorama import Fore, Back, Style, Cursor
# colorama.just_fix_windows_console()
#
# спрайт - отедльная картинка которая выводится
# спрайт лист - анимация
#
# s = r"\ | / -"
# a = s.split()
# print(a)
# i = 0
# while True:
#     pos = lambda y, x: Cursor.POS(x,y)
#     MINY = MINX = 10
#     print(a[i], end ='')
#     print('%s%s%s%s%s' % (pos(MINY, MINX), Fore.WHITE, Back.BLACK, Style.NORMAL, a[i]), end = '')
#     i += 1
#     time.sleep(1)
#     if i == len(a):
#         i = 0

import re

with open('file.txt','r') as f:
    text = f.read()
    textLine = ''.join(text)
    pattern = r'[+87]+[-(]?[0-9]{3}[-)]?[0-9]{3}[-]?[0-9]{2}[-]?[0-9]{2}\s'
    matches = re.findall(pattern, text)
    unique_nums = set(matches)
    for item in unique_nums:
        if item[-1] in {'\n', ' '}:
            t = item[:-1]
            print(t)
            item = t
        print(item)
    print(unique_nums)

