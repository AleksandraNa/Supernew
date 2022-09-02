"""Игра угадай число. Компьютер сам загадывает и сам угадывает число"""

from itertools import count
import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    count = 0
    
    while True:
        count+=1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
        
    return(count)

def score_game(random_predict) -> int:
    
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    
    """
    
    count_ls = [] #список для сохранения попыток
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000)) # загадываем список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls)) # находим среднее количество попыток
    
    print(f"Ваш алгорит угадывает число за {score} количество попыток")
    return(score)

if __name__ == '_main_':
    
    #RUN

    score_game(random_predict)




