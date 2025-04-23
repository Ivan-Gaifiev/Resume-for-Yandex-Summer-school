import logging
import time
from multiprocessing import Process as pr

logger = logging.getLogger(__name__)
logging.basicConfig(filename = "log.txt", level = logging.WARNING,
                    format = '[%(asctime)s] {%(pathname)s:%(linena)d %(levelname)s - %(message)s')

def division():
# процедура спрашивает у пользователя число и выводит 1 делённое на него
    try:
        number = int(input("enter the num: "))
        res = 1/number
        print(res)
    # except (ZeroDivisionError, ValueError):  #сначала пишем специфичные исключения, а потом обычный except, чтобы ловил всё остальное
    #     print("Try smth instead 0 and use only numbers")
    # else:
    #     print("You are a grate divider!")
    # finally:
    #     print("something happend")

    except:
        logger.warning("Wrong input")
    else:
        logger.info("everything works")
    finally:
        logger.debug("Done")

# for i in range(10):
#     division()

import threading

count = 0

def hundred():
    res=1
    for i in range(1,10000000):
        res*=i
    print(res)
def hundred():
    for _ in range (101):
        global count
        print(count)
        count+=1
        time.sleep(1)

def hundred1():
    for _ in range(0,101, 2):
        global count
        print(count)
        count+=1
        time.sleep(2)

def greet(name):
    print('hello: ', name)


if __name__ == '__main__':
    t1 = threading.Thread(target=hundred, daemon=True)
    t2 = threading.Thread(target=hundred, daemon=True)
    # t1 = pr(target=hundred)
    # t2 = pr(target=hundred)
    # t3 = pr(target=hundred)
    # t4 = pr(target=hundred)
    # t5 = pr(target=hundred)
    # t6 = pr(target=hundred)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    # t3.start()
    # t4.start()
    # t3.join()
    # t4.join()
    # t5.start()
    # t6.start()
    # t5.join()
    # t6.join()



