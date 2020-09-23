import threading
import time
import random

mutex = threading.Lock()

goldFishfed = False
s1 = threading.Semaphore()
s2 = threading.Semaphore()
def Person1():
    while True:
        # print('Person 1 starting') testing purposes
        global goldFishfed
        s1.acquire()
        workTime = random.randint(0, 10) # random number generator for random time spent for the rest of the day
        sleepTime = 10 - workTime
        time.sleep(workTime)
        if goldFishfed is False:
            goldFishfed = True
            print('Goldfish has been fed') # if goldfish has not been fed, feed him
            time.sleep(sleepTime)
            goldFishfed = False
        s1.release()


def Person2():
    while True:
        global goldFishfed
        s1.acquire()
        # print('Person 2 starting') testing print
        workTime = random.randint(0, 10) # random number generator for random time spent for the rest of the day
        sleepTime = 10 - workTime
        time.sleep(workTime)
        print(goldFishfed)
        if goldFishfed is False: # if goldfish has not been fed, feed him
            goldFishfed = True
            print('Goldfish has been fed')
            time.sleep(sleepTime)
            goldFishfed = False
        s1.release()

Thread1 = threading.Thread(target=Person1)
Thread2 = threading.Thread(target=Person2)
Thread1.start()
Thread2.start()
