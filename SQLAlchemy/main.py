import os
import sys

from ORM import SyncORM


SyncORM.create_tables()
SyncORM.insert_tables_client('Сашко', 'Анна')
SyncORM.insert_tables_client('НФ')

SyncORM.select_client(1)
SyncORM.select_client(0)

SyncORM.update_client(3, 'Жопа')

SyncORM.insert_tables_pets('1','Плюша','2',
                           'метис')
SyncORM.insert_tables_pets('2','Мася','8',
                           'брит')
SyncORM.insert_tables_pets('2','Вася','5',
                           'мейнкун')
SyncORM.insert_tables_pets('3','Петч','7',
                           'брит')
SyncORM.insert_tables_pets('1','Кровосися','2',
                           'метис')
SyncORM.insert_tables_pets('1','Сплюша','6',
                           'метис')

SyncORM.avg_pets_age('ме',4)