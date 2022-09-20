# Игра: Угадай число

## Оглавление  
[1. Описание проекта](https://github.com/AleksandraNa/Supernew/blob/main/project_1/README.md#Описание-проекта)  
[2. Какой кейс решаем?](https://github.com/AleksandraNa/Supernew/blob/main/project_1/README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](https://github.com/AleksandraNa/Supernew/blob/main/project_1/README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/AleksandraNa/Supernew/blob/main/project_1/README.md#Этапы-работы-над-проектом)  
[5. Результат](https://github.com/AleksandraNa/Supernew/blob/main/project_1/README.md#Результат)    
[6. Выводы](https://github.com/AleksandraNa/Supernew/blob/main/project_1/README.md#Выводы) 

### Описание проекта    
Угадать загаданное компьютером число от 1 до 100 менее чем за 20 попыток.

:arrow_up:[к оглавлению](https://github.com/AleksandraNa/Supernew/blob/main/project_1/README.md#Оглавление)


### Какой кейс решаем?    
Нужно написать программу, которая угадывает число от 1 до 100 за минимальное число попыток

**Условия соревнования:**  
- Компьютер загадывает целое число от 1 до 100 и его угадывает. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**     
Учимся писать хороший код на python


### Этапы работы над проектом  
В ходе реализации проекта была написана программа, которая брала среднее значение в диапазоне от 1 до 100, затем сравнивала среднее значение с загаданным числом. Получив результат больше загаданное число или меньше среднего значения, программа брала среднее значение в диапазоне от 1 до 50 или от 51 до 100 и т.д.
Далее угадывание кода проходило 1000 раз, после чего вычислялось среднее число попыток угадывания.
([код] https://github.com/AleksandraNa/Supernew/blob/main/project_1/final_game.py)

:arrow_up:[к оглавлению](https://github.com/AleksandraNa/Supernew/blob/main/project_1/README.md#Оглавление)


### Результаты:  
По [результатам опробирования](https://github.com/AleksandraNa/Supernew/blob/main/project_1/final_game.ipynb):
Среднее число попыток угадывания кода значительно меньше поставленной цели 20 попыток и составило только 5 попыток.

:arrow_up:[к оглавлению](https://github.com/AleksandraNa/Supernew/blob/main/project_1/README.md#Оглавление)


### Выводы:  
Данный код является успешным, так как не длинный, легко читаемый и решает поставленную задачу.

:arrow_up:[к оглавлению](https://github.com/AleksandraNa/Supernew/blob/main/project_1/README.md#Оглавление)