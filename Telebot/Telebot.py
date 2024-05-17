import re

import telebot  # Импортируем библиотеку для телеботов
from telebot import types  # Импортируем метод types (для кнопок)
from telebot.types import ReplyKeyboardRemove  # Импортируем метод для удаления кнопок
import sqlite3 as sq

from typing import List

new_human = []  # Наш список для хранения данных по человекам
eho_flag = False
podbor_flag = False

letters = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя-'


class Human:  # Класс человеков
    def __init__(self, name='Иван Иванов', car='Volvo', money=0):  # Инициализируем и задаем значения по умолчанию
        self.name = name
        self.car = car
        self.money = money

    def __iter__(self):  # НА запрос делаем итерированный кортеж
        _list = (self.name, self.car, int(self.money))
        it = iter(_list)
        return it


# Создаем экземпляр бота
bot = telebot.TeleBot('6574088819:AAGCI0fWRLqQx033FKAZ9qWvTzx16SEH-Z8')


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Создаем кнопки с выбором типа программы
    item1 = types.KeyboardButton("Эхо-бот")
    item2 = types.KeyboardButton("Подбор машины-бот")
    markup.add(item1, item2)

    bot.send_message(message.chat.id, text=f'Вас приветствует дикий ИскИн. Если Вы будете вести себя хорошо, '
                                           f'то мы можем поиграть в игру Эхо (я буду повторять ваши слова) или '
                                           f'же я могу подобрать для Вас машину исходя из Ваших требований',
                     reply_markup=markup)  # Высылаем сообщение пользователю и рисуем кнопки


@bot.message_handler(commands=["info"])
def info(message):
    message = bot.reply_to(message, 'Для просмотра списка введите пожалуйста пароль')
    bot.register_next_step_handler(message, process_pass_step)


def process_pass_step(message):
    count = 0

    if message.text == '32167':
        db_read(message)

    else:
        bot.send_message(message.chat.id, text=f'К сожалению пароль неправильный. Попробуйте еще раз!')


# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])  # метод реакции на текст
def get_text_messages(message):
    global eho_flag, podbor_flag

    if eho_flag is True:  # Если включен эхо-бот

        bot.send_message(message.chat.id, message.text)  # повторяем сообщения
    elif message.text == "Эхо-бот":
        eho_flag = True
        podbor_flag = False
        bot.send_message(message.chat.id, text='Загружен Эхо-бот. Он же бот повторяка. Пробуйте',
                         reply_markup=ReplyKeyboardRemove())  # Удаляем кнопки
    elif message.text == "Подбор машины-бот":
        podbor_flag = True
        eho_flag = False
        bot.send_message(message.chat.id, text='Загружен модуль подбора машины',
                         reply_markup=ReplyKeyboardRemove())  # Удаляем кнопки
        message.text = "Готов"
        # get_text_messages(message)

    if podbor_flag is True:  # Если включен подбор. Запрашиваем доп данные

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Создаем кнопки с выбором
        item1 = types.KeyboardButton("Готов")
        item2 = types.KeyboardButton("Не готов")
        markup.add(item1, item2)

        bot.send_message(message.chat.id, text=f'Если Вы готовы. То давайте '
                                               f'приступим к подбору!  )',
                         reply_markup=markup)

        if message.text == "Готов" or message.text == 'Неверно':
            bot.send_message(message.from_user.id, text="Для формирования списка ответьте на несколько вопросов!",
                             reply_markup=ReplyKeyboardRemove())
            message = bot.reply_to(message, 'Введите Ваше имя и Фамилию!')
            bot.register_next_step_handler(message, process_name_step)
        elif message.text == 'Верно' and podbor_flag is True:  # Ответ по кнопке
            link = get_link(new_human[-1].car, new_human[-1].money)
            bot.send_message(message.chat.id, 'Загружаем сайт в соответствии с Вашими запросами')
            bot.send_message(message.chat.id, f'{link}')
            bot.send_message(message.chat.id, text='Спасибо за пользование программой',
                             reply_markup=ReplyKeyboardRemove())

            db_open()

            bot.send_message(chat_id=-4266542112, text=f'Был  сформирован запрос от '
                                                       f'{new_human[-1].name} на машину {new_human[-1].car} с '
                                                       f'максимальной суммой {new_human[-1].money}')


