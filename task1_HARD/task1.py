import os
os.system('cls') #напоминаю что люблю когда всё чистенько :)

number = 12345.67  # указываю любое число

# преобразую число в его абсолютное значение (чтоб обработать отрицательные числа)
number = abs(number)

# тут иниализирую сумму цифр
sum_of_digits = 0

# Итерируются по каждой цифре числа
while number > 0:
    digit = number % 10  # последняя цифра числа
    sum_of_digits += digit  # добавлю цифру к сумме
    number //= 10  # удалю последнюю цифру числа

print(sum_of_digits)  # выводим сумму цифр
