"""Задача 1: Создание и заполнение таблиц
● Создайте таблицу authors с полями id, first_name и last_name.
Используйте PRIMARY KEY для поля id
● Создайте таблицу books с полями id, title, author_id и
publication_year. Используйте PRIMARY KEY для поля id и
FOREIGN KEY для поля author_id, ссылаясь на таблицу
authors
● Создайте таблицу sales с полями id, book_id и quantity.
Используйте PRIMARY KEY для поля id и FOREIGN KEY для
поля book_id, ссылаясь на таблицу books
● Добавьте несколько авторов в таблицу authors
● Добавьте несколько книг в таблицу books, указывая авторов из
таблицы authors
● Добавьте записи о продажах книг в таблицу sales
Задача 2: Использование JOIN
● Используйте INNER JOIN для получения списка всех книг и их
авторов.
● Используйте LEFT JOIN для получения списка всех авторов и
их книг (включая авторов, у которых нет книг).
● Используйте RIGHT JOIN для получения списка всех книг и их
авторов, включая книги, у которых автор не указан
Задача 3: Множественные JOIN
● Используйте INNER JOIN для связывания таблиц authors,
books и sales, чтобы получить список всех книг, их авторов и
продаж
● Используйте LEFT JOIN для связывания таблиц authors, books
и sales, чтобы получить список всех авторов, их книг и продаж
(включая авторов без книг и книги без продаж)
Задача 4: Агрегация данных с использованием JOIN
TeachMeSkills.by
● Используйте INNER JOIN и функции агрегации для
определения общего количества проданных книг каждого
автора
● Используйте LEFT JOIN и функции агрегации для определения
общего количества проданных книг каждого автора, включая
авторов без продаж
Задача 5: Подзапросы и JOIN
● Найдите автора с наибольшим количеством проданных книг,
используя подзапросы и JOIN
● Найдите книги, которые были проданы в количестве,
превышающем среднее количество продаж всех книг,
используя подзапросы и JOIN"""
import psycopg2 as ps


def create_table_authors():  # Функция создлания таблицы authors

    # Сначала удаляем таблицу (если она есть)

    cursor.execute(
        "DROP TABLE IF EXISTS authors CASCADE")  # чистов  рамках дз чтобы при перезапуке не дублирвоать данные в таблице

    create_table_query = """

                CREATE TABLE IF NOT EXISTS authors (
                id SERIAL PRIMARY KEY, 
                first_name Text NOT NULL,
                last_name Text
                );

                """
    cursor.execute(create_table_query)


def create_table_books():  # Функция создлания таблицы books

    # Сначала удаляем таблицу (если она есть)

    cursor.execute(
        "DROP TABLE IF EXISTS books CASCADE")  # чистов  рамках дз чтобы при перезапуке не дублирвоать данные в таблице

    create_table_query = """

                CREATE TABLE IF NOT EXISTS books (
                id SERIAL PRIMARY KEY, 
                title Text NOT NULL,
                publication_year Integer,
                author_id INTEGER REFERENCES authors (id)
                );

                """
    cursor.execute(create_table_query)


def create_table_sales():  # Функция создлания таблицы sales

    # Сначала удаляем таблицу (если она есть)

    cursor.execute(
        "DROP TABLE IF EXISTS sales")  # чистов  рамках дз чтобы при перезапуке не дублирвоать данные в таблице

    create_table_query = """

                CREATE TABLE IF NOT EXISTS sales (
                id SERIAL PRIMARY KEY, 
                quantity Integer,
                book_id INTEGER REFERENCES books (id)
                );

                """
    cursor.execute(create_table_query)


def add_authors():  # Функция для добавления данных в SQL таблицу авторов

    # SQL-запрос для вставки данных

    insert_query = """

    INSERT INTO authors (first_name, last_name) VALUES (%s, %s);

    """

    list_value = [('Алексанр', 'Пушкин'), ('Лев', 'Толстой'),
                  ('Сергей', 'Есенин'), ('Михаил', 'Булгаков'),
                  ('Серега','')]

    cursor.executemany(insert_query, list_value)

    # Сохранение изменений (commit)
    conn.commit()


def add_book():  # Функция для добавления данных в SQL таблицу книг

    # SQL-запрос для вставки данных

    insert_query = """

    INSERT INTO books (title, publication_year, author_id) VALUES (%s, %s, %s);

    """

    list_value = [('Граф Нулин', 1825, 1), ('Война и мир', 1915, 2),
                  ('Красный восток', 1925, 3), ('Мастер и маргарита', 1940, 4),
                  ('Собачье сердце', 1925, 4)]

    cursor.executemany(insert_query, list_value)

    # Сохранение изменений (commit)
    conn.commit()


