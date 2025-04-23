#THIRD LESSON
# print("hello")
#commenting
#sep - separate sign between printed objects
#end - перевод на новую строку (если \n, то на новую строку, а если в кавычках пусто, то останется на первой строке, если какой-то знак, то он будет стоять в конце первой строки
#examples of end: 1) end="!\n", 2)end=""
# print("allocate: ", 123, 23, ",", sep="&", end="\n")
#хотим вывести служебный символ как обычный => ставим перед ним \
#другой способ - использовать два разных типа кавычек
# print("Second \" line")
# \t - табуляция, \n - новая строка,   \\ - выведется один слеш (второй) как обычный символ, а первый - служебный
#print(34*34/768)
# % - получить остаток при делении;  ** - pow; // - убрать дробную часть из ответа
#funcions:  min(), max(), abs(x)=(модуль x), pow(), round() = округление по мат правилам,
#input - вводить в консоль
#a=int(input())
#print(a)


#FOURTH LESSON
#variables
# num = 5.92
# word = 'Our digit is ' #there's no difference btw "" and ''
# boolean = True
# print(word,num)  #we can't do print(word+num), but.... print(word+str(num))
# del num #удалить переменную
# str_num = '5'
# print(word + str(5+int(str_num)))
# num1 = int(input('Enter first number:'))
# num2 = int(input("Enter second number:"))
# print(num1+num2, num1-num2, num1*num2, sep=" ")
# num1+=5 # *=, -=, %= etc   \\ - деление нацело без остатка, % - остаток от деления
# print(num1*word, sep="  ")
# val = 0
# val = True
# val = "Hi

# import math
# print(f'{math.factorial(12)/12**12:.8f}') # вывод дробного числа с 8 знаками после запятой


#FIFTH LESSON
#Conditional Constructions
# if 5==5:
#     print("yes")  #создан автоматический отступ

# isHappy = True
# boobs = 3
# if isHappy:   #same that   isHappy==True
#     print(1)
# if not isHappy:    #same that   isHappy==False
#     print(0)
# elif isHappy:   #additional condition - elif
#     print(2)
# else:
#     print(1)
# data = input()
# isHappy = True
# if isHappy and data=="3":  #and, or, not
#     print("0_0")
# else:
#     print("T_T")
#тернарный оператор (короткая версия условной конструкции):
# data = input()
# number = 5 if data == "3" else 0
# print(number)

# user_date = int(input("Enter your number:"))
# if user_date > 5:
#     print("user's number is bigger than 5")
#     if user_date > 6:
#         print("pon")
#следить за отступами и вложенными условиями!


#SIXTH LESSON
#Cycles (loops): for and while
# for i in range (6):  #begins with 0
#     print(i)
# for i in range (3, 6, 2):  #first - start value, second - end value, third - step
#     print(i)
# word = "Hello world"
# for i in word:  #outputting each letter of the variable word
#     print(i)

# word = "i like big boobs"
# ind = 1
# count = 0
# for i in word:  #use for if you wanna iterate smth
#     if i == "s":
#         count+=1
#         print("I found 's'. It is",ind, "'th  symbol in the string. In total", count, "'s' per line")
#     ind+=1

# isHasCar=True
# while isHasCar:
#     if input()=="Stop":
#         isHasCar=False

# for i in range(1, 11):
#     if i == 7:
#         break #leave the loop
#     elif i%3==0:
#         continue
#     print(i)

# found = None  #empty variable
# for i in "hello":
#     if i == "l":
#         found = True
#         break
# else:
#     found = False
# print(found)


#SEVENTH LESSON
#список (list)
# nums = [4, 9.3, "hello", False, [2,3,1]]
# nums[0]=32  #[indices]
# print(nums, nums[3], nums[-1],"\n", nums[2:], nums[1:3], nums[-1][2])

# numbers = [2,3,6]
# numbers.append(100)  #adds 100 to the end of the list
# numbers.insert(1,True)  #moves elemenet(according to the index) forward and adds new element to the stated position
# numbers.extend(reversed(sorted([5,2,9])))   #adds new elements to the end
# numbers.pop(2)  #removes element by index ([elements in total - value in()])mod(elements in total)
# numbers.remove(True)  #deletes element in ()
# print(numbers, numbers.count(5), len(numbers))   #true=1
# numbers.clear()  #removes all elements

