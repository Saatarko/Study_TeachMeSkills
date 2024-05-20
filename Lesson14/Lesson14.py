"""1. Представим, что у нас есть таблица "Employees" с полями
"Name", "Position", "Department", "Salary".
• Создайте таблицу "Employees" с указанными полями.
• Вставьте в таблицу несколько записей с информацией о
сотрудниках вашей компании.
• Измените данные в таблице для каких-то сотрудников.
Например, изменим должность одного из сотрудников на
более высокую.
• Добавьте новое поле "HireDate" (дата приема на работу) в
таблицу "Employees".
• Добавьте записи о дате приема на работу для всех
сотрудников.
• Найдите всех сотрудников, чья должность "Manager".
• Найдите всех сотрудников, у которых зарплата больше 5000
долларов.
• Найдите всех сотрудников, которые работают в отделе
"Sales".
• Найдите среднюю зарплату по всем сотрудникам.
• Удалите таблицу "Employees".
* в качестве задания с повышенным уровнем сложности
можете реализовать пункты 6-9 в рамках хранимой функции"""
import psycopg2 as ps


def create_table():  # Функция создлания таблицы

    # Сначала удаляем таблицу (если она есть)
    del_table = """
    
    DROP TABLE IF EXISTS employees   
     
    """

    cursor.execute(del_table)

    create_table_query = """

                CREATE TABLE IF NOT EXISTS employees (
                id SERIAL PRIMARY KEY, 
                name Text,
                Position Text NOT NULL,
                Department TEXT NOT NULL,
                Salary INTEGER
                );

                """

    cursor.execute(create_table_query)




def add_row_table():  # Функция для добавления данных в SQL

    # SQL-запрос для вставки данных

    insert_query = """

    INSERT INTO employees (name, Position, Department, Salary) VALUES (%s, %s, %s, %s);

    """

    list_value = [('Иван Петров', 'Менеджер', 'ОМТС', 20000), ('Лидия Жопова', 'Директор', 'Директорат', 30000),
                  ('Сергей Сергеев', 'Уборщик', 'ОМТС', 1000), ('Сергей Есенин', 'Менеджер', 'ОМТС', 5000),
                  ('Антон Маяковский', 'сантехник', 'ОМТС', 1500)]

    cursor.executemany(insert_query, list_value)

    # Сохранение изменений (commit)
    conn.commit()


def db_read():  # Функция чтения данных из таблицы
    select_query = """

        SELECT * FROM employees;

        """

    # Выполнение SQL-запроса для извлечения данных

    cursor.execute(select_query)

    # Получение всех данных

    data = cursor.fetchall()

    # Вывод данных
    a = []
    for row in data:
        a.append(row)

    print(a)


def update():  # Функция обновления данных в таблице
    select_query = """

            UPDATE employees SET Position = 'Менеджер' WHERE Position = 'Уборщик'

            """
    cursor.execute(select_query)


def add_column():  # Функция добавления столбца
    add_query = """

                ALTER TABLE employees
                ADD COLUMN IF NOT EXISTS HireDate Date DEFAULT '2020-01-01'

                """
    cursor.execute(add_query)


def update_date():  # Функция заполнения нового столбца новыми данными
    select_query = """

            UPDATE employees SET HireDate = '2022-12-31' WHERE HireDate = '2020-01-01'

            """
    cursor.execute(select_query)


def manager_search():  # Функция поиска менеджеров
    select_query = """

            SELECT name, Position, Department, Salary FROM employees WHERE Position = 'Менеджер'

            """
    cursor.execute(select_query)

    data = cursor.fetchall()

    # Вывод данных
    a = []
    for row in data:
        a.append(row)

    print(a)


def salarity_search():  # Функция поиска тех укого большая зп
    select_query = """

            SELECT name, Position, Department, Salary FROM employees WHERE Salary >= 5000

            """
    cursor.execute(select_query)

    data = cursor.fetchall()

    # Вывод данных
    a = []
    for row in data:
        a.append(row)

    print(a)


def avg_sal():  # Функция подсчета средней зп
    select_query = """

                SELECT AVG(Salary) AS Average_Price FROM employees;

                """
    cursor.execute(select_query)

    data = cursor.fetchall()

    print(f'Средняя зарплата по фирме {data}')


conn = ps.connect(dbname="postgres", user="postgres", password="Almalexia8675309", host="127.0.0.1", port="5433")

cursor = conn.cursor()

conn.autocommit = True

create_table()
add_row_table()
db_read()
update()
db_read()
add_column()
db_read()
update_date()
db_read()
manager_search()
salarity_search()
avg_sal()

# Закрытие курсора
cursor.close()

# Закрытие соединения с базой данных

conn.close()
