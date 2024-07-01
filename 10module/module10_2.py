from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, skill:int):
        super().__init__()
        self.name = name
        self.skill = skill

    def run(self):
        count_of_daty = 1
        for i in range(0,100, self.skill):
            if i == 0:
                print (f'{self.name}, , на нас напали!')
                continue
            print(f' {self.name} сражается {count_of_daty} дней(дня)... осталось {100 - i} воинов')
            sleep(5)
            count_of_daty += 1
        print(f'{self.name} одержал победу спустя {count_of_daty} дней')


knight1 = Knight("Sir Lancelot", 10) # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20) # Высокий уровень умения
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print('Все битвы закончились!')
