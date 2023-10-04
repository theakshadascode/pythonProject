from time import sleep
from threading import *


class Hello(Thread):  #need to add Thread  to make it multithreading

    def run(self):  #by default method was present so its working
        for i in range(5):
            print("hello")
            sleep(1) #sleep for 1 sec to run other thread
class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1=Hello()
t2=Hi()

t1.start()  #need to call start to start thread
sleep(0.5)  #for avoiding collise
t2.start()

t1.join()  #wait for t1 completion
t2.join()  #wait for t2 completion

print("Thanks for waiting Bye!")  #main thread will work
