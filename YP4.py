# Базовый класс Transport
class Transport:
    def __init__(self, brand, speed):
        self.brand = brand  # марка
        self.speed = speed  # скорость
    
    def move(self):
        print(f"Транспорт движется со скоростью {self.speed} км/ч")
    
    def __str__(self):
        return f"Транспорт: {self.brand}, Скорость: {self.speed}"

# Дочерний класс Car
class Car(Transport):
    def __init__(self, brand, speed, seats):
        super().__init__(brand, speed)
        self.seats = seats  # количество мест
    
    def honk(self):
        print("Бип бип!")  # гудок
    def move(self):
        print(f"Автомобиль {self.brand} едет со скоростью {self.speed} км/ч")
    def __str__(self):
        return f"Автомобиль: {self.brand}, Скорость: {self.speed}, Мест: {self.seats}"
    def __len__(self):
        return self.seats  # возвращает количество мест
    def __eq__(self, other):
        if isinstance(other, Car):
            return self.speed == other.speed  # сравнение по скорости
        return False
    def __add__(self, other):
        if isinstance(other, Car):  # Проверяем, что other - Car
            return self.speed + other.speed  # суммарная скорость
        return NotImplemented

# Дочерний класс Bike
class Bike(Transport):
    def __init__(self, brand, speed, type):
        super().__init__(brand, speed)
        self.type = type  # тип велосипеда
    def move(self):
        print(f"Велосипед {self.brand} едет со скоростью {self.speed} км/ч")
    def __str__(self):
        return f"Велосипед: {self.brand}, Скорость: {self.speed}, Тип: {self.type}"



transport = Transport("Generic", 50)  # базовый транспорт
car1 = Car("Semerka", 160, 4)         # авто 1
car2 = Car("Piatnashka", 150, 8)      # авто 2
bike = Bike("Trek", 20, "mountain")   # велосипед

print("Вывод объектов:")
print(transport)
print(car1)
print(car2)
print(bike)
print()  
# Проверка работы методов move()
transport.move()
car1.move()
car2.move()
bike.move()
print()  

print("Проверка метода honk() для автомобиля:") #honk
car1.honk()
print()  

print("Количество мест в car1:", len(car1)) #len(car)
print()  

print("Сравнение car1 == car2:", car1 == car2) #Сравнение 2 avto
print()  

print("Суммарная скорость car1 + car2:", car1 + car2) # Сложение 
print()  

print("Попытка сложить автомобиль и велосипед:") # Попытка (car1 + bike)
try:
    result = car1 + bike
    print("Суммарная скорость car1 + bike:", result)
except TypeError as e:
    print("Ошибка при сложении car1 + bike:", e)
print()  

# Создание списка объектов и вызов метода move() для каждого
vehicles = [transport, car1, car2, bike]
print("Вызов метода move() для всех объектов в списке:")
for vehicle in vehicles:
    vehicle.move()