"""3. Паттерн «Строитель»
● Создайте класс Pizza, который содержит следующие
атрибуты: size, cheese, pepperoni, mushrooms, onions,
bacon.
● Создайте класс PizzaBuilder, который использует паттерн
«Строитель» для создания экземпляра Pizza. Этот класс
должен содержать методы для добавления каждого из
атрибутов Pizza.
● Создайте класс PizzaDirector, который принимает
экземпляр PizzaBuilder и содержит метод make_pizza,
который использует PizzaBuilder для создания Pizza."""

from dataclasses import dataclass, field  # импортируем библиотеку датаклассов


@dataclass
class Pizza:  # создаем класс пицца
    size: int = field(default=15)
    cheese: int = field(default=0)
    pepperoni: int = field(default=0)
    mushrooms: int = field(default=0)
    onions: int = field(default=0)
    bacon: int = field(default=0)


@dataclass
class PizzaBuilder:  # создаем класс сборки пиццы
    parts = []

    @property
    def product(self):
        self._product = Pizza()  # присваиваем полю класса элементы другого класса.
        product = self._product  # присваиваем поле в переменную
        return product

    def add_size(self, part):  # метод изменения размера пиццы
        self.product.size = part
        self.parts.append(f'размер {part}')

    def add_cheese(self, part):  # метод добавки сыра
        self.product.cheese = part
        self.parts.append(f'сыр {part}')

    def add_pepperoni(self, part):  # метод добавки пеперони
        self.product.pepperoni = part
        self.parts.append(f'Пеперони {part}')

    def add_mushrooms(self, part):  # метод добавки грибов
        self.product.mushrooms = part
        self.parts.append(f'Грибы {part}')

    def add_onions(self, part):  # метод добавки лука
        self.product.onions = part
        self.parts.append(f'лук {part}')

    def add_bacon(self, part):  # метод добавки бекона
        self.product.bacon = part
        self.parts.append(f'Бекон {part}')

    def list_parts(self):  # метод описания состава пиццы
        print(f"Сделанная пицца: {', '.join(self.parts)}", end="")


@dataclass
class PizzaDirector:  # создание класса директора пиццы

    _builder = None  # создание класса директора пиццы

    @property  # передаем в директора класс создания пиццы(геттер)
    def builder(self):
        return self._builder

    @builder.setter  # передаем в директора класс создания пиццы(сеттер)
    def builder(self, builder: PizzaBuilder):
        self._builder = builder

    def make_pizza(self, size, cheese, pepperoni, mushrooms, onions, bacon):  # метод создания пиццы
        self.builder.add_size(size)
        self.builder.add_cheese(cheese)
        self.builder.add_pepperoni(pepperoni)
        self.builder.add_mushrooms(mushrooms)
        self.builder.add_onions(onions)
        self.builder.add_bacon(bacon)
        self.builder.list_parts()


director = PizzaDirector()   # создаем объекта класса директор
builder = PizzaBuilder()    # создаем объекта класса создания пиццы
director.builder = builder  # вызываем метод билдер из класса директор

director.make_pizza(20, 5, 10, 1, 5, 6)

