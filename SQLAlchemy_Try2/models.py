from dataclasses import dataclass, field
from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, func, Index, CheckConstraint, Text, \
    DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship, backref

from ORM import Base


class Order(Base):
    __tablename__ = "order"

    id_order = Column(Integer, primary_key=True)
    date = Column(DateTime, server_default=func.now())

    id_client_order = Column(Integer, ForeignKey('id_client'))

    client_order = relationship('client', backref=backref('order'))
    orderList = relationship('order_list', backref=backref('order_orderList'))
    order_order_employees = relationship('employees', backref=backref('order_employees'))


class Client(Base):
    __tablename__ = "client"

    id_client = Column(Integer, primary_key=True)
    client_name = Column(Text)
    client_address = Column(Text)
    client_phone = Column(Text)

    order = relationship('order', backref=backref('client_order'))


class OrderList(Base):
    __tablename__ = "order_list"

    id_order_list = Column(Integer, primary_key=True)
    order = Column(Text)
    prize = Column(Integer)

    id_order_order_list = Column(Integer, ForeignKey('id_order'))
    order_orderList = relationship('order', backref=backref('orderList'))


class Employees(Base):
    __tablename__ = "employees"

    id_employees = Column(Integer, primary_key=True)
    employees_fullname = Column(Text)
    employees_profession = Column(Text)
    salary = Column(Integer)

    id_order_employees = Column(Integer, ForeignKey('id_order'))
    order_employees = relationship('order', backref=backref('order_order_employees'))








