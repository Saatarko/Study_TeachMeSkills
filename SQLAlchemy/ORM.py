from sqlalchemy import Integer, and_, cast, func, insert, inspect, or_, select, text

from database import Base, sync_engine, session_factory
from models import ClientsORM, PetsORM


class SyncORM:

    @staticmethod
    def create_tables():  # создаем все таблицы наледуемые от Base
        """Функция удаления и создания всех таблиц"""
        sync_engine.echo = False
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
        sync_engine.echo = True

    @staticmethod
    def insert_tables_client(*_client_name):  # функция доабвления данных в таблицу (если данные много по 1 на 1 объект)
        """Функция выбора вставки таблицы клиента. _client_name - имя клиента/клиентов """
        with session_factory() as session:
            for i in range(len(_client_name)):
                client = ClientsORM(client_name=_client_name[i])
                session.add(client)
                session.flush()  # заносим данные базу без закрытия сессии
            session.commit()

    @staticmethod
    def insert_tables_pets(temp_id, temp_name, temp_age, temp_breed):  # функция доабвления данных в таблицу
        """Функция выбора вставки таблицы питомцев. temp_id - id клиента, temp_name -имя питомца,
        temp_age возраст питомца, temp_breed - порода питомца """
        with session_factory() as session:
            pet = PetsORM(client_id=temp_id, pets_name=temp_name, pets_age=temp_age, pets_breed=temp_breed)
            session.add(pet)
            session.commit()

    @staticmethod
    def select_client(temp_id):  # Функция выбора клиента из списка (можно выбрать одного, моэжно всех)
        """Функция выбора  клиента/клиентов. temp_id - цифра конкретный id, 0 - выбрать всех"""
        with session_factory() as session:
            if temp_id == 0:
                query = select(ClientsORM)  # для выбора всех выбирае всю таблицу целиком
                result = session.execute(query)  # экзекьютим/выполняем ее
                clients = result.scalars().all()  # отображаем выбранных клиентво (скаляр для отсеива ненужных скобок)

                for i in range(len(clients)):
                    print(f'{clients[i].client_name}')

            else:
                result = session.get(ClientsORM, temp_id)  # для вывода ожного достаточно использовать get
                clients = result.client_name
            print(f'{clients}')


    @staticmethod
    def update_client(clients_id, new_name):  # обновляем данные в таблице клиентво
        """Функция обновления имени клиента. clients_id - id клиента которому обновляем имя, new_name - новое имя"""
        with session_factory() as session:
            client = session.get(ClientsORM, clients_id)
            client.client_name = new_name
            session.commit()

    @staticmethod
    def avg_pets_age(temp_part_breed,
                     temp_age):  # фукнция выборки из таблицы питомцев среднего возраста для метисов и британцев
        """Функция выборки по породе  и возрасту. temp_part_breed - часть названия породы по которой будет отсев.
        temp_age - ограничительный возраст (покажет не старше этого возраста) """

        with session_factory() as session:
            query = (  # октрываем переменную для выборки
                select(  # октрываем выборку
                    PetsORM.pets_breed,

                    # cast -функция приведения (тут к интегеру), label - название
                    cast(func.avg(PetsORM.pets_age), Integer).label('avg_metis_and_brit_age')
                )
                .select_from(PetsORM)  # если таблица одна и таже не обяхзательная строка
                .filter(and_(  # октрываем фильтр и затем если несколько условий открываем спец фун-ю алхимии _and
                    PetsORM.pets_breed.contains(temp_part_breed),  # аналог Like -поиск сопадения слова
                    PetsORM.pets_age < temp_age  # отсев по возрасту

                ))
                .group_by(PetsORM.pets_breed)  # группируем по породе
            )
            # длеаем так чтобы в консоль выводился так же как SQL запрос
            print(query.compile(compile_kwargs={'literal_binds': True}))


