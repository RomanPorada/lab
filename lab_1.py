# Створення змінної з назвою улюбленої марки машити та виведення її
car = "Alfa Romeo"

print(car)

# Присвоєння змінним значень True, False і виведення їх логічних операцій
is_student = True
is_teacher = False

print(f"and operanion = {is_student & is_teacher}")
print(f"or operation = {is_student | is_teacher}")
print(f"not is_student operation = {not is_student}")
print(f"not is_teacher operation = {not is_teacher}")
print(f"xor operation = {is_student ^ is_teacher}")

# Присвоєння змінним значень True, False і виведення логічної операції and
is_red = False
is_blue = True

print(f"and operation = {is_red & is_blue}")

# Імпортування потрібних функцій з бібліотеки math
from math import sqrt, sin, tan

# Присвоєння змінним необхідних значення
x = 0.712
y = 3.161

# Обчислення виразу та виведення результату
s = sqrt(x * y ** 2  + y * sin(x) + 142 * x ** 2  * y) + tan(x* y) - (142 * (y - x)) / 16.32

print(s)