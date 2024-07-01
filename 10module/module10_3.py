#import threading, lock
import threading
from threading import Thread, Lock
from time import sleep


class BankAccount:
    def __init__(self, amount=1000):
        self.amount = amount

    def deposit(self, amount):
        lock.acquire()
        self.amount += amount
        sleep(1)
        print(f'Deposited {amount}, new balance is {self.amount}')
        lock.release()


    def withdraw(self,amount):
        with lock:
            self.amount = self.amount - amount
            sleep(1)
            print(f'Withdrew  {amount}, new balance is {self.amount}')

def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)

def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)



lock = Lock()

account = BankAccount()
deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()