class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

vector1 = Vector(2, 3)
vector2 = Vector(1, 4)
vector3 = vector1 + vector2
print(f"Вектор с элементами {vector3.x,vector3.y}")