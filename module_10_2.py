import time
import threading
class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.remainder_enemies = 100
        self.day = 0
    def run (self):
        print(f"{self.name}, на нас напали!")
        while self.remainder_enemies > 0:
            self.day += 1
            daily_defense = min(self.power, self.remainder_enemies)
            self.remainder_enemies -= daily_defense
            print(f"{self.name}, сражается {self.day} день(дня)..., осталось {self.remainder_enemies} воинов.")
            time.sleep(1)
        print(f"{self.name} одержал победу спустя {self.day} дней(дня)!")


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения
first_knight.start()
second_knight .start()

first_knight.join()
second_knight .join()

print("Все битвы закончились!")
