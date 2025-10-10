def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 17

result = binary_search(numbers, target)

if result != -1:
    print(f"Элемент {target} найден на позиции {result}")
else:
    print(f"Элемент {target} не найден в массиве")