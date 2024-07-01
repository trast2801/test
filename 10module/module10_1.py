from threading import Thread
from time import sleep

end = 10
string = 'abcdefghij'

def dig(end):
    for i in range(0, end):
        print(i)
        sleep(1)
def sym(b):
    for i in b:
        print (i)
        sleep(1)
thread1 = Thread(target=dig, args=(end,))
thread2 = Thread(target=sym, args=(string,))

thread1.start()
thread2.start()
thread1.join()
thread2.join()

