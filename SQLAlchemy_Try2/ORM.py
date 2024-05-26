from dataclasses import dataclass, field

from sqlalchemy import Integer, and_, cast, func, insert, inspect, or_, select, text
from sqlalchemy.orm import aliased, joinedload, selectinload, DeclarativeBase, contains_eager

from database import sync_engine, session_factory, Base
from models import Client, Employees, Order, OrderList, Recipes


class Clients:
    pass


class SyncORM:

    @staticmethod
    def create_tables():  # создаем все таблицы наcледуемые от Base
        """Функция удаления и создания всех таблиц"""
        sync_engine.echo = False
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
        sync_engine.echo = False

    @staticmethod
    def insert_tables_client(temp_name, temp_address, temp_phone):  # функция доабвления данных в таблицу
        """Функция выбора вставки таблицы клиента. temp_name - имя клиента, temp_address - адрес, temp_phone -тел """
        with session_factory() as session:
            client = Client(client_name=temp_name, client_address=temp_address, client_phone=temp_phone)
            session.add(client)
            session.commit()

    @staticmethod
    def insert_tables_order(temp_id):
        """Функция добавления данных в табл заказ - temp_id - id клиента, дата заказа ставится автоматом"""
        with session_factory() as session:
            order = Order(id_client_order=temp_id)
            session.add(order)
            session.commit()

    @staticmethod
    def insert_tables_order_list(temp_id, temp_order, temp_price):
        """Функция добавления данных в заказ - temp_id - id заказа, temp_order - заказ, temp_price - цена"""
        with session_factory() as session:
            order_list = OrderList(id_order_order_list=temp_id, order=temp_order, price=temp_price)
            session.add(order_list)
            session.commit()

    @staticmethod
    def print_table_client(temp_id):
        with session_factory() as session:
            if temp_id == 0:
                query = select(Client)  # для выбора всех выбирае всю таблицу целиком
                result = session.execute(query)  # экзекьютим/выполняем ее
                clients = result.scalars().all()  # отображаем выбранных клиентво (скаляр для отсеива ненужных скобок)

                for i in range(len(clients)):
                    print(f'Клиент {clients[i].client_name}, адрес={clients[i].client_address} , '
                          f'тел={clients[i].client_phone}')

            else:
                result = session.get(Clients, temp_id)  # для вывода ожного достаточно использовать get
                clients = result.client_name
                print(f'{clients}')

    @staticmethod
    def print_table_order(temp_id):
        with session_factory() as session:
            if temp_id == 0:
                query = select(Order)  # для выбора всех выбирае всю таблицу целиком
                result = session.execute(query)  # экзекьютим/выполняем ее
                order = result.scalars().all()  # отображаем выбранных клиентво (скаляр для отсеива ненужных скобок)

                for i in range(len(order)):
                    print(f'Клиент-ID {order[i].id_client_order}, дата {order[i].date} ')

            else:
                result = session.get(Order, temp_id)  # для вывода ожного достаточно использовать get
                print(f'Клиент-ID {result.id_client_order},  дата {result.date} ')

    @staticmethod
    def insert_tables_recipes(temp_name_recipe, temp_size, temp_cheese, temp_pepperoni, temp_mushrooms, temp_onions,
                              temp_bacon, temp_price):  # функция доабвления данных в таблицу
        """Функция выбора вставки таблицы клиента. temp_name - имя клиента, temp_address - адрес, temp_phone -тел """
        with session_factory() as session:
            recipes = Recipes(name_recipe=temp_name_recipe, size=temp_size, cheese=temp_cheese,
                              pepperoni=temp_pepperoni, mushrooms=temp_mushrooms, onions=temp_onions,
                              bacon=temp_bacon, price=temp_price)
            session.add(recipes)
            session.commit()

    @staticmethod
    def print_table_recipe():
        with session_factory() as session:
            query = select(Recipes)
            result = session.execute(query)  # экзекьютим/выполняем ее
            recipes = result.scalars().all()  # отображаем выбранных клиентво (скаляр для отсеива ненужных скобок)

            for i in range(len(recipes)):
                print(f'Пицца - {recipes[i].name_recipe}, размер {recipes[i].size}, сыр {recipes[i].cheese},'
                      f' пепперони {recipes[i].pepperoni}, грибы {recipes[i].mushrooms}, лук {recipes[i].onions},'
                      f'бекон {recipes[i].bacon}, цена {recipes[i].price}')

    @staticmethod
    def insert_tables_employees(temp_id_order_employees, temp_employees_fullname, temp_employees_profession,
                                temp_salary):  # функция доабвления данных в таблицу
        """Функция выбора вставки таблицы клиента. temp_name - имя клиента, temp_address - адрес, temp_phone -тел """
        with session_factory() as session:
            employees = Employees(id_order_employees=temp_id_order_employees,
                                  employees_fullname=temp_employees_fullname,
                                  employees_profession=temp_employees_profession, salary=temp_salary)
            session.add(employees)
            session.commit()

    @staticmethod
    def select_tables_client_and_order():
        with session_factory() as session:
            query = (
                select(
                    Client,
                )
                .options(selectinload(Client.order))
                .order_by(Client.id_client)

            )
            result = session.execute(query)  # экзекьютим/выполняем ее
            res = result.scalars().all()

            for i in res:
                for j in i.order:
                    temp = ''.join(j.date.strftime("%Y-%m-%d %H:%M:%S.%f"))
                    print(f'Клиент - {i.client_name} адрес -{i.client_address} телефон - {i.client_phone} '
                          f'заказ дата- {temp}')

    @staticmethod
    def select_tables_client_order_order_list():
        with session_factory() as session:
            query = (
                select(
                    Client,
                    Order
                )
                .options(selectinload(Client.order))
                .options(selectinload(Order.client_order_list))

                .order_by(Client.id_client)

            )
            result = session.execute(query)  # экзекьютим/выполняем ее
            res = result.scalars().all()
            price = 0
            for i in res:
                for j in i.order:
                    temp = ''.join(j.date.strftime("%Y-%m-%d %H:%M:%S.%f"))
                    for k in j:
                        temp_order_list = ''.join(k.order)
                        price += k.price

                        print(f'Клиент - {i.client_name} адрес -{i.client_address} телефон - {i.client_phone} '
                              f'дата- {temp}, заказ {temp_order_list}')
