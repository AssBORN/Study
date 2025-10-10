text = "Программная инженерия"
vowels = "аеёиоуыэюя"
vowels_list = []

for char in text.lower():
    if char in vowels:
        if char not in vowels_list:
            vowels_list.append(char)

print("Текст:", text)
print("Найденные гласные:", vowels_list)
print("Количество гласных:", len(vowels_list))