import numbers
import random
from re import T

number = random.randint(1, 101)
count = 0
min1 = 1
max1 = 100

while True:
    count+=1
    mid = (min1 + max1) // 2
    if mid > number:
        max1 = mid
    elif mid < number:
        min1 = mid
    elif mid == number:
        print(f"Поздравляем, загаданное число {number}, за {count} попыток")
        break