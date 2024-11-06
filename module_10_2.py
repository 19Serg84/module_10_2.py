import threading
import time

# Общее количество врагов
total_enemies = 100
# Создание блокировки для синхронизации доступа к общему ресурсу
lock = threading.Lock()

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        global total_enemies
        days = 0

        print(f"{self.name}, на нас напали!")

        while True:
            time.sleep(1)  # Ожидание 1 секунду
            days += 1
            with lock:
                total_enemies -= self.power
                remaining_enemies = max(total_enemies, 0)  # Не допускаем отрицательное количество врагов
                print(f"{self.name}, сражается {days} день(дня)..., осталось {remaining_enemies} воинов.")

                if remaining_enemies <= 0:
                    print(f"{self.name} одержал победу спустя {days} дней(дня)!")
                    break

# Создаем два рыцаря
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запускаем потоки
first_knight.start()
second_knight.start()

# Ожидаем завершения всех битв
first_knight.join()
second_knight.join()

print("Все битвы закончились!")