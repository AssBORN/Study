def is_simple(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def filter_simples(numbers):
    simples = []
    for num in numbers:
        if is_simple(num):
            simples.append(num)
    return simples

if __name__ == "__main__":
    numbers = list(range(1,101))
    simple_numbers = filter_simples(numbers)
    print("Исходный массив:", numbers)
    print("Простые числа:", simple_numbers)