numbers = list(range(1,101))
simple = []

for num in numbers:
    if num == 1:
        continue
    is_simple = True
    if num == 2:
        is_simple = True
    elif num % 2 == 0:
        is_simple = False
    else:
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                is_simple = False
                break
    if is_simple:
        simple.append(num)
print("Исходный массив:", numbers)
print("Простые числа:",simple)