def add_sales():  # Функция для добавления данных в SQL таблицу продаж

    # SQL-запрос для вставки данных

    insert_query = """

    INSERT INTO sales (quantity, book_id) VALUES (%s, %s);

    """

    list_value = [(2, 1), (5, 2), (50, 4), (11, 5)]

    cursor.executemany(insert_query, list_value)

    # Сохранение изменений (commit)
    conn.commit()


def innerjoin_author_and_book():  # Функция выполнения innerjoin по  author и book
    select_query = """

        SELECT authors.first_name, authors.last_name, books.title 
        FROM authors
        JOIN books ON books.author_id = authors.id;

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


def left_or_right_join_author_and_book(path):  # Функция выполнения left_or_right join по  author и book

    if path == 'right':
        select_query = """
            SELECT first_name, last_name, title
            FROM authors RIGHT JOIN books 
            ON authors.id = author_id;            
    
            """
    else:
        select_query = """
            SELECT first_name, last_name, title
            FROM authors LEFT JOIN books 
            ON authors.id = author_id;
            
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


def many_innerjoin_author_and_book_and_sales():  # Функция выполнения множественного innerjoin по  author и book
    select_query = """

        SELECT authors.first_name, authors.last_name, books.title, sales.quantity
        FROM authors
        JOIN books ON books.author_id = authors.id
        JOIN sales ON sales.book_id = books.id;

        """

    # Выполнение SQL-запроса для извлечения данных

    cursor.execute(select_query)

    # Получение всех данных

    data = cursor.fetchall()

    # Вывод данных
    a = []
    for row in data:
        a.append(row)


def many_left_join_author_and_book_and_sales():  # Функция выполнения множественного left join по  author и book

    select_query = """

        SELECT first_name, authors.last_name, books.title, sales.quantity
        FROM authors
        LEFT JOIN books ON books.author_id = authors.id
        LEFT JOIN sales ON sales.book_id = books.id;
       
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


def inner_join_with_agregation():  # Функция выполнения inner join с агрегатной функцией
    select_query = """

        SELECT authors.first_name, authors.last_name, sum(sales.quantity)
        FROM authors
        JOIN books ON books.author_id = authors.id
        JOIN sales ON sales.book_id = books.id
        GROUP BY authors.first_name, authors.last_name;
        """

    # Выполнение SQL-запроса для извлечения данных

    cursor.execute(select_query)

    # Получение всех данных

    data = cursor.fetchall()

    # Вывод данных
    a = []
    for row in data:
        a.append(row)


def left_join_with_agregation():  # Функция выполнения  left join с агрегатной функцией

    select_query = """

        SELECT authors.first_name, authors.last_name, sum(sales.quantity) as sum_book
        FROM authors
        LEFT JOIN books ON books.author_id = authors.id
        LEFT JOIN sales ON sales.book_id = books.id
        GROUP BY authors.first_name, authors.last_name;
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

def find_max_sales_author():  # Функция поиска автора с максимльно продаваемой книгой
    select_query = """

        SELECT authors.first_name, authors.last_name, sales.quantity 
        FROM authors
        JOIN books ON books.author_id = authors.id
        JOIN sales ON sales.book_id = books.id
        GROUP BY authors.first_name, authors.last_name, sales.quantity 
        HAVING sales.quantity = MAX(sales.quantity);
        
        """

    # Выполнение SQL-запроса для извлечения данных

    cursor.execute(select_query)

    # Получение всех данных

    data = cursor.fetchall()

    # Вывод данных
    a = []
    for row in data:
        a.append(row)


def find_book_higher_avg():  # Функция поиска книги продажи которой выше среднего
    select_query = """

        SELECT books.title, sales.quantity
        FROM authors
        JOIN books ON books.author_id = authors.id
        JOIN sales ON sales.book_id = books.id
        GROUP BY books.title, sales.quantity
        HAVING sales.quantity > avg(sales.quantity);
        
        """

    # Выполнение SQL-запроса для извлечения данных

    cursor.execute(select_query)

    # Получение всех данных

    data = cursor.fetchall()

    # Вывод данных
    a = []
    for row in data:
        a.append(row)



# Соезиняемся с служеббной бд
conn = ps.connect(dbname="postgres", user="postgres", password="Almalexia8675309", host="127.0.0.1", port="5433")

cursor = conn.cursor()

create_table_authors()
create_table_books()
create_table_sales()
add_authors()
add_book()
add_sales()
innerjoin_author_and_book()
left_or_right_join_author_and_book('right')
left_or_right_join_author_and_book('left')
many_innerjoin_author_and_book_and_sales()
many_left_join_author_and_book_and_sales()
inner_join_with_agregation()
left_join_with_agregation()
find_max_sales_author()
find_book_higher_avg()

# Закрытие курсора
cursor.close()

# Закрытие соединения с базой данных

conn.close()
