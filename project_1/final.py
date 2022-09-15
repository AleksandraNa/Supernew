import random

number = random.randint(1, 100) # загадываем число в пределах от 1 до 100
count = 0 # количество попыток, за которое компьютер угадает число
min1 = 1 # минимально возможное число
max1 = 101 # максимально возможное число
average_count = 0 # среднее число попыток угадывания за 1 цикл
number_of_counts = 0 # количество циклов

while number_of_counts < 1000:
    count += 1
    mid = (min1 + max1) // 2 # компьютер пробует угадать среднее число
    if mid > number: # если загаданное число меньше,
        max1 = mid # среднее число становится максимальным
    elif mid < number: # если загаданное число больше,
        min1 = mid # среднее становится минимальным
    else:
        number_of_counts += 1 
        average_count = average_count + count # складываем общее количество попыток
        number = random.randint(1, 100) # выбираем новое число для угадывания
        count = 0
        min1 = 1
        max1 = 101

average_count = average_count // 1000 # среднее число попыток угадывания за 1 цикл
print(f"Выполнено 1000 раз, среднее число попыток угадывания {average_count}")