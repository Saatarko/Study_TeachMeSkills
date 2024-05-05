import re

import telebot  # Импортируем библиотеку для телеботов
from telebot import types  # Импортируем метод types (для кнопок)
from telebot.types import ReplyKeyboardRemove  # Импортируем метод для удаления кнопок

new_human = []  # Наш список для хранения данных по человекам


class Human:  # Класс человеков

    def __init__(self, name='Иван Иванов', car='Volvo', money=0):  # Инициализируем и задаем значения по умолчанию
        self.name = name
        self.car = car
        self.money = money


# Создаем экземпляр бота
bot = telebot.TeleBot('6574088819:AAGCI0fWRLqQx033FKAZ9qWvTzx16SEH-Z8')


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Создаем кнопки с запросом корректности данных
    item1 = types.KeyboardButton("Готов")
    item2 = types.KeyboardButton("Не готов")
    markup.add(item1, item2)

    bot.send_message(message.chat.id, text=f'Вас приветствует дикий ИскИн. Если Вы будете вести себя хорошо'
                                           f' я помогу Вам подобрать машину исходя из нужной Вам марки и '
                                           f'имеющихся у Вас денег! Если Вы готовы жмите кнопку готов )',
                     reply_markup=markup)  # Высылаем сообщение пользователю и рисуем кнопки


# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Готов" or message.text == 'Неверно':

        bot.send_message(message.from_user.id, text="Для формирования списка ответьте на несколько вопросов!",
                         reply_markup=ReplyKeyboardRemove())
        message = bot.reply_to(message, 'Введите Ваше имя и Фамилию!')
        bot.register_next_step_handler(message, process_name_step)
    elif message.text == 'Верно':  # Ответ по кнопке
        link = get_link(new_human[-1].car, new_human[-1].money)
        bot.send_message(message.chat.id, 'Загружаем сайт в соответствии с Вашими запросами')
        bot.send_message(message.chat.id, f'{link}')
        bot.send_message(message.chat.id, text='Спасибо за пользование программой', reply_markup=ReplyKeyboardRemove())

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
        elif not re.search(r'[а-яё]{2,}\s[а-яё]{2,}', name.lower()):
            message = bot.reply_to(message, 'То что вы написали, не очень похоже на Имя и Фамилию')
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
        elif not re.search(r'[а-яё]{2,}(\s[а-яё]{2,})?', car.lower()):
            message = bot.reply_to(message, 'То что вы написали, не очень похоже на марку машины. Попробуйте '
                                            'ввести еще раз!')
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


# Запускаем бота
bot.polling(none_stop=True, interval=0)
