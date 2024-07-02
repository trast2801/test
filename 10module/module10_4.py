import threading
import queue
from time import sleep

q = queue.Queue()
q2 = queue.Queue()


class Customer:
    def __init__(self, free_tables:int):
        self.q_customer = q2
        self.free_tables = free_tables

    # генерит количество посетителей равное количеству свободных столиков
    def generator_customer(self):
        for i in range(self.free_tables):
            #ss = 'Посетитель номер ' + str(i+1)+ ' создан'
            ss = ' (' + str(i + 1) + ' созданый) '
            print(ss)
            #sleep(2)
            self.q_customer.put(ss)

    #служебный метод для рповерки как вынимается из очереди
    def get_customer_from_queue(self):
        for i in range (self.q_customer.qsize()):
            print(self.q_customer.get())




class Table:
    def __init__(self, number = int, is_busy = False):
        self.number = number
        self.is_busy = is_busy
class Cafe:

    def __init__(self, tables):
        q = queue.Queue()
        self.tables = tables
        self.queue = q

    def customer_arrival(self):
        #self.stream_customer()
        custom = []
        for i in range(20): #ограничение числа посетителей
            custom.append(Customer(i))
        for i in range (q2.qsize()):
            ss = 'Посетитель номер ' + q2.get(i) + ' прибыл'
            print(ss)
            self.queue.put(ss)

            sleep(1)
    def stream_customer(self):
        count_of_free_tables = 0

        for i in tables: #считает число свободных мест, таким образом посетителей никогда не будет больше
                         # числа свободных столиков
            if i.is_busy == False:
                count_of_free_tables += 1
        print(f'Всего свободных столиков {count_of_free_tables}')
        if count_of_free_tables != 0:
            custom = []
            #for i in count_of_free_tables:
            #    custom.append(Customer(i))
            customer =  Customer(count_of_free_tables)
            customer_generator_thead = threading.Thread(target=customer.generator_customer())
            customer_generator_thead.start()
            customer_generator_thead.join()
        #customer.get_customer_from_queue()

    # служебный метод для контрля за числом посетителей, через обрезания кол-ва столиков
    def limit_tables(self):
        if len(self.tables) > 20:
            del self.tables[20:len(tables)]
        print('общее кол-во столов не привысит ', len(self.tables))


    def serve_customer(self, customer):
                pass

table1 = Table(1)
table2 = Table(2)
table3 = Table(3)

tables = [table1, table2, table3]
#for i in range (4,40):
#    tables.append(Table(i))
#print(tables)
# Инициализируем кафе
cafe = Cafe(tables)
#cafe.stream_customer()
cafe.customer_arrival()
cafe.limit_tables()