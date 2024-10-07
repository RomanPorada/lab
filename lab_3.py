import random

def generate_random_list(n, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(n)]

def sum(list):
    sum = 0
    for num in list:
        sum += num
    return sum


def min_value_to_balance(list):
    n = len(list)
    if n % 2 != 0:
        raise ValueError("Послідовність повинна мати парну кількість елементів")
    

    left_half = list[:n//2]
    right_half = list[n//2:]
    
    sum_left = sum(left_half)
    
    sum_right = sum(right_half)
    
    difference = abs(sum_left - sum_right)
    return difference * -1
    

n = int(input("Введіть значення довжини списку(воно має бути парним): "))
min_value = int(input("Введіть початок відрізка з якого буде формуватися список: "))
max_value = int(input("Введіть кінець відрізка з якого буде формуватися список: "))

# Генерація випадкового списку
random_list = generate_random_list(n, min_value, max_value)

# Виведення результатів
print("Випадкова послідовність:", random_list)
print("Мінімальне значення для балансування:", min_value_to_balance(random_list))

dic = {
    "yes": True,
    "no": False
}

del(dic["no"])
print(dic)
