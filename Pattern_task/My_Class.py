from abc import ABC, abstractmethod  # добавляем абстраткный метод
from dataclasses import dataclass, field  # импортируем библиотеку датаклассов
from datetime import datetime


@dataclass
class Materials:
    bandages: int = field(default=0)
    sterilization: int = field(default=0)
    napkins: int = field(default=0)
    syringe: int = field(default=0)
    anesthetic: int = field(default=0)
    hypnotic: int = field(default=0)
    chip: int = field(default=0)
    anthelmintic: int = field(default=0)
    rabies_vaccinations: int = field(default=0)


@dataclass
class ProcedureAndMaterialLink(Materials):

    def __init__(self, name, bandages, sterilization, napkins, syringe, anesthetic, hypnotic, chip, anthelmintic,
                 rabies_vaccinations):
        self.name = name
        self.bandages = bandages
        self.sterilization = sterilization
        self.napkins = napkins
        self.syringe = syringe
        self.anesthetic = anesthetic
        self.hypnotic = hypnotic
        self.chip = chip
        self.anthelmintic = anthelmintic
        self.rabies_vaccinations = rabies_vaccinations


chipping = ProcedureAndMaterialLink('Чипирование', 0, 1, 1, 0,
                                    0, 0, 1, 0, 0)
deworming = ProcedureAndMaterialLink('Дегельминизация', 0, 1, 1, 0,
                                     0, 0, 0, 1, 0)
ultrasound = ProcedureAndMaterialLink('УЗИ', 0, 1, 1, 0, 0,
                                      0, 1, 0, 0)
x_ray = ProcedureAndMaterialLink('Рентген', 0, 1, 1, 0, 0,
                                 0, 1, 0, 0)
preliminary_examination = ProcedureAndMaterialLink('Предварительный осмотр', 0, 1,
                                                   1, 0, 0, 0, 1,
                                                   1, 1)
sterilization = ProcedureAndMaterialLink('Стерелизация', 5, 3, 1, 0,
                                         1, 0, 0, 0, 0)
operation = ProcedureAndMaterialLink('Операции', 5, 5, 3, 2, 1,
                                     0, 0, 0, 0)


@dataclass
class ProcedureBuilder:
    procedure_list = []

    def add_chipping(self):
        self.procedure_list.append(chipping)
        print('')

    def add_deworming(self):
        self.procedure_list.append(deworming)

    def add_ultrasound(self):
        self.procedure_list.append(ultrasound)

    def add_x_ray(self):
        self.procedure_list.append(x_ray)

    def add_preliminary_examination(self):
        self.procedure_list.append(preliminary_examination)

    def add_sterilization(self):
        self.procedure_list.append(sterilization)

    def add_operation(self):
        self.procedure_list.append(operation)


@dataclass
class Client:
    first_name: str
    phone: str
    address: str


@dataclass
class Employee:
    employee: str
    last_name: str
    profession: str


@dataclass
class Order(Client, Employee):
    procedure_list = []
    price: int
    date: datetime

    _builder = None  # создание класса директора пиццы

    @property  # передаем в директора класс создания пиццы(геттер)
    def builder(self):
        return self._builder

    @builder.setter  # передаем в директора класс создания пиццы(сеттер)
    def builder(self, builder: ProcedureBuilder):
        self._builder = builder

    def create_order(self, name, phone, address, last_name, profession, procedure_list, price, date):
        self.first_name = name
        self.phone = phone
        self.address = address
        self.last_name = last_name
        self.profession = profession
        self.price = price
        self.date = date
        self.procedure_list = procedure_list
        order = self.__class__()


@dataclass
class Animal:  # создаем класс животные
    name: str
    age: int

    @abstractmethod
    def do_some(self):  # создаем абтрактный метод
        pass


@dataclass
class Dog(Animal):  # создаем класс собак
    pass


@dataclass
class Cat(Animal):  # создаем класс котов
    pass


@dataclass
class AcceptanceAnimals:  # создаем класс AnimalFactory

    @staticmethod
    def create_animal(type_animal, name, age):  # создаем метод для добавления животных
        if type_animal == 'dog':
            animal = Dog(name, age)


        elif type_animal == 'cat':
            animal = Cat(name, age)
