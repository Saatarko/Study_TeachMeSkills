import re
from datetime import datetime

import telebot  # Импортируем библиотеку для телеботов
from telebot import types  # Импортируем метод types (для кнопок)
from telebot.types import ReplyKeyboardRemove  # Импортируем метод для удаления кнопок
import sqlite3 as sq
import My_Class

client_flag = False
employ_flag = False

builder = My_Class.ProcedureBuilder()

letters = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя-'

bot = telebot.TeleBot('6845881716:AAHaObSsf-NRYaIuBGnnUqzW2iLugNfFHaE')


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Создаем кнопки с выбором типа программы
    item1 = types.KeyboardButton("Клиент")
    item2 = types.KeyboardButton("Сотрудник")
    markup.add(item1, item2)

    bot.send_message(message.chat.id, text=f'Добрый день. Вас приветствует клиника "Веселые котики". Вы можете '
                                           f'забронировать и заказать любую процедуру предоставляемую нашей клиникой '
                                           f'и сразу получить полный расчет',
                     reply_markup=markup)  # Высылаем сообщение пользователю и рисуем кнопки


@bot.message_handler(content_types=['text'])  # метод реакции на текст
def get_text_messages(message):
    global employ_flag, client_flag

    if message.text == "Клиент":

        client_flag = True
        employ_flag = False
        bot.send_message(message.chat.id, text='Выберите любую процедуру которую Вы бы хотели получить',
                         reply_markup=ReplyKeyboardRemove())  # Удаляем кнопки

    elif message.text == "Сотрудник":
        client_flag = False
        employ_flag = True
        bot.send_message(message.chat.id, text='Загружен модуль подбора машины',
                         reply_markup=ReplyKeyboardRemove())  # Удаляем кнопки

    if client_flag is True:  # Если включен подбор. Запрашиваем доп данные

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Создаем кнопки с выбором
        item1 = types.KeyboardButton("Процедуры")
        item2 = types.KeyboardButton("Заказ")
        item3 = types.KeyboardButton("Цены")
        item4 = types.KeyboardButton("Назад")
        markup.add(item1, item2, item3, item4)

        bot.send_message(message.chat.id, text=f'Если Вы готовы. То давайте '
                                               f'приступим к выбору!  )',
                         reply_markup=markup)

        if message.text == "Процедуры":
            bot.send_message(message.from_user.id, text="_",
                             reply_markup=ReplyKeyboardRemove())

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Создаем кнопки с выбором
            item1 = types.KeyboardButton("Чипирование")
            item2 = types.KeyboardButton("Дегельминизация")
            item3 = types.KeyboardButton("УЗИ")
            item4 = types.KeyboardButton("Рентген")
            item5 = types.KeyboardButton("Предварительный осмотр")
            item6 = types.KeyboardButton("Стерилизация")
            item7 = types.KeyboardButton("Операции")
            markup.add(item1, item2, item3, item4, item5, item6, item7)

            message = bot.reply_to(message, text=f'Все процедуры проводятся нашими лучшими специалистами!  )',
                                   reply_markup=markup)

            bot.register_next_step_handler(message, order_step)
        elif message.text == "Заказ":
            bot.send_message(message.from_user.id, text="Для формирования заказа понадобятся дополнительные данные",
                             reply_markup=ReplyKeyboardRemove())
            message = bot.reply_to(message, text=f'Введите свою Имя и Фамилию')

            bot.register_next_step_handler(message, process_name_step)


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



        message = bot.reply_to(message, 'Введите на какую дату вы хотите записаться. В формате ДД.ММ.ГГ')
        bot.register_next_step_handler(message, process_date_step, name)  # Пошаговый запрос
    except Exception:
        bot.reply_to(message, 'Извините но что-то пошло не так!')


def process_date_step(message, name):
    try:

        date = message.text
        date = datetime.strptime(date, '%d.%m.%Y')

        client

        message = bot.reply_to(message, 'Введите на какую дату вы хотите записаться. В формате ДД.ММ.ГГ')
        bot.register_next_step_handler(message, process_date_step, name)
    except Exception:
        bot.reply_to(message, 'Извините но что-то пошло не так!')


def order_step(message):
    if message.text == "Чипирование":
        builder.add_chipping()
        message.text = "При необходимости выберите еще одну процедуру или сформируйте заказ"
        message.text = "Клиент"
    elif message.text == "Дегельминизация":
        builder.add_deworming()
        message.text = "При необходимости выберите еще одну процедуру или сформируйте заказ"
        message.text = "Клиент"
    elif message.text == "УЗИ":
        builder.add_ultrasound()
        message.text = "При необходимости выберите еще одну процедуру или сформируйте заказ"
        message.text = "Клиент"
    elif message.text == "Рентген":
        builder.add_x_ray()
        message.text = "При необходимости выберите еще одну процедуру или сформируйте заказ"
        message.text = "Клиент"
    elif message.text == "Предварительный осмотр":
        builder.add_preliminary_examination()
        message.text = "При необходимости выберите еще одну процедуру или сформируйте заказ"
        message.text = "Клиент"
    elif message.text == "Стерилизация":
        builder.add_sterilization()
        message.text = "При необходимости выберите еще одну процедуру или сформируйте заказ"
        message.text = "Клиент"
    elif message.text == "Операции":
        builder.add_operation()
        message.text = "При необходимости выберите еще одну процедуру или сформируйте заказ"
        message.text = "Клиент"


# Запускаем бота
bot.polling(none_stop=True, interval=0)