# n = input("Enter length: ")
# numbers=[]
# for i in range (1, int(n)+1):
#     string="Enter element #"+str(i)+ " :"
#     numbers.append(input(string))
# print(numbers)

#generation lists
# a=[i*i for i in range (8)] #expresion before 'for'
# a=[int(i) for i in input().split()]


#EIGHTH LESSON
#string funcions, indices and slices
# word='word, length, slice, sigma'
# print(word[1])  #any string is list of chars
# print(len(word), word.count('o'), word.upper(), word.isupper(), word.islower(), word.capitalize())
# array = word.split(', ')
# print(word.find('w'), array[0])
# for el in range(len(array)):
#     array[el] = array[el].capitalize()
# result = ", ".join(array)  #gathers all elements of list and adds ", " between them making one general string
# print(result)

# word = 'monkey'
# print(word[2:5], word[2:-1:True])  #range - [from : to : step]
# lis = [2, 4,7.3, "dgg"]
# print(lis[1:4:2])
# print(lis[::2])   #we can also write only one or two of them like in this line


#NINETH LESSON
#Tuple (кортеж)
#we can't change elements in tuple.
#используются для передачи данных из сервера или на сервер. тем самым оптимизируют программу
# data = (4, 4 ,2, 7 ,[5,4,2] ,4 ,3.9, True, "lol")
#data[0]=5   impossible
# print(data[4:7:2])
# print(data.count(4), len(data), data)
# data2 = 2, True, "lps"  #also tuple
# data3 = (9)  #not a tuple, but (9,) is tuple
# print(data2)
# nums = [3, 6, 2]
# new_data = tuple(nums)
# word = tuple("Hello")
# print(new_data, word)
# data[4].append(19) #there may be mutable elements in immutable tuple
# print(data.__sizeof__(), list(data).__sizeof__())  #size of tuples is less than size of lists


#TENTH LESSON
#dict (словарь)
# test = {4:3,
#            5:2,
#            True:1,
#            False:0
#            }
# print(test[True])

# country = {'code': 'RU', 'name': 'Russia', 'population': 144, 'existence': True}  # key:value
# country2 = dict(code = 'RU', name = 'Russia')
# print(country2['name'])
# country.popitem()  #delete last elem
# country['name']=None
# print(country, type(country))
# print(country.keys(), country.values())
# print(country.items())
# for key, val in country.items():
#     print(key, ":", val)
# print(country.get('name'))

#dict is convenient for describing an object
# person={
#     'user_1':{
#         'first name':'John',
#         'last name':'Marley',
#         'age': 45,
#         'address' : ['Moscow c.', 'some str', 32],
#         'grades' : {'math' : 4, 'physics':3, 'literature':5}
#     },
#     'user_2':{}
# }
# print(person['user_1']['address'][1])


#ELEVENTH LESSON
#sequences: set, frozenset
#properties: all elements in random order and there aren't repeated elem-s
#use_case: we want to get some data from user, then we split the data and delete all repeated elements (making set out of list)
# data = set('hello')
# data2={5,7,4, 3,2}  #if we don't write keys, we make set
# #  data2[0] = 3  set is immutable, but:
# data2.add('kks')
# data2.update([3,2.5,True,'s'])
# data2.remove(3)
# data.pop()  #delete first elem
# print(data, type(data),"\n", data2, type(data2))
# data.clear()

# nums=set([3,1,7,3,1,9])
# print(nums)  #repeated elems are deleted

#frozen set = tuple + set  (we can't change elems inside frozen set. no add, no pop etc)
# a=frozenset([222,444,224,566,444, True, 'ssss'])
# print(a, type(a))
# b=a.difference([222,444])
# print(b)


#TWELTH LESSON
#creating and using functions
#function is like subprograms where we can put a code for often-repeating parts of pur program and launch this code|
#such approach allows us make our code shorter
# print()  #also a function
# def name_of_func():   #parameters in ()
#     print("hello", end="")
#     print("!")
#    # pass  -  #nothing will happen
# for i in range (7):
#     name_of_func()

# def name_of_func(word):
#     print(word, "!")
# name_of_func("hi")
# name_of_func(5)
# name_of_func(True)

# def sum(a, b):
#     print(a+b)
# sum(3,2)
# sum("H","i")
# sum(True, 5.3)

# def sum (a,b):
#     return a+b
# res = sum(4.3, 6)
# print(res)
# print(sum(int('4'), 9))

