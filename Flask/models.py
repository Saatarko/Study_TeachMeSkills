from dataclasses import dataclass, field
from datetime import datetime

from sqlalchemy import Column, Integer, String, MetaData, ForeignKey, func, Index, CheckConstraint, Text, DateTime

from database import db


class Order(db.Model):
    id_order = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, server_default=func.current_date())

    id_client_order = db.Column(db.Integer, db.ForeignKey('client.id_client'))

    client_order = db.relationship('Client', back_populates='order')

    client_order_list = db.relationship('OrderList', back_populates='order_order_list')

    client_order_employees = db.relationship('Employees', back_populates='order_employees')


class Client(db.Model):
    id_client = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.Text)
    client_address = db.Column(db.Text)
    client_phone = db.Column(db.Text)

    order = db.relationship('Order', back_populates='client_order')


class OrderList(db.Model):
    id_order_list = db.Column(db.Integer, primary_key=True)
    order = db.Column(db.Text)
    price = db.Column(db.Integer)

    id_order_order_list = db.Column(db.Integer, db.ForeignKey('order.id_order'))
    order_order_list = db.relationship('Order', back_populates='client_order_list')


class Employees(db.Model):
    id_employees = db.Column(db.Integer, primary_key=True)
    employees_fullname = db.Column(db.Text)
    employees_profession = db.Column(db.Text)
    salary = db.Column(db.Integer)

    id_order_employees = db.Column(Integer, db.ForeignKey('order.id_order'))
    order_employees = db.relationship('Order', back_populates='client_order_employees')


@dataclass
class Products:
    size: int = field(default=15)
    cheese: int = field(default=0)
    pepperoni: int = field(default=0)
    mushrooms: int = field(default=0)
    onions: int = field(default=0)
    bacon: int = field(default=0)


class Recipes(db.Model):
    id_recipe = db.Column(db.Integer, primary_key=True)
    name_recipe = db.Column(db.String(50), unique=True)
    size = db.Column(db.Integer)
    cheese = db.Column(db.Integer)
    pepperoni = db.Column(db.Integer)
    mushrooms = db.Column(db.Integer)
    onions = db.Column(db.Integer)
    bacon = db.Column(db.Integer)
    price = db.Column(db.Integer)
    description = db.Column(db.Text)
    eng_name = db.Column(db.Text)


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
