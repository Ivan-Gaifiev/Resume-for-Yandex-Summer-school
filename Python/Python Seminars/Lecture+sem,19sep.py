#Циклы и условия
#if, else
# c=input()
# match c:
#     case "Russia":
#         print("moscow")

#следить за тем, чтобы не создавался бесконечный цикл

#for
#break and continue also work if loop for
# a=[[0]*5]*5
# print(a)

# a=10
# c=a+2
# b=300
# print(a is 10, b is 300)  #числа от -5 до 256 закэшированный при запуске программы

# моды для открытия файла: r, w, a,b
# 3 кавычки игнорируют символы переноса строки ''' 3 '''
# seek(offset) - сместить бегунок на место относительно начала файла
# tell() - скажи, на каком месте стоит бегунок
# read(10) прочитай первые 10 символов
# seek(tell()-num) - сдвинуться вперёд или назад относительно текущей позиции курсора

# for line in f:
#     print(line.strip())

# в множестве неповторяющиеся элементы
# pop возвращает любое значение из множества
# a|b - объединить множества, a&b - пересечь множества, a-b вычесть b из a, a^b - симметрическая разность двух множеств
# discard - Удаляет указанный элемент из множества, если он там присутствует.
# список изменяемый, кортеж - нет (не можем добавить в него элементы)


# SEMINAR
# from math import sqrt
# l=input().split()
# n=[]
# for el in l:
#     n.append(int(el))
# a,b,c=n[0],n[1],n[2]
# D=b**2-4*a*c
#
# if (a==0):
#     x=-c/b
#     print(x)
#
# if D<0:
#     print("no real roots")
# elif D==0:
#     x_1 = (-b + sqrt(D)) / (2 * a)
#     print(x_1)
# elif D>0:
#     x_1=(-b+sqrt(D))/(2*a)
#     x_2=(-b-sqrt(D))/(2*a)
#
# print(x_1, x_2)

# Майнинг, криптовалюта - числа
# блокчейн - база данных, последовательность операций в сети
# майнинг - подбор хэша таким оьразом, чтобы он был определённого вида. в хэше должны быть нули

# from math import sqrt
# for a in range (1,10):
#     for b in range (1,10):
#         for c in range (1,10):
#             D = b ** 2 - 4 * a * c
#             if D>0:
#                 x_1 = (-b + sqrt(D)) / (2 * a)
#                 x_2 = (-b - sqrt(D)) / (2 * a)
#                 if x_1==round(x_1) and x_2==round(x_2):
#                     print(x_1, x_2,a,b,c)
# делаем из введённого числа его представление в римских цифрах.
# I II V..X...L..50..C-100
# num=int(input())
# roman_num={'C':100,'XC':90,'L':50,'XL':40,'X':10, 'IX':9, 'V':5, 'IV':4, "I":1}
# roman=""
# for letter,value in roman_num.items():
#     while num>= value:
#         roman+=letter
#         num-=value
# print(roman)