# def min(*a):  #function taking any number of parameters
# m=a[0]
# for x in a:
#     if m>x:
#         m=x
# return m

# nums1 = [2, 6, 3, 8, 4,1,-6,399,-6.000000000001,-6-2]
# minN = nums1[0]  #it is better not to use already reserved by python names (min, max)
# def find_min (nums1):
#     minN = nums1[0]
#     for el in range(len(nums1)):
#         if minN>=nums1[el]:
#             minN = nums1[el]
#     return minN
# print(find_min(nums1))

#lambda function - anonimous function
#lambda is shorter and more simple
# func = lambda x,y: x*y  #there's no need to write 'return'. it is already implied
# print(func(5,2))


#THIRTEENTH LESSON
#working with files
#before the work we must always open the file we're gonna use and close it where it's unnecessary
# file = open('test/text.txt', 'w')  #second parameter - way of opening the file (for reading, writing etc)
# file.write('Hello')  #if there is already text in the file, it will be deleted (otherwise - use 'a' to add text in file)
# file.write('!!!')   #no line break.  it is possible to do by additing \n to the end of first line
# file.close()

# data = input('Enter your text:')
# file = open('test/text.txt', 'a')
# file.write(data+'\n')
# file.close()

# file = open('test/text.txt', 'r')
# print(file.read(3))   #(number) - how many first characters would you like to output
# for line in file:
#     print(line, end="")
# file.close


#FOURTEENTH LESSON
#exceptions/ "try-except"
#we want our program continue working. even if there is an error, we want program show us this error but without stopping
# try:
#     x = int(input("Enter your number:")) + 5
#     print(x)
# except ValueError:
#     print("Enter a number instead!")

# x=0
# while x==0:
#     try:
#         x = int(input("Enter your number:")) + 5
#         print(x)
#         x+=1
#     except ValueError:
#         print("Enter a number instead!")

# try:
#     x=5/2
#     x=int(input())
# except ZeroDivisionError:
#     print("you're stupid damn")
# except ValueError:
#     print("nah")
# else:
#     print("if everything above is correct and no exceptions caught")
# finally:
#     print("this line always appears")


#FIFTEENTH LESSON
#Manager "with...as" for file work
# try:
#     file = open('text.txt','r')   #if 'r' and file doesn't exist = error, if 'w' then file will be created
#     file.read()
# except FileNotFoundError:
#     print('File not found')
# finally:
#     file.close()  #file isn't visible here
#with...as   opens and closes the file by itself (eben if an error appears)
# try:
#     with open('text.txt','r',encoding='utf-8') as file:   #using this construction allows us to not write finally block and it is already implied that file will be automatically closed
#         file.read()
# except FileNotFoundError:
#     print('File not found')


#SIXTEENTH LESSON
#modules and working with them
#module - set of files with new instruments  (module = library)
#pypi.org    for new modules
# import datetime as x  #after as we write pseudonim
#time.sleep(4) #stops our program for 4 seconds
# x.datetime.now()
# print(x.datetime.now().date())

#let's use system and os if we want to get some info from user
# import sys, os, platform, random, array, math
# print(sys.path)
# print(os.name)
# print(platform.system())

# from math import sqrt as s, ceil  #s is function sqrt() here,  ceil = round
# print(ceil(s(144)))

#how to create your own module:
#1) create new file and fill it with parameters and functions
#2) import our own module in main file
# import mymodule as my
# print(my.name)
# my.hello()
# from mymodule import add_three_numbers as add  #when we want to import concrete function
# print(add(3,7,2))

#find any module in pypi.ord that we need/  copy install phrase from there and paste it to local terminal
#now you are able to use installed module
# import cowsay
# cowsay.cow('Artem')


#SEVENTEENTH LESSON
#object-oriented programming: creating a class and object
#полиморфизм - когда есть общий функционал, но его можно переписать для каждого последующего наследника
#инкапсуляция - доступ к полю возможет только через спец методы доступа
#поле = набор переменных в классе
# class cat:
#     age = None
#     name = None
#     cost = None
#     isHappy = None
#     def set_data(self, age, name, cost, isHappy):
#         self.name = name
#         self.age=age
#         self.cost = cost
#         self.isHappy = isHappy
#     def get_data(self):
#         print(self.name, "age:", self.age, "Happy:", self.isHappy)
# cat1 = cat()
# cat1.set_data(5,"Marssik",2324.245,True)
# cat2=cat()
# cat2.set_data(3,"wwf",35,False)
# print(cat1.name, cat2.age)
# print(cat1.get_data(), cat2.get_data())


