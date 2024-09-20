# імпорти потрібних функцій
from math import atan, tan, log

# присвоєння змінній х початкового значення
x = 0.3

# виконання обчислень
while x  <= 3.5:
    if x < 1:
        result = atan(1/x)
    elif 1 <= x < 3:
        result = tan(x + log(x, 4))
    elif x >= 3:
        result = 1 / (1 + log(x))
    print(f"result 1 = {result}")
    x += 0.3

# присвоєння значень змінних
n = 1
x = -0.5

# виконання обчислень
while x <= 0:
    result_2 = -1 * ((x ** n)/n)
    print(f"result 2 = {result_2.__round__(3)}")
    n += 1
    x += 0.05