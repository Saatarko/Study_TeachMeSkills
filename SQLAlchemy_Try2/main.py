import os
import sys

from ORM import SyncORM
from models import Recipes

SyncORM.create_tables()

SyncORM.insert_tables_client('Антон', 'г.Минск, Черняховского 4-3', '32546545774')
SyncORM.insert_tables_client('Денис Евсеев', 'г.Минск, Рокоссовского 15-354', '6756757567')
SyncORM.insert_tables_client('Михаил Булгаков', 'г.Гродно, Ленина 21-12', '2354879565')
SyncORM.insert_tables_client('Петюня', 'г.Брест, Лынькова 166', '235896793456')
SyncORM.insert_tables_client('Оля Вуду', 'г.Брест, Гагарина 3-5', '56756860342')
SyncORM.insert_tables_client('Алина Рин', 'г.Минск, Машерова 124', '4578967947')
SyncORM.insert_tables_client('Дмитрий Бейл', 'г.Могилев, Б. Шевченко 111-6', '789213475885')
SyncORM.insert_tables_client('Игорь ГХК', 'г.Пинск, Черняховского 5-2', '4579625547655')

SyncORM.insert_tables_order(1)
SyncORM.insert_tables_order(2)
SyncORM.insert_tables_order(3)
SyncORM.insert_tables_order(4)
SyncORM.insert_tables_order(5)
SyncORM.insert_tables_order(6)
SyncORM.insert_tables_order(7)
SyncORM.insert_tables_order(8)
SyncORM.insert_tables_order(1)
SyncORM.insert_tables_order(2)
SyncORM.insert_tables_order(2)
SyncORM.insert_tables_order(3)
SyncORM.insert_tables_order(4)

SyncORM.insert_tables_recipes('4 сезона', 18, 4, 3, 6, 7, 3, 35)
SyncORM.insert_tables_recipes('5 Сыров', 14, 5, 7, 3, 4, 1, 43)
SyncORM.insert_tables_recipes('Ветчина и Грибы', 14, 3, 5, 6, 1, 6, 45)
SyncORM.insert_tables_recipes('Гавайская', 13, 8, 2, 6, 5, 3, 36)
SyncORM.insert_tables_recipes('Грибная с голубым сыром', 18, 6, 3, 5, 7, 1, 51)
SyncORM.insert_tables_recipes('Карбонара', 15, 12, 7, 1, 4, 5, 23)
SyncORM.insert_tables_recipes('Маргарита', 15, 2, 10, 6, 8, 9, 34)
SyncORM.insert_tables_recipes('Пепперони', 18, 4, 4, 2, 6, 6, 25)
SyncORM.insert_tables_recipes('Фермерская', 18, 1, 9, 9, 9, 9, 42)

SyncORM.insert_tables_employees(1, 'Сергей Петров', "Пиццерист", 5)
SyncORM.insert_tables_employees(2, 'Сергей Петров', "Пиццерист", 7)
SyncORM.insert_tables_employees(3, 'Сергей Петров', "Пиццерист", 9)
SyncORM.insert_tables_employees(4, 'Сергей Петров', "Пиццерист", 10)
SyncORM.insert_tables_employees(5, 'Сергей Петров', "Пиццерист", 4)
SyncORM.insert_tables_employees(6, 'Сергей Петров', "Пиццерист", 9)
SyncORM.insert_tables_employees(7, 'Сергей Петров', "Пиццерист", 6)
SyncORM.insert_tables_employees(8, 'Сергей Петров', "Пиццерист", 7)
SyncORM.insert_tables_employees(9, 'Сергей Петров', "Пиццерист", 4)
SyncORM.insert_tables_employees(10, 'Сергей Петров', "Пиццерист", 8)
SyncORM.insert_tables_employees(11, 'Сергей Петров', "Пиццерист", 5)
SyncORM.insert_tables_employees(12, 'Сергей Петров', "Пиццерист", 4)
SyncORM.insert_tables_employees(13, 'Сергей Петров', "Пиццерист", 9)
SyncORM.insert_tables_employees(13, 'Анна Васильева', "Пиццерист", 11)

# SyncORM.print_table_client(0)
# SyncORM.print_table_order(0)
# SyncORM.print_table_recipe()

# SyncORM.select_tables_client_and_order()

SyncORM.select_tables_client_order_order_list()
