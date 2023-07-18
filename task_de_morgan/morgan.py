# ВОЗМОЖНО НЕ ВЕРНО, НО ПОПЫТКА НЕ ПЫТКА!

import os
os.system('cls') #напоминаю что люблю когда всё чистенько :)

import random
import time

# проверка истинности утверждения
def check_truth(X, Y, Z):
    return not (X or Y or Z) == (not X and not Y and not Z)

# генерация случайного количества предикатов и их значений
def generate_predicates():
    num_predicates = random.randint(3, 15)
    predicates = [bool(random.getrandbits(1)) for _ in range(num_predicates)]
    return predicates

# проверка истинности утверждения и засекание времени выполнения
def run_tests():
    start_time = time.time()

    for _ in range(100):
        predicates = generate_predicates()
        X, Y, Z = predicates[:3]

        result = check_truth(X, Y, Z)

    end_time = time.time()
    total_time = end_time - start_time

    return total_time

# Запуск тестов и вывод времени выполнения
execution_time = run_tests()
print("Total execution time:", execution_time, "seconds")
