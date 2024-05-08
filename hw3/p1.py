import threading

value = 0 
thread_lock = threading.Lock()

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        global value 
        thread_lock.acquire(1)  
        value += 5 
        thread_lock.release()

thread1 = MyThread('A')
thread2 = MyThread('B')
thread3 = MyThread('C')
thread4 = MyThread('D')

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()


print("Value =", value)