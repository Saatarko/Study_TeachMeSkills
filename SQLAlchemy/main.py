import os
import sys

from ORM import SyncORM

SyncORM.create_tables()
SyncORM.insert_tables_client('Сашко', 'Анна')
SyncORM.insert_tables_client('НФ')
SyncORM.insert_tables_client('Фекла', 'Антонина', 'Захар')


SyncORM.select_client(1)
SyncORM.select_client(0)

SyncORM.update_client(3, 'Климентина')

SyncORM.insert_tables_pets('1', 'Плюша', '2',
                           'метис')
SyncORM.insert_tables_pets('2', 'Мася', '8',
                           'брит')
SyncORM.insert_tables_pets('2', 'Вася', '5',
                           'мейнкун')
SyncORM.insert_tables_pets('3', 'Петч', '7',
                           'брит')
SyncORM.insert_tables_pets('1', 'Кровосися', '2',
                           'метис')
SyncORM.insert_tables_pets('1', 'Сплюша', '6',
                           'метис')
SyncORM.insert_tables_pets('5', 'Тигер', '4',
                           'мейнкун')
SyncORM.insert_tables_pets('6', 'Потрошитель бабушек', '12',
                           'ориентал')


SyncORM.insert_tables_services(1, 'Чипирование', 85)
SyncORM.insert_tables_services(1, 'Вакцинирование', 60)
SyncORM.insert_tables_services(1, 'УЗИ', 47)
SyncORM.insert_tables_services(2, 'Стерилизация', 96)
SyncORM.insert_tables_services(3, 'Операции', 175)
SyncORM.insert_tables_services(4, 'УЗИ', 47)
SyncORM.insert_tables_services(4, 'Дегельминтизация', 15)
SyncORM.insert_tables_services(5, 'Рентген', 90)
SyncORM.insert_tables_services(6, 'Предварительный осмотр', 45)
SyncORM.insert_tables_services(6, 'УЗИ', 47)

SyncORM.avg_services_cost()
SyncORM.avg_services_cost_left_join()



SyncORM.avg_pets_age('ме', 4)


