"""Программа с классом Car. При инициализации объекта ему
должны задаваться атрибуты color, type и year. Реализовать
пять методов. Запуск автомобиля – выводит строку
«Автомобиль заведён». Отключение автомобиля – выводит
строку «Автомобиль заглушен». Методы для присвоения
автомобилю года выпуска, типа и цвета."""


class Car:  # Создаем класс Car
    default_color = 'Metallic'   # Задаем значения по умолчанию для ряда атрибутов
    default_type = 'Polo'
    default_year = 2005

    def __init__(self, color=default_color, car_type=default_type, year=default_year):  # Инициализуемся
        self.color = color   # присваиваем полученные данные атрибутам класса
        self.car_type = car_type
        self.year = year

    def starting_the_car(self):   # Метод завода авто
        print(f'Автомобиль {self.car_type} {self.year} года, {self.color} цвета заведен')

    def turning_off_the_car(self):  # Метод загрушения авто
        print(f'Автомобиль {self.car_type} {self.year} года, {self.color} цвета заглушен')

    def change_type(self, new_type):  # Метод смены типа авто
        self.car_type = new_type

    def change_year(self, new_year):  # Метод смены года авто
        self.year = new_year

    def change_color(self, new_color):  # Метод смены цвета авто
        self.color = new_color

    def __str__(self):
        return f"Автомобиль {self.car_type} {self.year} года, {self.color}"  # Строковое отображение


car1 = Car('red', 'Lexus', 2010)  # Создаем элементы класса
car2 = Car('white', 'Lada', 1986)
car3 = Car('green', 'Reno', 2022)
car4 = Car('black', 'Ford mustang', 1998)

print(car1)  # выводим на печать
print(car2)
print(car3)
print(car4)

car1.starting_the_car()     # вызываем наши методы
car2.turning_off_the_car()
car3.change_type('Mercedes')
car4.change_year('2050')
car1.change_color('green')

print(car1)   # выводим на печать уже с изменениями после методов
print(car2)
print(car3)
print(car4)
