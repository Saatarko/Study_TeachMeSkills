from dataclasses import dataclass, field

from sqlalchemy import Integer, and_, cast, func, insert, inspect, or_, select, text
from sqlalchemy.orm import aliased, joinedload, selectinload, DeclarativeBase

from database import sync_engine, session_factory
from models import Client, Employees, Order, OrderList


class Base(DeclarativeBase):
    pass


@dataclass
class Products:
    size: int = field(default=15)
    cheese: int = field(default=0)
    pepperoni: int = field(default=0)
    mushrooms: int = field(default=0)
    onions: int = field(default=0)
    bacon: int = field(default=0)


@dataclass
class PizzaBuilder:  # создаем класс сборки пиццы
    parts = []


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


class Clients:
    pass


class SyncORM:

    @staticmethod
    def create_tables():  # создаем все таблицы наcледуемые от Base
        """Функция удаления и создания всех таблиц"""
        sync_engine.echo = False
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
        sync_engine.echo = True

    @staticmethod
    def insert_tables_client(temp_name, temp_address, temp_phone):  # функция доабвления данных в таблицу
        """Функция выбора вставки таблицы клиента. _client_name - имя клиента/клиентов """
        with session_factory() as session:
            client = Client(client_name=temp_name, client_address=temp_address, client_phone=temp_phone)
            session.add(client)
            session.commit()

    @staticmethod
    def insert_tables_order():
        pass


    @staticmethod
    def insert_tables_order_list():
        pass
