import threading
import queue
import time

class Customer:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Cafe:

    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables

    def customer_arrival(self):
        for i in range(1, 21):  # ограничение числа посетителей
                customer = Customer(i)
                print(f"Посетитель номер {i} прибыл")
                time.sleep(1)
                self.queue.put(customer)

    def serve_customer(self, customer):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f"Посетитель номер {customer.get_name()} ожидает свободный стол (помещение в очередь)")
                time.sleep(5)
                table.is_busy = False
                print(f"Посетитель номер {customer.get_name()} сел за стол {table.number} (начало обслуживания)")
                return print(f"Посетитель номер {customer.get_name()} покушал и ушёл (конец обслуживания)")



def customer_thread(cafe):
    while True:
        customer = cafe.queue.get()
        cafe.serve_customer(customer)
        cafe.queue.task_done()
        if cafe.queue.empty():
            break


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

cafe = Cafe(tables)

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

for _ in range(3):
    t = threading.Thread(target=customer_thread, args=(cafe,))
    t.start()

customer_arrival_thread.join()