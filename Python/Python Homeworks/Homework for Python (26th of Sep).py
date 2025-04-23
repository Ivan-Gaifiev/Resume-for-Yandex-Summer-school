import time  # To display the text with a delay

f = open('akinator.txt')  # Picture of Akinator made with ASCII symbols
for line in f:
    print(line, end="")
    time.sleep(0.1)
print('\n')
f.close()

# Greeting part of script
print("Oh, hello, dear traveler!", '\n')
time.sleep(0.8)
print('I, Great Akinator, already feel your thought.')
time.sleep(1.4)
print('You have guessed a number, and I am ready to guess it with the precision of a wizard.')
time.sleep(2.6)
print("Let's get started!", '\n')
time.sleep(1.4)

# Main part with calculations
add_part, middle = 500, 500  # variables to calculate middle values
for quest_num in range(11):
    print('Tell me, wise friend, is your number greater or equal than '+str(middle)+'?', end='\n')
    if quest_num == 0: print('Use "y" as "yes" and "n" as "no"')
    user_ans = input().lower()
    if quest_num == 10:  # Ending part with guessed number
        print('Hmm... So be it!')
        time.sleep(0.6)
        print('I already see your number, like a clear sky over the desert!')
        time.sleep(2.6)
        print("It's in front of me... and it's "+str(round(middle))+"!", '\n')
        time.sleep(2)
        print("Surprised? Of course I'm never wrong!")
        time.sleep(1.5)
        print("Come with new riddles, I will always be here, ready to solve them.")
        time.sleep(3)
        print("Good luck, dear friend!")

    while (user_ans != 'y' and user_ans != 'n'):  # Fool test)
        print('Please use only "y" as "yes" and "n" as "no"','\n')
        user_ans = input().lower()

    if (user_ans == 'y'): # if user answered 'yes', guessed number greater than the middle
        add_part = add_part / 2
        middle += add_part
    else:
        add_part = add_part / 2
        middle -= add_part  # if user answered 'no', guessed number smaller than the middle