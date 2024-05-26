from dataclasses import dataclass, field
from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, func, Index, CheckConstraint, Text, \
    DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship, backref

from database import Base


class Order(Base):
    __tablename__ = "order"

    id_order = Column(Integer, primary_key=True)
    date = Column(DateTime, server_default=func.now())

    id_client_order = Column(Integer, ForeignKey('client.id_client'))

    client_order = relationship('Client', back_populates='order')

    client_order_list = relationship('OrderList', back_populates='order_order_list')

    client_order_employees = relationship('Employees', back_populates='order_employees')



class Client(Base):
    __tablename__ = "client"

    id_client = Column(Integer, primary_key=True)
    client_name = Column(Text)
    client_address = Column(Text)
    client_phone = Column(Text)

    order = relationship('Order', back_populates='client_order')


class OrderList(Base):
    __tablename__ = "order_list"

    id_order_list = Column(Integer, primary_key=True)
    order = Column(Text)
    price = Column(Integer)

    id_order_order_list = Column(Integer, ForeignKey('order.id_order'))

    order_order_list = relationship('Order', back_populates='client_order_list')


class Employees(Base):
    __tablename__ = "employees"

    id_employees = Column(Integer, primary_key=True)
    employees_fullname = Column(Text)
    employees_profession = Column(Text)
    salary = Column(Integer)

    id_order_employees = Column(Integer, ForeignKey('order.id_order'))

    order_employees = relationship('Order', back_populates='client_order_employees')


@dataclass
class Products:
    size: int = field(default=15)
    cheese: int = field(default=0)
    pepperoni: int = field(default=0)
    mushrooms: int = field(default=0)
    onions: int = field(default=0)
    bacon: int = field(default=0)


class Recipes(Base, Products):
    __tablename__ = "recipe"

    id_recipe = Column(Integer, primary_key=True)
    name_recipe = Column(String(50), unique=True)
    size = Column(Integer)
    cheese = Column(Integer)
    pepperoni = Column(Integer)
    mushrooms = Column(Integer)
    onions = Column(Integer)
    bacon = Column(Integer)
    price = Column(Integer)


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
