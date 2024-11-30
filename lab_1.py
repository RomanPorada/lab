car = "Alfa Romeo"

print(car)

is_student = True
is_teacher = False

print(f"and operanion = {is_student & is_teacher}")
print(f"or operation = {is_student | is_teacher}")
print(f"not is_student operation = {not is_student}")
print(f"not is_teacher operation = {not is_teacher}")
print(f"xor operation = {is_student ^ is_teacher}")

is_red = False
is_blue = True

print(f"and operation = {is_red & is_blue}")

from math import sqrt, sin, tan

x = 0.712
y = 3.161

s = sqrt(x * y ** 2  + y * sin(x) + 142 * x ** 2  * y) + tan(x* y) - (142 * (y - x)) / 16.32

print(s)
print(int(y))

str_1 = "Hello "
str_2 = "World"
delete_str = "l"
str_1 = str_1.replace(delete_str, "")

print(str_1 + str_2)
