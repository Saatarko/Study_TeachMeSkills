"""3. Паттерн «Фабричный метод»
● Создайте абстрактный класс Animal, у которого есть
абстрактный метод speak.
● Создайте классы Dog и Cat, которые наследуют от Animal
и реализуют метод speak.
● Создайте класс AnimalFactory, который использует
паттерн «Фабричный метод» для создания экземпляра
Animal. Этот класс должен иметь метод create_animal,
который принимает строку («dog» или «cat») и возвращает
соответствующий объект (Dog или Cat)"""

from abc import abstractmethod   # добавляем абстраткный метод
from dataclasses import dataclass  # импортируем библиотеку датаклассов


@dataclass
class Animal:   # создаем класс животные
    name: str
    age: int

    @abstractmethod
    def speak(self):  # создаем абтрактный метод разговора
        pass


@dataclass
class Dog(Animal):   # создаем класс собак

    def speak(self):   # перегружаем метод разговора для собак
        print('Гав-Гав')


@dataclass
class Cat(Animal):  # создаем класс котов

    def speak(self):  # перегружаем метод разговора для котов
        print('Мяу-мяу')


@dataclass
class AnimalFactory:   # создаем класс AnimalFactory

    @staticmethod
    def create_animal(type_animal, name, age):  # создаем метод для добавления животных
        if type_animal == 'dog':
            animal = Dog(name, age)
            print(f'Создан экземпляр класса собака по имени {animal.name} возраста {animal.age} год(лет)')
            print(f'И она умеет делать')
            animal.speak()
        elif type_animal == 'cat':
            animal = Cat(name, age)
            print(f'Создан экземпляр класса кот/кошка по имени {animal.name} возраста {animal.age} год(лет)')
            print(f'И он умеет делать')
            animal.speak()


AnimalFactory.create_animal('dog', 'Пит', 1)   # проверяем
print(f'\n')
AnimalFactory.create_animal('cat', 'Плюша', 2)
