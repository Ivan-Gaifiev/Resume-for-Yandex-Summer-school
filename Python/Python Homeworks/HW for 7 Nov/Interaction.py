import threading as t  # I use threads in my programs to launch timers in parallel
import sys
import work_with_seconds as w_w_s
import colorama as c # library for colourful text in output
c.init()


def inp_num_timers():
    """
    This function asks user to enter the number of timers he needs. After this the function
    checks if entered number between 1 and 10.
    :return: integer - number of timers the user wants to create
    """
    while True:  # infinite loop until user enters correct number
        num_timers = int(input("Enter the number of timers you need (from 1 to 10): "))
        if num_timers > 10 or num_timers < 1:  # check correctness
            print(c.Fore.RED + "Only in interval [1,10]!" + c.Style.RESET_ALL)  # if wrong
        else:
            break  # if correct
    return num_timers


def inp_time_work(num_timers):
    """
    This functions asks the user to enter the time (in natural language) each timer will work.
    Also, the function checks if entered parameters are correct
    :param: number of timers the user decided to create
    :return: dictionary with the correct time user entered to each timer
    """
    dict_time = {}  # create dictionary to keep entered parameters in usable format
    for n in range(1, num_timers + 1):  # iterate through all timers and ask the user to enter the time timers will work
        print(f"\nEnter the time you want the timer #{n} to work")
        print(c.Fore.CYAN + "Follow this format (write without quotes): 'number_(put point if your num is float) ",
              "\n", "unit_of_measurement_(in English: sec/min/hour) number another_unit' and so on ..." + c.Style.RESET_ALL, sep="")
        # create list with entered parameters and check if even elements are numbers
        while True:
            try:
                dict_time[n] = list(input("Enter here: ").lower().strip().split(' '))
                # key of the dictionary - number of the timer,
                # value - list with numbers (even positions) and units of measurement
                for i in range(0, len(dict_time[n]), 2):
                    float(dict_time[n][i])
                break  # if correct input
            except (TypeError, ValueError):
                print(c.Fore.RED + "Incorrect input, please try again."+ c.Style.RESET_ALL)  # if wrong input
    return dict_time


def timer_launch(dict_time):
    """
    This function suggests the user launching any timer he created.
    Thread realization allows to launch more than one timer in parallel
    The function also catches exceptions if the input is incorrect
    :param dict_time: dictionary with the correct time user entered to each timer
    """
    print("\nCome up with the number of the timer you want to launch " + "\n" + c.Fore.CYAN +
          "(you can start another one while the first one is running, "
          "but keep in mind that the timer will start, but it may not be visible in the console)" + c.Style.RESET_ALL)
    while True:
        while True:
            try:
                num_of_timer = int(input("Enter it here: "))
                # initializing new thread for the timer user decided to launch
                our_timer = t.Thread(target=w_w_s.func_timer_state, args=(w_w_s.which_time(dict_time[num_of_timer]), num_of_timer))
                our_timer.start()
                break
            # if the input is incorrect
            except (ValueError, KeyError):
                print(c.Fore.RED + "Invalid input. Please enter a valid integer." + c.Style.RESET_ALL)
            # if we want to quit the program
            except KeyboardInterrupt:
                print(c.Fore.CYAN + "Program finished" + c.Style.RESET_ALL, end="")
                sys.exit()


