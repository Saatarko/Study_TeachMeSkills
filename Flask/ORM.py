import datetime
from dataclasses import dataclass, field

from flask import render_template
from sqlalchemy import func
from sqlalchemy.orm import selectinload

from database import sync_engine
from models import Client, Employees, Order, OrderList, Recipes
from database import db, app


class SyncORM:

    @staticmethod
    def create_tables():  # создаем все таблицы наcледуемые от db
        """Функция удаления и создания всех таблиц"""
        # db.drop_all()
        db.create_all()

    @staticmethod
    def insert_tables_client(temp_name, temp_address, temp_phone):
        """Функция выбора вставки таблицы клиента. temp_name - имя клиента, temp_address - адрес, temp_phone -тел """
        with app.app_context():  # замена сессиям в связки Фласк+Алхимия
            client = Client(client_name=temp_name, client_address=temp_address, client_phone=temp_phone)
            db.session.add(client)
            db.session.commit()

    #
    @staticmethod
    def insert_tables_order(temp_id):
        """Функция добавления данных в табл заказ - temp_id - id клиента, дата заказа ставится автоматом"""
        with app.app_context():
            order = Order(id_client_order=temp_id)
            db.session.add(order)
            db.session.commit()

    @staticmethod
    def insert_tables_order_list(temp_id, temp_order):
        """Функция добавления данных в заказ - temp_id - id заказа, temp_order - заказ, temp_price - цена"""
        with app.app_context():
            query = db.select(Recipes)
            result = db.session.execute(query)
            recipes = result.scalars().all()
            for i in recipes:
                if i.name_recipe == temp_order:
                    temp_price = i.price
                    break

            order_list = OrderList(id_order_order_list=temp_id, order=temp_order, price=temp_price)
            db.session.add(order_list)
            db.session.commit()

    @staticmethod
    def insert_tables_recipes(temp_name_recipe, temp_size, temp_cheese, temp_pepperoni, temp_mushrooms, temp_onions,
                              temp_bacon, temp_price):  # функция доабвления данных в таблицу
        """Функция выбора вставки таблицы клиента. temp_name - имя клиента, temp_address - адрес, temp_phone -тел """
        with app.app_context():
            recipes = Recipes(name_recipe=temp_name_recipe, size=temp_size, cheese=temp_cheese,
                              pepperoni=temp_pepperoni, mushrooms=temp_mushrooms, onions=temp_onions,
                              bacon=temp_bacon, price=temp_price)
            db.session.add(recipes)
            db.session.commit()

    @staticmethod
    def insert_tables_employees(temp_id_order_employees, temp_employees_fullname, temp_employees_profession,
                                temp_salary):  # функция доабвления данных в таблицу
        """Функция выбора вставки таблицы клиента. temp_name - имя клиента, temp_address - адрес, temp_phone -тел """
        with app.app_context():
            employees = Employees(id_order_employees=temp_id_order_employees,
                                  employees_fullname=temp_employees_fullname,
                                  employees_profession=temp_employees_profession, salary=temp_salary)
            db.session.add(employees)
            db.session.commit()

    @staticmethod
    def get_client(client_id):
        with app.app_context():
            result = db.session.get(Client, client_id)  # для вывода ожного достаточно использовать get
            client = result
            return client

    @staticmethod
    def get_clients():
        with app.app_context():
            query = db.select(Client)  # для выбора всех выбирае всю таблицу целиком
            result = db.session.execute(query)  # экзекьютим/выполняем ее
            clients = result.scalars().all()  # отображаем выбранных клиентво (скаляр для отсеива ненужных скобок)
            return clients

    @staticmethod
    def get_pizza(name):
        with app.app_context():
            query = (
                db.select(
                    Client,
                )
                .db.options(selectinload(Client.order))
                .db.order_by(Client.id_client)

                )
            result = db.session.execute(query) # экзекьютим/выполняем ее
            res = result.scalars().all()  # отображаем выбранных клиентво (скаляр для отсеива ненужных скобок)
            return res

    #
    # @staticmethod
    # def print_table_client(temp_id):
    #     with session_factory() as session:
    #         if temp_id == 0:
    #             query = select(Client)  # для выбора всех выбирае всю таблицу целиком
    #             result = session.execute(query)  # экзекьютим/выполняем ее
    #             clients = result.scalars().all()  # отображаем выбранных клиентво (скаляр для отсеива ненужных скобок)
    #
    #             for i in range(len(clients)):
    #                 print(f'Клиент {clients[i].client_name}, адрес={clients[i].client_address} , '
    #                       f'тел={clients[i].client_phone}')
    #
    #         else:
    #             result = session.get(Clients, temp_id)  # для вывода ожного достаточно использовать get
    #             clients = result.client_name
    #             print(f'{clients}')
    #
    # @staticmethod
    # def print_table_order(temp_id):
    #     with session_factory() as session:
    #         if temp_id == 0:
    #             query = select(Order)  # для выбора всех выбирае всю таблицу целиком
    #             result = session.execute(query)  # экзекьютим/выполняем ее
    #             order = result.scalars().all()  # отображаем выбранных клиентво (скаляр для отсеива ненужных скобок)
    #
    #             for i in range(len(order)):
    #                 print(f'Клиент-ID {order[i].id_client_order}, дата {order[i].date} ')
    #
    #         else:
    #             result = session.get(Order, temp_id)  # для вывода ожного достаточно использовать get
    #             print(f'Клиент-ID {result.id_client_order},  дата {result.date} ')
    #

    #
    # @staticmethod
    # def print_table_recipe():
    #     """Функция вывода таблицы рецептов """
    #     with session_factory() as session:
    #         query = select(Recipes)
    #         result = session.execute(query)  # экзекьютим/выполняем ее
    #         recipes = result.scalars().all()  # отображаем выбранных клиентво (скаляр для отсеива ненужных скобок)
    #
    #         for i in range(len(recipes)):
    #             print(f'Пицца - {recipes[i].name_recipe}, размер {recipes[i].size}, сыр {recipes[i].cheese},'
    #                   f' пепперони {recipes[i].pepperoni}, грибы {recipes[i].mushrooms}, лук {recipes[i].onions},'
    #                   f'бекон {recipes[i].bacon}, цена {recipes[i].price}')
    #

    #
    # @staticmethod
    # def select_tables_client_and_order():
    #     """Функция выбора и вывода таблицы клиента и заказа"""
    #     with session_factory() as session:
    #         query = (
    #             select(
    #                 Client,
    #             )
    #             .options(selectinload(Client.order))
    #             .order_by(Client.id_client)
    #
    #         )
    #         result = session.execute(query)  # экзекьютим/выполняем ее
    #         res = result.scalars().all()
    #
    #         for i in res:
    #             for j in i.order:
    #                 temp = ''.join(j.datec)
    #             print(f'Клиент - {i.client_name} адрес -{i.client_address} телефон - {i.client_phone} '
    #                   f'заказ дата- {temp}')
    #
    # @staticmethod
    # def select_tables_client_order_order_list():
    #     """Функция выбора и вывода таблицы клиента, заказа и списка заказа"""
    #     with session_factory() as session:
    #         query = (
    #             select(
    #                 Client,
    #             )
    #             .options(selectinload(Client.order, Order.client_order_list))
    #         )
    #         result = session.execute(query)  # экзекьютим/выполняем ее
    #         res = result.scalars().all()
    #         temp_order_list = []
    #         for i in res:
    #             price = 0
    #             for j in i.order:
    #                 temp = ''.join(j.date.strftime("%Y-%m-%d %H:%M:%S.%f"))
    #                 for k in j.client_order_list:
    #                     temp_order_list.append(k.order)
    #                     price += k.price
    #
    #             print(f'Клиент - {i.client_name} адрес -{i.client_address} телефон - {i.client_phone} '
    #                   f'дата- {temp}, заказ {temp_order_list} сумма {price}')
    #
    # @staticmethod
    # def select_tables_client_order_order_list_avg_price():
    #     """Функция выбора и вывода таблицы клиента, заказа и средней суммы"""
    #     with session_factory() as session:
    #         query = (
    #             select(
    #                 Client,
    #                 func.avg(OrderList.price)
    #             )
    #             .options(selectinload(Client.order, Order.client_order_list))
    #             .group_by(Client.id_client)
    #         )
    #         result = session.execute(query)  # экзекьютим/выполняем ее
    #         res = result.scalars().all()
    #         print(f'{res}')
    #
    # @staticmethod
    # def update_any_table_with_id(temp_table, temp_field, new_value, temp_id):
    #     """Функция обновления данных в таблице по ID, где temp_table - таблица для обновления
    #     temp_field - поле для обновлениея, new_value - новое значение, temp_id - id"""
    #     with session_factory() as session:
    #         if temp_table == 'Client':
    #             search = session.get(Client, temp_id)
    #             if temp_field == 'client_name':
    #                 search.client_name = new_value
    #             elif temp_field == 'client_address':
    #                 search.client_address = new_value
    #             elif temp_field == 'client_phone':
    #                 search.client_phone = new_value
    #         elif temp_table == 'OrderList':
    #             search = session.get(OrderList, temp_id)
    #             search.order = new_value
    #         elif temp_table == 'Employees':
    #             search = session.get(Employees, temp_id)
    #             if temp_field == 'employees_fullname':
    #                 search.employees_fullname = new_value
    #             elif temp_field == 'employees_profession':
    #                 search.employees_profession = new_value
    #             elif temp_field == 'salary':
    #                 search.salary = new_value
    #
    #         session.commit()
    #
    # @staticmethod
    # def update_any_table_without_id(temp_table, temp_field, old_value, new_value):
    #     """Функция обновления данных в таблице без ID, где temp_table - таблица для обновления
    #     temp_field - поле для обновлениея, old_value -текущее значение, new_value - новое значение"""
    #     with session_factory() as session:
    #         if temp_table == 'Client':
    #             if temp_field == 'client_name':
    #                 query = (select(Client, ).filter(Client.client_name == old_value))
    #             elif temp_field == 'client_address':
    #                 query = (select(Client, ).filter(Client.client_address == old_value))
    #             elif temp_field == 'client_phone':
    #                 query = (select(Client, ).filter(Client.client_phone == old_value))
    #
    #         elif temp_table == 'OrderList':
    #             query = (select(OrderList, ).filter(OrderList.order == old_value))
    #         elif temp_table == 'Employees':
    #             if temp_field == 'employees_fullname':
    #                 query = (select(Employees, ).filter(Employees.employees_fullname == old_value))
    #             elif temp_field == 'employees_profession':
    #                 query = (select(Employees, ).filter(Employees.employees_profession == old_value))
    #             elif temp_field == 'salary':
    #                 query = (select(Employees, ).filter(Employees.salary == old_value))
    #
    #         result = session.execute(query)  # экзекьютим/выполняем ее
    #         res = result.scalars().all()
    #         if temp_table == 'Client':
    #
    #             if temp_field == 'client_name':
    #                 for a in res:
    #                     a.client_name = new_value
    #             elif temp_field == 'client_address':
    #                 for a in res:
    #                     a.client_address = new_value
    #             elif temp_field == 'client_phone':
    #                 for a in res:
    #                     a.client_phone = new_value
    #         elif temp_table == 'OrderList':
    #             for a in res:
    #                 a.order = new_value
    #         elif temp_table == 'Employees':
    #             if temp_field == 'employees_fullname':
    #                 for a in res:
    #                     a.employees_fullname = new_value
    #             elif temp_field == 'employees_profession':
    #                 for a in res:
    #                     a.employees_profession = new_value
    #             elif temp_field == 'salary':
    #                 for a in res:
    #                     a.salary = new_value
    #
    #         session.commit()
    #
    # @staticmethod
    # def search_client_by_city(temp_city):
    #     """Функция формирования списка клиентов по городу (Можно не целиком), temp_city - строка с названием"""
    #     with session_factory() as session:
    #         query = (
    #             select(
    #                 Client,
    #             )
    #             .options(selectinload(Client.order, Order.client_order_list))
    #             .filter(Client.client_address.ilike(f'%{temp_city}%'))
    #             .order_by(Client.client_name)
    #         )
    #         result = session.execute(query)  # экзекьютим/выполняем ее
    #         res = result.scalars().all()
    #         temp_order_list = []
    #         for i in res:
    #             price = 0
    #             for j in i.order:
    #                 temp = ''.join(j.date.strftime("%Y-%m-%d %H:%M:%S.%f"))
    #                 for k in j.client_order_list:
    #                     temp_order_list.append(k.order)
    #                     price += k.price
    #
    #             print(f'Клиент - {i.client_name} адрес -{i.client_address} телефон - {i.client_phone} '
    #                   f'дата- {temp}, заказы {temp_order_list} на сумму {price}')
    #
    # @staticmethod
    # def delete_any_row_in_table_with_id(temp_table, temp_id):
    #     """Функция удаления данных в таблице по ID, где temp_table - таблица для удаления, а temp_id - id"""
    #     with session_factory() as session:
    #         if temp_table == 'Client':
    #             search = session.get(Client, temp_id)
    #         elif temp_table == 'OrderList':
    #             search = session.get(OrderList, temp_id)
    #         elif temp_table == 'Employees':
    #             search = session.get(Employees, temp_id)
    #         delete(search)
    #         session.commit()
    #
    # @staticmethod
    # def delete_any_row_in_table_without_id(temp_table, temp_field, old_value):
    #     """Функция удаления данных в таблице без ID по любому полю, где temp_table - таблица для обновления
    #     temp_field - поле для обновлениея, old_value -текущее значение"""
    #     with session_factory() as session:
    #         if temp_table == 'Client':
    #             if temp_field == 'client_name':
    #                 query = (select(Client, ).filter(Client.client_name == old_value))
    #             elif temp_field == 'client_address':
    #                 query = (select(Client, ).filter(Client.client_address == old_value))
    #             elif temp_field == 'client_phone':
    #                 query = (select(Client, ).filter(Client.client_phone == old_value))
    #
    #         elif temp_table == 'OrderList':
    #             query = (select(OrderList, ).filter(OrderList.order == old_value))
    #         elif temp_table == 'Employees':
    #             if temp_field == 'employees_fullname':
    #                 query = (select(Employees, ).filter(Employees.employees_fullname == old_value))
    #             elif temp_field == 'employees_profession':
    #                 query = (select(Employees, ).filter(Employees.employees_profession == old_value))
    #             elif temp_field == 'salary':
    #                 query = (select(Employees, ).filter(Employees.salary == old_value))
    #
    #         result = session.execute(query)  # экзекьютим/выполняем ее
    #         res = result.scalars().all()
    #         for a in res:
    #             delete(a)
    #         session.commit()
