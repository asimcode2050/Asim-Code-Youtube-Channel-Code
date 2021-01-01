import threading
import time
import os
from threading import Thread
from random import randint
threadLock = threading.Lock()
class ThreadDemoClass(Thread):
    def __init__(self,name,duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration
    def run(self):
        threadLock.acquire()
        print("*** "+self.name+ " running, belong to processID "+ str(os.getpid())+"\n" )
        time.sleep(self.duration)
        print("*** "+self.name+" is over\n")
        threadLock.release()
def main():
    st_time = time.time()
    th1 = ThreadDemoClass("Thread#1",randint(1,10))
    th2 = ThreadDemoClass("Thread#2",randint(1,10))
    th3 = ThreadDemoClass("Thread#3",randint(1,10))
    th1.start()
    th2.start()
    th3.start()
    th1.join()
    th2.join()
    th3.join()
    print("End")
    print("-- @@@ %s seconds -- @@ " % (time.time() - st_time))
if __name__=="__main__":
    main()
