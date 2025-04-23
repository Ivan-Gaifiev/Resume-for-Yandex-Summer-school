# initializing dictionary of letters and their prices
dict_letters = {1: ['a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r', 'а', "в", "е", "и", "н", "о", "р", "с", "т"],
                2: ['d', 'g', 'д', 'к', 'л', 'м', 'п', 'у'], 3: ['b', 'c', 'm', 'p', 'б', 'г', 'ё', 'ь', 'я'],
                4: ['f', 'h', 'v', 'w', 'y', 'й', 'ы'], 5: ['k', 'ж', 'з', 'х', 'ц', 'ч'], 8: ['j', 'x', 'ш', 'э', 'ю'],
                10: ['q', 'z', 'ф', 'щ', 'ъ']}

word_price = 0  # counter for summarising all letter prices in user's word
user_word = input('Enter your word: ').lower()

# first loop goes through keys of the dictionary (keys = prices of letters, letters in lists)
# second loop goes through letters of user's word
# condition checks if letter of user's word in the list connected to a certain number of points.
# If so, it adds price of the letter to the counter
for points in dict_letters:
    for letter in list(user_word):
        if letter in dict_letters[points]:
            word_price += points
print('Price of your word is', word_price)
