class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    @property
    def celsius(self):
        return round(self._celsius,2)
    @celsius.setter
    def celsius(self, value):
        self._celsius = value
    @property
    def fahrenheit(self):
        return (self._celsius * 9 / 5) + 32
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5 / 9

temp = Temperature(25)
print(f"По цельсию: {temp.celsius}")
print(f"По фаренгейту: {temp.fahrenheit}")

temp.fahrenheit = 100
print(f"По цельсию: {temp.celsius}")
print(f"По фаренгейту: {temp.fahrenheit}")