def process_name_step(message):  # Функция пошагового запроса для получения данных (ФИО)
    try:

        name = message.text


        if not isinstance(name, str):  # Проверка на то что бы ФИо были строкой

            message = bot.reply_to(message, 'Имя и Фамилия из цифр -  что-то новое! Попробуйте ввести еще раз!')
            bot.register_next_step_handler(message, process_name_step)
            return
        temp_name = name.lower()
        temp_name = temp_name.split()
        if len(temp_name) < 2:
            message = bot.reply_to(message, 'Имя и Фамилия состоят минимум из 2 слов')
            bot.register_next_step_handler(message, process_name_step)
            return

        for s in temp_name:
            if len(s.strip(letters)) != 0:
                message = bot.reply_to(message, 'В Имени и Фамилии допустимы только буквы!')
                bot.register_next_step_handler(message, process_name_step)
                return

        user = Human(name)  # Создаем элемент класса
        new_human.append(user)  # Загоняем эк в список
        message = bot.reply_to(message, 'Машину какой марки Вы бы хотели приобрести? (Mersedes, Volvо и т.д.)')
        bot.register_next_step_handler(message, process_car_step)  # Пошаговый запрос
    except Exception:
        bot.reply_to(message, 'Извините но что-то пошло не так!')


def process_car_step(message):  # Функция пошагового запроса для получения данных (Машина)
    try:

        car = message.text

        if not isinstance(car, str):  # Проверка на то что бы ФИо были строкой

            message = bot.reply_to(message, 'Марка машины из цифр -  что-то новое! Попробуйте ввести еще раз!')
            bot.register_next_step_handler(message, process_car_step)
            return
        temp_car = car.lower()

        for s in temp_car:
            if len(s.strip(letters)) != 0:
                message = bot.reply_to(message, 'В названии машины допустимы только буквы!')
                bot.register_next_step_handler(message, process_car_step)
                return

        new_human[-1].car = car  # Экземпляр класса уже есть и в списке. Присваиваем ему новое авто
        message = bot.reply_to(message, 'Сколько у Вас денег для покупки?')
        bot.register_next_step_handler(message, process_money_step)  # Пошаговый запрос
    except Exception:
        bot.reply_to(message, 'Извините но что-то пошло не так!')


def process_money_step(message):  # Функция пошагового запроса для получения данных (деньги)ьштщ
    try:

        money = message.text
        if not money.isdigit() or int(money) < 0:  # Проверка на то что бы денежки были цифрой

            message = bot.reply_to(message, 'Значение денег - это положительная цифра. Попробуйте ввести еще раз!')
            bot.register_next_step_handler(message, process_money_step)
            return

        new_human[-1].money = money  # Экземпляр класса уже есть и в списке. Присваиваем ему новое значение денег

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Создаем кнопки с запросом корректности данных
        item1 = types.KeyboardButton("Верно")
        item2 = types.KeyboardButton("Неверно")
        markup.add(item1, item2)

        bot.send_message(message.chat.id, text=f'Итак. Вы {new_human[-1].name}, хотите машину {new_human[-1].car}.'
                                               f'По деньгам не более - {new_human[-1].money}. Все верно?',
                         reply_markup=markup)  # Высылаем сообщение пользователю и рисуем кнопки

    except Exception:
        bot.reply_to(message, 'Извините но что-то пошло не так!')


