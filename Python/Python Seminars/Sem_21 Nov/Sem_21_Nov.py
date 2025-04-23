"""
Класс, осуществляющий шифрование текста. текст - номер букв
"""
class Text:
    def __init__(self):
        self.alph = list(' abcdefghijklmnopqrstuvwxyz')
    def encrypt(self, string):
        stri = list(string.lower())
        res=''
        for i in range(len(stri)):
            res += f'{self.alph.index(stri[i]):02}'

        return res

    def decrypt(self, string):
        stri = list(string)
        list_s = []
        for i in range(0, len(stri), 2):
            char = stri[i] + stri[i+1]
            list_s.append(char)
        for j in range(len(list_s)):
            list_s[j] = self.alph[int(list_s[j])]

        return ''.join(list_s)

class Cesar(Text):
    def __init__(self, key):
        super().__init__()
        self.key = key
    def encrypt(self, string):
        res = ""
        stri = list(string.lower())
        for i in range(len(stri)):

            cript = self.alph.index(stri[i]) + self.key
            res += f'{self.alph[cript]}'
        return res
    def decrypt(self, string):
        res=''
        stri = list(string)
        for i in range(len(stri)):
            cript = (self.alph.index(stri[i]) - self.key) % len(self.alph)
            res += f'{self.alph[cript]}'
        return res


a = Cesar(3)
w = a.encrypt('Pack my box with five dozen liquor jugs')
print(w)
f = a.decrypt(w)
print(f)

