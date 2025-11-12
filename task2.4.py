class MyList(list):
    def remove_duplicates(self):
        unique_list = list(set(self))
        self.clear()
        self.extend(unique_list)
        return self
    def get_average(self):
        if not self:
            return 0
        return sum(self) / len(self)

my_list = MyList([1, 2, 2, 3, 4, 4, 5])
print("Исходный список:", my_list)

my_list.append(6)
print("После append(6):", my_list)

my_list.remove_duplicates()
print("После remove_duplicates():", my_list)

average = my_list.get_average()
print("Среднее значение:", average)

print("Длина:", len(my_list))
print("Первый элемент:", my_list[0])