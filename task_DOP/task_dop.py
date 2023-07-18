import os
os.system('cls')

import math

def all_divisors(number):
    divisors = []
    sqrt = int(math.sqrt(number))

    for i in range(1, sqrt + 1):
        if number % i == 0:
            divisors.append(i)
            if i != sqrt:
                divisors.append(number // i)

    return sorted(divisors)

# Примеры чисел
numbers = [23436, 190187200, 380457890232]

for number in numbers:
    divisors = all_divisors(number)
    print(f"Делители числа {number}: {divisors}")
