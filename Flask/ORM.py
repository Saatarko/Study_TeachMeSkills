from dataclasses import dataclass, field

from sqlalchemy import func
from sqlalchemy.orm import selectinload
from wtforms.validators import ValidationError

from database import sync_engine
from models import Client, Employees, Order, OrderList, Recipes, PizzaDirector, PizzaBuilder, Basket, User
from database import db, app

director = PizzaDirector()  # создаем объекта класса директор
builder = PizzaBuilder()  # создаем объекта класса создания пиццы
director.builder = builder  # вызываем метод билдер из класса директор


class SyncORM:

    @staticmethod
    def create_tables():  # создаем все таблицы наcледуемые от db
        """Функция удаления и создания всех таблиц"""
        with app.app_context():
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
                              temp_bacon, temp_price, temp_decription,
                              temp_eng_name):  # функция доабвления данных в таблицу
        """Функция выбора вставки таблицы клиента. temp_name - имя клиента, temp_address - адрес, temp_phone -тел """
        with app.app_context():
            recipes = Recipes(name_recipe=temp_name_recipe, size=temp_size, cheese=temp_cheese,
                              pepperoni=temp_pepperoni, mushrooms=temp_mushrooms, onions=temp_onions,
                              bacon=temp_bacon, price=temp_price, description=temp_decription, eng_name=temp_eng_name)
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
            query = db.select(Recipes)
            result = db.session.execute(query)
            recipes = result.scalars().all()
            for i in recipes:
                if i.name_recipe == name:
                    return i

    @staticmethod
    def get_order(name):
        with app.app_context():
            query = db.select(Recipes)
            result = db.session.execute(query)
            recipes = result.scalars().all()
            for i in recipes:
                if i.name_recipe == name:
                    # это функция для потенциального списывания продуктов со склада
                    director.make_pizza_self(size=i.size, cheese=i.cheese, pepperoni=i.pepperoni, mushrooms=i.mushrooms,
                                             onions=i.onions, bacon=i.bacon)
                    # кладем заказ в корзину
                    basket = Basket(order=i.name_recipe, price=i.price)
                    db.session.add(basket)
                    db.session.commit()
                    basket, all_price = SyncORM.basket_order()
                    return basket, all_price

    @staticmethod
    def basket_order():
        with app.app_context():
            all_price = 0
            query = db.select(Basket)
            result = db.session.execute(query)
            basket = result.scalars().all()  # отображаем выбранных заказов
            all_price = sum([i.price for i in basket])
            return basket, all_price

    @staticmethod
    def drop_basket_order():
        with app.app_context():
            db.session.query(Basket).delete()
            db.session.commit()

    @staticmethod
    def search_client_id(name):
        with app.app_context():
            query = db.select(Client)
            result = db.session.execute(query)
            client = result.scalars().all()
            for i in client:
                if i.client_name == name:
                    return i.id_client

    @staticmethod
    def search_table_order(temp_id):
        with app.app_context():
            query = db.select(Order)
            result = db.session.execute(query)
            order = result.scalars().all()
            for i in order:
                if i.id_client_order == temp_id:
                    return i.id_order

    @staticmethod
    def create_new_order(usernameorder, addressorder, phoneorder):
        SyncORM.insert_tables_client(usernameorder, addressorder, phoneorder)
        temp_id = SyncORM.search_client_id(usernameorder)
        SyncORM.insert_tables_order(temp_id)
        temp_id_order = SyncORM.search_table_order(temp_id)
        with app.app_context():
            query = db.select(Basket)
            result = db.session.execute(query)
            basket = result.scalars().all()
            for i in basket:
                SyncORM.insert_tables_order_list(temp_id_order, i.order)
                db.session.commit()
            SyncORM.drop_basket_order()

    @staticmethod
    def chek_value(username, password):
        query = db.select(User)
        result = db.session.execute(query)
        user = result.scalars().all()
        for i in user:
            if i.username == username:
                return User.check_password(i, password)

    @staticmethod
    def insert_tables_user(temp_name, temp_pass):
        """Функция выбора вставки таблицы клиента. temp_name - имя клиента, temp_address - адрес, temp_phone -тел """
        with app.app_context():
            check = False
            query = db.select(User)
            result = db.session.execute(query)
            user = result.scalars().all()
            for i in user:
                if i.username == temp_name:
                    check = True
                    break
            if check is False:
                u = User(username=temp_name)
                u.set_password(temp_pass)
                db.session.add(u)
                db.session.commit()

    @staticmethod
    def search_user(username):
        query = db.select(User)
        result = db.session.execute(query)
        user = result.scalars().all()
        for i in user:
            if i.username == username:
                return i

    @staticmethod
    def select_tables_client_order_order_list(temp_id):
        """Функция выбора и вывода  клиента, заказа и списка заказа id -это id клиента"""
        query = (
            db.select
                (
                Client,
            )
            .options(selectinload(Client.order, Order.client_order_list))
            .filter(Client.id_client == temp_id)
        )
        result = db.session.execute(query)
        res = result.scalars().all()

        return res



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
