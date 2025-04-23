# import time
# start_time = time.time()
# with open('file.txt', 'r', encoding="utf-8") as f:
#     d=""
#     for line in f:
#         d=d+line.lower().strip()+" "
# dict={}
# for i in d.split():
#     if i not in dict:
#         dict[i]=1
#         continue1
#     dict[i]+=1
# max_val=max(dict.values())
# max_keys=[k for k in dict.keys() if dict[k]==max_val]
# print(min(max_keys),dict[min(max_keys)])
#
# end_time = time.time()
# execution_time = end_time - start_time
# print(execution_time)


# import time
# start_time = time.time()
#
# arr=[]
# with open('file.txt','r',encoding="utf-8") as f:
#     s=f.read().strip().split('\n')
#     for i in s:
#         arr.append(i.split(';'))
# mat,ph,rus=0,0,0
# for i in arr:
#     print(sum([int(i[j]) for j in range(1,4)])/3)
#     mat,ph,rus=mat+int(i[1]),ph+int(i[2]),rus+int(i[3])
# print(mat/len(arr),ph/len(arr), rus/len(arr), sep=" ")
#
# end_time = time.time()
# execution_time = end_time - start_time
# print(execution_time)


# from math import pi
# print(pi * float(input()) *2)


# from sys import argv
# print(*argv[1::])


# import requests as r
# with open('file.txt','r') as f:
#     s=f.read().strip()
# a=r.get(s)
# print(len(a.text.splitlines()))


# import requests as r
# with open('file.txt') as f:
#     link=f.readline().strip()
#     s=''
#     while 'We' not in s:
#         s=r.get(link).text
#         link='https://stepik.org/media/attachments/course67/3.6.3/'+s
#     print(s)


# n, games = int(input()),[]
# for i in range(n): games.append(input().split(';'))
# num_games_team={}
# for i in range(n):
#     for j in[0,2]:
#         if games[i][j] not in num_games_team: num_games_team[games[i][j]]=1
#         else: num_games_team[games[i][j]]+=1
# table=list(num_games_team)
# for i in range(len(table)):
#     table[i]=[table[i]]
#     table[i].append(num_games_team[table[i][0]])
# for i in range(len(table)):
#     win,draw,defeat = 0,0,0
#     for j in range(len(games)):
#         if table[i][0] == games[j][0] and int(games[j][1])>int(games[j][3]) or table[i][0] == games[j][2] and int(games[j][3])>int(games[j][1]): win+=1
#         if table[i][0] == games[j][0] and int(games[j][1]) == int(games[j][3]) or table[i][0] == games[j][2] and int(games[j][3]) == int(games[j][1]): draw += 1
#         if table[i][0] == games[j][0] and int(games[j][1]) < int(games[j][3]) or table[i][0] == games[j][2] and int(games[j][3]) < int(games[j][1]): defeat += 1
#     table[i].extend([win,draw,defeat,win*3+draw])
# for i in range(len(table)):
#     s=str(table[i][0])+':'+str(table[i][1])
#     del table[i][1]
#     table[i][0]=s
#     print(*table[i])


# word,rule,cipher,decipher=(input().split()[0] for i in range(4))
# dict={word[i]:rule[i] for i in range(len(word))}
# print(''.join([dict[el] for el in cipher]))
# print(''.join([k for i in decipher for k in dict.keys() if dict[k]==i]))


# known=[input().lower() for i in range(int(input()))]
# text=[input().lower().split() for i in range(int(input()))]
# a=[]
# for i in range(len(text)):
#     for j in text[i]:
#         if j not in known: a.append(j)
# [print(i) for i in list(set(a))]


# a=[input().split() for i in range(int(input()))]
# dict = {'запад': 0, 'север':0, 'юг':0, 'восток':0}
# for i in a:
#     for k in dict.keys():
#         if i[0]==k: dict[k]+=int(i[1])
# print(dict['восток']-dict['запад'], dict['север']-dict['юг'])


# with open('file.txt') as f:
#     s=f.read().split()
#     dict={s[i]:[] for i in range(0,len(s),3)}
#     for j in range(0, len(s), 3):
#         dict[s[j]].append(int(s[j+2]))
#     for i in range(1, 12):
#         if str(i) in dict.keys():
#             print(i, sum(dict[str(i)])/len(dict[str(i)]))
#         else: print(i, "-")

