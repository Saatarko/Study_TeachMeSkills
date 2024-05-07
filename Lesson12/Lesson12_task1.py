"""1. Класс «Товар» содержит следующие закрытые поля:
● Название товара
● Название магазина, в котором подаётся товар
● Стоимость товара в рублях
Класс «Склад» содержит закрытый массив товаров.
Обеспечить следующие возможности:
● Вывод информации о товаре со склада по индексу
● Вывод информации о товаре со склада по имени товара
● Сортировка товаров по названию, по магазину и по цене
● Перегруженная операция сложения товаров по цене"""

from dataclasses import dataclass    # добавляем библиотеку dataclass
from typing import List   # добавляем метод List из  библиотеки typing
import operator           # добавляем библиотеку operator


@dataclass        # Объявляем класс - датакласом
class Product:    # добавляем класс товаров
    __name: str         # Объявляем закрытые поля
    __store_name: str
    __price: int

    @property                # свойс-во property для доступа к закрытым полям. это геттер(получает значение)
    def name(self):
        return self.__name

    @name.setter   # свойс-во property для доступа к закрытым полям. это сеттер(передает значение)
    def name(self, name):
        self.__name = name

    @property  # свойс-во property для доступа к закрытым полям. это геттер(получает значение)
    def store_name(self):
        return self.__store_name

    @store_name.setter  # свойс-во property для доступа к закрытым полям. это сеттер(передает значение)
    def store_name(self, store_name):
        self.__store_name = store_name

    @property    # свойс-во property для доступа к закрытым полям. это геттер(получает значение)
    def price(self):
        return self.__price

    @price.setter   # свойс-во property для доступа к закрытым полям. это сеттер(передает значение)
    def price(self, price):
        self.__price = price

    def __repr__(self):   # метод для отображения данных
        return f'{self.name}  магазина {self.store_name} по цене {self.price}'

    def __add__(self, other):    # перегрузка метода сложения
        return self.price + other

    def __radd__(self, other):   # доп метод чтобы сложение работало в любом порядке (т.е а+б и б+а)
        return self.__add__(other)


@dataclass(order=True)   # Объявляем класс Магазина как датакласс
class Store:
    __list: List[Product]  # закрытый атрибут в виде списка продуктов

    @property    # свойс-во property для доступа к закрытым полям. это геттер(получает значение)
    def list(self):
        return self.__list

    @list.setter   # свойс-во property для доступа к закрытым полям. это сеттер(передает значение)
    def list(self, temp_list):
        self.__list = temp_list

    def __repr__(self):    # метод для отображения объекта
        temp = len(self.list)
        temp_list = [f'{self.list[i].name}  магазина {self.list[i].store_name} по цене {self.list[i].price}\n'
                     for i in range(temp)]
        set_str = 'На складе есть: ' + ' '.join(temp_list)
        return set_str

    def sorted(self, sort_field):  # метод для сортировки списка с экземплярами класса (по любому из полей)
        if sort_field == 'name':
            print(f'Итог сортировки по имени: {sorted(self.__list, key=operator.attrgetter("name"))}')
        elif sort_field == 'store_name':
            print(f'Итог сортировки по названию магазина: {sorted(self.__list, key=operator.attrgetter("store_name"))}')
        elif sort_field == 'price':
            print(f'Итог сортировки по цене: {sorted(self.__list, key=operator.attrgetter("price"))}')

    def __getitem__(self, item):   # метод упрощения поиска по индексу
        return self.list[item]

    def get_by_value(self, value):  # метод для поиска по значению
        for i in self.list:
            f = operator.attrgetter('name')
            if f(i) == value:
                return i


def get_sum():   # функция для сложения цен элементов склада
    c = 0
    for i in my_store.list:
        c += i

    return c


zrill = Product('zrill', '21Vek', 500)     # создание элементов класса товаров
teapot = Product('Teapot', 'Electosila', 500)
dildo = Product('dildo', 'Sexshop', 150)
pan = Product('pan', '21Vek', 26)

my_store = Store([zrill, teapot, dildo, pan])  # создание элемента класса склада

print(my_store[0])     # Вывод данных по индексу
print(my_store[1])
print(my_store[2])
print(f'{my_store[3]}\n')


code_goods = my_store.get_by_value('Teapot')  # Вывод данных по имени товара
print(f'Поиск по имени товара: {code_goods}\n')


my_store.sorted('name')    # Вывод сортировок
my_store.sorted('store_name')
my_store.sorted('price')
print('\n')


print(f'Сумма цен всех товаров на складе будет {get_sum()}')    # Вывод общей суммы
