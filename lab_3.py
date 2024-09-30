import random

def generate_random_list(n, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(n)]

def min_value_to_balance(list):
    n = len(list)
    if n % 2 != 0:
        raise ValueError("Послідовність повинна мати парну кількість елементів")
    
    left_half = list[:n//2]
    right_half = list[n//2:]
    
    sum_left = 0
    for num in left_half:
        sum_left += num
    
    sum_right = 0
    for num in right_half:
        sum_right += num
    
    difference = abs(sum_left - sum_right)
    return difference * -1
    

n = 6
min_value = 1
max_value = 18

# Генерація випадкового списку
random_list = generate_random_list(n, min_value, max_value)

# Виведення результатів
print("Випадкова послідовність:", random_list)
print("Мінімальне значення для балансування:", min_value_to_balance(random_list))