#EIGHTEENTH LESSON
#constructors and redefinition of methods
#we can complete some code right after creating an object
#using constructors we can set some values very quickly
# class cat:
#     age = None
#     name = None
#     cost = None
#     isHappy = None
#     def __init__(self, age=None, name=None, cost=None, isHappy=None):  #creating a constructor/  we can create an empty object with no exact values (moreover, put any exact value/sequence/set/string/list instead None)
#         self.set_data(age, name, cost, isHappy)
#         self.get_data()
#     def set_data(self, age=None, name=None, cost=None, isHappy = None):  #now we can set different number of parameters
#         self.name = name
#         self.age=age
#         self.cost = cost
#         self.isHappy = isHappy
#     def get_data(self):
#         print(self.name, "age:", self.age, "Happy:", self.isHappy)
# cat1 = cat(5,"Marssik",2324.245,True) #setting data when creating an object/
# cat1.set_data(2)
# cat2 = cat(3,"wwf",35,False)
# cat3=cat()


#NINETEENTH LESSON
#inheritance, encapsulation, polymorphism
# class Building:
#     __year = None  #__ - encapsulation/ very bad implementation in python
#     __city = None
#     def __init__(self, year, city):
#         self.year = year
#         self.city = city
#     def get_info(self):
#         print("Year:", self.year, "city:", self.city)
# class School(Building):  #there's no multi-inheritance in python
#     pupils = 0
#     def __init__(self, pupils, year, city):
#         self.pupils = pupils
#         super(School, self).__init__(year, city)   #чтобы передать данные в класс-конструктор/ функция вызывает класс-родитель
#     def get_info(self):
#         super().get_info()
#         print("Pupils:",self.pupils)
# class House(Building):
#     pass
# class Shop(Building):
#     pass
# school = School(100,2000, 'Moscow')
# school.__year = 6
# school.get_info()
# #print(school.__year)
# house = House(2000, 'Moscow')
# shop = Shop(2000, 'Moscow')


#TWENTIETH LESSON
#function decorators
#a decorator is a design pattern that allows you to modify the functionality of
#a function by wrapping it in another function
#decorators are like additional conditions (and not only them but any additional functional) that made in form of new function
# import webbrowser
# def validator(func):
#     def wrapper(url):
#         print("This text is before the funcion")
#         func(url)
#         print("after the func")
#     return wrapper   #without ()  !!
# @validator  #decorating
# def open_url(url):
#     webbrowser.open(url)
# open_url("https://youtube.com")

# import webbrowser
# def validator(func):
#     def wrapper(url):
#         if "." in url:
#             func(url)
#         else:
#             print("Wrong url")
#     return wrapper
# @validator   #it is our decorator
# def open_url(url):
#     webbrowser.open(url)
# open_url("https:youtubecom")


#STEPIK, Programming Python, 3.8 - 3.10
#libraries for data analysis
#NumPy
# import numpy as np
# a=array([2,3,4]) #only one type of data
# a.ndim  #размерность (одномерный, двумерный)
# a.shape  #разммеры массива (кол-во  строк, столбцов)
# b=array([(2,3),(2,9)])
# b.size #кол-во эл-ов
# z=zeros((3,2)) #массив с нулями на 3 строках и 2 столбцах
# arange(10,30,5) #out: [10,15,20,25]
# linspace(0,2,9) #9 - то, сколько точек на интервале между 0 и 2
# print(arange(8).reshape(2,2,2)) #поменять размерность
# s = np.array([2, 3])
# d = np.array([2, 6])
# print(s + d, s-d) #поэлементно
# print(s**2) #опреация для каждого элемента
# print(s<6)

#matplotlib
# from pylab import *
# a=linspace(0,5,10)
# b=a**2
# figure()
# plot(a,b,'r')
# xlabel('x')
# ylabel('y')
# show()
# fig=plt.figure()
# axes=fig.add_axes([0.1, 0.1, 0.8,0.8]) #left,bottom, width, height (range 0 to 1)
# axes.plot(a,b,'r')
# axes.set_xlabel('x')
# axes.set_ylabel('y')
# axes.set_title('title')