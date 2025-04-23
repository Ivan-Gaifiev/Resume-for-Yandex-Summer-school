import sys
import time
import pyttsx3, chime  # libraries for sound output when timer finishes
import colorama as c  # library for colourful text in output
c.init()


def which_time(list_time):
    """
    This function counts how many seconds timer will work.
    :param list_time: value of dict_time, the list contains numbers (even positions) and units of measurement (odd pos.)
    :return: number of seconds timer will work
    """
    overall_seconds = 0
    for i in range(0, len(list_time) - 1, 2):  # iterating through even indexes
        # check if next element second/minute/hour or something else (in this case program stops due to the wrong input)
        if 'sec' in list_time[i + 1]:
            overall_seconds += float(list_time[i])
        elif 'min' in list_time[i + 1]:
            overall_seconds += float(list_time[i]) * 60
        elif 'hour' in list_time[i + 1]:
            overall_seconds += float(list_time[i]) * 3600
        else:
            print(c.Fore.RED + 'Incorrect input of units of measurement' + c.Style.RESET_ALL)
            sys.exit()
    return int(overall_seconds)


def func_timer_state(num_seconds, timer_id):
    """
    This function prints numbers of seconds timer left to work and turns on the sound when the timer finished working
    :param num_seconds: number of seconds timer will work
    :param timer_id: number of timer user launched at this moment
    :return:
    """
    for i in range(num_seconds):
        print(c.Fore.GREEN + f"\r{num_seconds} seconds left before the end of the timer #{timer_id}" + c.Style.RESET_ALL, end="")
        # I use \r to update seconds in one line
        num_seconds -= 1
        time.sleep(1)  # wait exactly 1 second before updating
    print(c.Fore.YELLOW + f"\nDin-don, the timer #{timer_id} has finished!" + c.Style.RESET_ALL, '\n')
    engine = pyttsx3.init()
    chime.success()
    engine.say(f"Таймер номер {timer_id} звенит дзинь-дзинь-дзинь")
    try:
        engine.runAndWait()
    except RuntimeError:
        print(c.Fore.RED + "The sound couldn't appear as some timers finished their work almost at the same time"
              + c.Style.RESET_ALL)
