"""Паттерн «Стратегия»
● Создайте класс Calculator, который использует разные
стратегии для выполнения математических операций.
● Создайте несколько классов, каждый реализует
определенную стратегию математической операции,
например, Addition, Subtraction, Multiplication, Division.
Каждый класс должен содержать метод execute, который
принимает два числа и выполняет соответствующую
операцию.
● Calculator должен иметь метод set_strategy, который
устанавливает текущую стратегию, и метод calculate,
который выполняет операцию с помощью текущей стратегии"""

from abc import ABC, abstractmethod  # добавляем абстраткный метод


class Strategy(ABC):  # создаем класс стратегии
    """
    Интерфейс Стратегии объявляет операции, общие для всех поддерживаемых версий
     алгоритма.

    Контекст использует этот интерфейс для вызова алгоритма, определённого
    Конкретными Стратегиями.
    """

    @abstractmethod   # добавляем абстрактный метод (который будет прообразом для других методов)
    def execute(self, a, b):
        pass


class Calculator:  # создаем класс калькулятора
    """
    определяет интерфейс
    """

    def __init__(self, strategy: Strategy):
        """
        принимает стратегию через конструктор, а также
        предоставляет сеттер для её изменения во время выполнения.
        """

        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        хранит ссылку на один из объектов Стратегии.  не знает
        конкретного класса стратегии.  должен работать со всеми стратегиями
        через интерфейс Стратегии.
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        """
        позволяет заменить объект Стратегии во время выполнения.
        """

        self._strategy = strategy

    @staticmethod
    def set_strategy(type_strategy, a, b):    # создаем статический метод для выбора класса для работы
        if type_strategy == 'Addition':
            data = Calculator(Addition())
            data.calculate(a, b)
        elif type_strategy == 'Subtraction':
            data = Calculator(Subtraction())
            data.calculate(a, b)
        elif type_strategy == 'Multiplication':
            data = Calculator(Multiplication())
            data.calculate(a, b)
        elif type_strategy == 'Division':
            data = Calculator(Division())
            data.calculate(a, b)

    def calculate(self, a, b):    # создаем метод для расчетов
        result = self._strategy.execute(a, b)
        print(result)


class Addition(Strategy):   # создаем класс для сложения
    def execute(self, a, b):
        result = a + b
        print('Метод сложения')
        return result


class Subtraction(Strategy):  # создаем класс для вычитания
    def execute(self, a, b):
        result = a - b
        print('Метод вычитания')
        return result


class Multiplication(Strategy):  # создаем класс для умножения
    def execute(self, a, b):
        result = a * b
        print('Метод умножения')
        return result


class Division(Strategy):   # создаем класс для деления
    def execute(self, a, b):
        try:
            result = a / b
            print('Метод деления')
            return result
        except ZeroDivisionError:
            print('Делить на ноль нельзя')


Calculator.set_strategy('Addition', 5, 10)    # проверям данные
print(f'\n')
Calculator.set_strategy('Subtraction', 5, 10)
print(f'\n')
Calculator.set_strategy('Multiplication', 5, 10)
print(f'\n')
Calculator.set_strategy('Division', 5, 10)
