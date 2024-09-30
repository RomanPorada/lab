# завдання 1
# імпорти потрібних функцій
from math import atan, tan, log

# присвоєння змінній х початкового значення
x = 0.3
max_x = 3.5
h = 0.3

# виконання обчислень
while x  <= max_x:
    if x < 1:
        result = atan(1/x)
    elif 1 <= x < 3:
        result = tan(x + log(x, 4))
    elif x >= 3:
        result = 1 / (1 + log(x))
    print(f"result 1 = {result}")
    print(f"x = {x}")
    x += h
    x = x.__round__(2)

# завдання 2
# присвоєння значень змінних
n = 1
result_final = 0.0
result_curent = 0.0
x = -0.5
deviation = 0.001

# виклик циклів
while x <= 0:
    result_curent = (x ** n) / n
    result_final += result_curent
    while result_curent.__abs__() > deviation:
        result_curent = (x ** n) / n
        result_final += result_curent       
        n += 1
    result_final *= -1
    print(
        "x = " + x.__round__(3).__str__() 
        + " result = " + result_final.__round__(2).__str__()
        )
    result_curent = 0.0
    result_final = 0.0
    x += 0.05
    x = x.__round__(2)
    n = 1