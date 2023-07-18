import os
os.system('cls')

S = 456  # Сумма задуманных чисел
P = 654  # Произведение задуманных чисел

# Находим задуманные числа X и Y
for X in range(1, S + 1):
    Y = S - X
    if X * Y == P:
        break

print(X, Y)  # Выводим задуманные числа X и Y