def get_link(car, money):  # Функция подготовки ссылки на сайт в соответствии с запросом
    if car.lower() == 'вольво' or car.lower() == 'volvo':
        temp_link = f'https://cars.av.by/filter?brands[0][brand]={1238}&price_usd[max]={money}]'
    elif car.lower() == 'альфа ромео' or car.lower() == 'alfa romeo':
        temp_link = f'https://cars.av.by/filter?brands[0][brand]={10297}&price_usd[max]={money}]'
    elif car.lower() == 'ауди' or car.lower() == 'audi':
        temp_link = f'https://cars.av.by/filter?brands[0][brand]={6}&price_usd[max]={money}]'
    elif car.lower() == 'бмв' or car.lower() == 'bmw':
        temp_link = f'https://cars.av.by/filter?brands[0][brand]={8}&price_usd[max]={money}]'
    elif car.lower() == 'шевроле' or car.lower() == 'chevrolet':
        temp_link = f'https://cars.av.by/filter?brands[0][brand]={41}&price_usd[max]={money}]'
    elif car.lower() == 'хендай' or car.lower() == 'hyundai':
        temp_link = f'https://cars.av.by/filter?brands[0][brand]={433}&price_usd[max]={money}]'
    elif car.lower() == 'лада' or car.lower() == 'lada':
        temp_link = f'https://cars.av.by/filter?brands[0][brand]={1279}&price_usd[max]={money}]'
    elif car.lower() == 'лада' or car.lower() == 'lada':
        temp_link = f'https://cars.av.by/filter?brands[0][brand]={1279}&price_usd[max]={money}]'
    elif car.lower() == 'опель' or car.lower() == 'opel':
        temp_link = f'https://cars.av.by/filter?brands[0][brand]={966}&price_usd[max]={money}]'
    elif car.lower() == 'мерседес' or car.lower() == 'mercedes':
        temp_link = f'https://cars.av.by/filter?brands[0][brand]={683}&price_usd[max]={money}]'
    elif car.lower() == 'фольксваген' or car.lower() == 'volkswagen':
        temp_link = f'https://cars.av.by/filter?brands[0][brand]={1216}&price_usd[max]={money}]'
    else:
        temp_link = 'Точного совпадения по марке машины не найдено. Поэтому просто ссылка на сайт https://cars.av.by'
    return temp_link


def db_open():  # Функция создания таблицы в SQL

    # Подключение или создание базы данных

    connection = sq.connect("people.db")

    # Получение объекта курсора для выполнения операций с базой данных
    cursor = connection.cursor()

    # SQL-запрос для создания таблицы

    create_table_query = """

    CREATE TABLE IF NOT EXISTS people (

    id INTEGER PRIMARY KEY,
    
    name Text NOT NULL,

    car TEXT NOT NULL,

    money INTEGER

    );

    """

    # Выполнение SQL-запроса для создания таблицы

    cursor.execute(create_table_query)

    # Закрытие курсора

    cursor.close()

    connection.close()

    # Вызов функции добавления данных в SQL
    db_work()


def db_work():  # Функция для добавления данных в SQL

    # Подключение или создание базы данных

    connection = sq.connect("people.db")

    cursor = connection.cursor()

    # SQL-запрос для вставки данных

    insert_query = """

    INSERT INTO people (name, car, money) VALUES (?, ?, ?);

    """
    # Итерируем наш класс вызывая соответвующий метод. И затем  переводим его в список ибо
    # по умолчанию __iter__ возвращает кортеж, а sql жрет только списки
    cursor.execute(insert_query, list(iter(new_human[-1])))

    # Сохранение изменений (commit)

    connection.commit()

    # Закрытие курсора
    cursor.close()

    # Закрытие соединения с базой данных

    connection.close()


def db_read(message):
    try:
        connection = sq.connect("people.db")

        cursor = connection.cursor()

        # SQL-запрос для извлечения данных

        select_query = """
    
        SELECT * FROM people;
    
        """

        # Выполнение SQL-запроса для извлечения данных

        cursor.execute(select_query)

        # Получение всех данных

        data = cursor.fetchall()

        # Вывод данных

        for row in data:
            bot.send_message(message.chat.id, text=f'{row}')

        # Закрытие курсора (опционально, но рекомендуется)

        cursor.close()

        # Закрытие соединения с базой данных

        connection.close()

    except Exception:
        bot.send_message(message.chat.id,
                         text=f'Запросов пока  небыло')  # Высылаем сообщение пользователю и рисуем кнопки


# Запускаем бота
bot.polling(none_stop=True, interval=0)
