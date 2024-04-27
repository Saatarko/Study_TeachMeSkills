from tkinter import *  # Добавляем библиотеку Ткинтер
from tkinter import ttk  # Добавляем модуль Ткинтера
from My_Function import *  # Добавляем библиотеку Function
from itertools import groupby
import csv

human_by_house_menu = Tk()

human_by_house_menu.title("Домашнее задание по теме 8")

# Получаем ширину и высоту экрана

screen_width = human_by_house_menu.winfo_screenwidth()
screen_height = human_by_house_menu.winfo_screenheight()

# Вычисляем координаты окна приложения
window_width = 600
window_height = 860
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

human_by_house_menu.geometry(f"{window_width}x{window_height}+{x}+{y}")
human_by_house_menu.resizable(None, None)  # Запрещаем изменять размер окна
human_by_house_menu["bg"] = "gray22"  # gray gray0-99   # Устанавливаем цвет фона

new_human = []  # переменная для хранения человеков
new_house = []  # переменная для хранения домов
human_name = []  # переменная для хранения имен (для выпадающего списка)
house_name = []  # переменная для хранения имен домов (для выпадающего списка)


class MyException(Exception):
    """Мой класс для исключений"""


class ExceptionNullField(MyException):
    """Класс для исключений на пустые поля"""


class ExceptionStrInNumber(MyException):
    """Класс для исключений на введение строк в цифровые поля"""


class ExceptionNegativeNumber(MyException):
    """Класс для исключений на введение отрицательных чисел """
    pass


class Human:
    """Мой класс для челвоеков"""
    # Статические поля (переменные класса)
    default_name = 'Никто'
    default_age = 25
    instances = 0

    def __init__(self, name, age):
        # Динамические публичные поля (переменные объекта)
        self.name = name
        self.age = age

        # Динамические приватные поля
        self.money = 0
        self.house = None

    # Метод для регулировки вывода данных в виде текста
    def __str__(self):
        return f'Имя: {self.name}, Возраст: {self.age}, Деньги в наличии: {self.money}, Дом: {self.house}'

    # Метод для регулировки вывода данных в виде кода
    def __repr__(self):
        return f'(\'{self.name}\', {self.age}, {self.money}, \'{self.house}\')'

    # добавляем метод инфо
    def info(self):
        print(f'Имя: {self.name}')
        print(f'Возраст: {self.age}')
        print(f'Деньги в наличии: {self.money}')
        print(f'Дом: {self.house}')

    # Приватный метод
    def __make_deal(self, house, house_price):
        # Динамические публичные поля (переменные объекта)
        self.money -= house_price
        self.house = house

    def earn_money(self, money):
        self.money += money

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.money > price:
            self.__make_deal(house, price)
        else:
            mb.showwarning(f"Внимание,", f'Денег не хватает. Надо еще заработать {price - self.money}')


class House:

    def __init__(self, name, price):
        self.name = name
        self.price = price

        # Метод для регулировки вывода данных в виде текста

    def __str__(self):
        return f'Название: {self.name}, Цена: {self.price}'

    # Метод для регулировки вывода данных в виде кода
    def __repr__(self):
        return f'(\'{self.name}\', {self.price})'

    def final_price(self, discount):
        final_price = self.price * (100 - discount) / 100

        return final_price


def get_enter():  # Создаем подкласс (второе окно)
    human_by_house_menu.withdraw()
    human_by_house = Toplevel(human_by_house_menu)
    human_by_house.title("Покупка дома. Классы")
    human_by_house.geometry(f"{window_width}x{window_height}+{x}+{y}")
    human_by_house.resizable(None, None)
    human_by_house["bg"] = "gray90"

    # region функции основной программы

    def on_screen_human():

        text_class.config(state="normal")
        text_class.delete('1.0', END)
        human_name.clear()
        for human in new_human:
            human_name.append(human.name)
            combobox_by_house['values'] = human_name
            combobox_by_house3['values'] = human_name
            text_class.insert(END, f'{human}\n')
        text_class.config(state="disabled")

    def add_human():

        try:
            name = entry_by_house.get()
            age = entry_by_house2.get()
            if not name or not age:
                raise ExceptionNullField("Одно из полей пустое")  # Генерация ошибки если поле пустое
        except ExceptionNullField:
            mb.showwarning(f"Ошибка,", 'Не все данные заполнены!')
        else:
            try:
                age, check = value_check_func(age)
                if check is False:
                    raise ExceptionStrInNumber("Вместо цифры в поле -строка")  # Генерация ошибки если поле строка
                elif age <= 0:
                    raise ZeroDivisionError("Невозможное значение для этого поля")
            except ExceptionStrInNumber:
                mb.showwarning(f"Ошибка,", 'Вы ввели не число')
            except ZeroDivisionError:
                mb.showwarning(f"Ошибка,", 'Проверьте значение возраста')
            else:

                new_hum = Human(name, age)
                new_human.append(new_hum)

                entry_by_house.delete(0, END)
                entry_by_house2.delete(0, END)
                on_screen_human()

    def add_home():

        try:
            temp_house_name = entry_by_house3.get()
            price = entry_by_house4.get()
            if not temp_house_name or not price:
                raise ExceptionNullField("Одно из полей пустое")  # Генерация ошибки если поле пустое
        except ExceptionNullField:
            mb.showwarning(f"Ошибка,", 'Не все данные заполнены!')
        else:
            try:
                price, check = value_check_func(price)
                if check is False:
                    raise ExceptionStrInNumber("Вместо цифры в поле -строка")  # Генерация ошибки если поле строка
                elif price <= 0:
                    raise ZeroDivisionError("Невозможное значение для этого поля")
            except ExceptionStrInNumber:
                mb.showwarning(f"Ошибка,", 'Вы ввели не число')
            except ZeroDivisionError:
                mb.showwarning(f"Ошибка,", 'Бесплатные дома закончились>')

            else:

                new_house_temp = House(temp_house_name, price)
                new_house.append(new_house_temp)

                entry_by_house3.delete(0, END)
                entry_by_house4.delete(0, END)

                house_name.clear()
                for house in new_house:
                    house_name.append(house.name)
                    combobox_by_house2['values'] = house_name

    def add_earn_money():

        try:
            temp_str = combobox_by_house.get()
            temp_salary = entry_by_house5.get()
            if not temp_str or not temp_salary:
                raise ExceptionNullField("Одно из полей пустое")  # Генерация ошибки если поле пустое
        except ExceptionNullField:
            mb.showwarning(f"Ошибка,", 'Не все данные заполнены!')
        else:
            try:
                temp_salary, check = value_check_func(temp_salary)
                if check is False:
                    raise ExceptionStrInNumber("Вместо цифры в поле -строка")  # Генерация ошибки если поле строка
                elif temp_salary <= 0:
                    raise ZeroDivisionError("Невозможное значение для этого поля")
            except ExceptionStrInNumber:
                mb.showwarning(f"Ошибка,", 'Вы ввели не число')
            except ZeroDivisionError:
                mb.showwarning(f"Ошибка,", 'Смысл начислять зп 0?')

            for i in new_human:  # Прогонка по списку в цикле с обращением к переменной как к полям класса
                if i.name == temp_str:
                    i.earn_money(temp_salary)
            on_screen_human()

    def add_by_house():

        try:
            temp_discount = entry_by_house6.get()
            temp_house = combobox_by_house2.get()
            temp_human = combobox_by_house3.get()
            if not temp_house or not temp_human:
                raise ExceptionNullField("Одно из полей пустое")  # Генерация ошибки если поле пустое
        except ExceptionNullField:
            mb.showwarning(f"Ошибка,", 'Не все данные заполнены!')
        else:
            try:
                if temp_discount == '':
                    temp_discount = 0  # Скидка по умолчанию

                temp_discount, check = value_check_func(temp_discount)

                if check is False:
                    raise ExceptionStrInNumber("Вместо цифры в поле -строка")  # Генерация ошибки если поле строка
                elif temp_discount < 0:
                    raise ZeroDivisionError("Невозможное значение для этого поля")
            except ExceptionStrInNumber:
                mb.showwarning(f"Ошибка,", 'Вы ввели не число')
            except ZeroDivisionError:
                mb.showwarning(f"Ошибка,", 'Скидка не может быть меньше 0')

            for i in new_human:  # Прогонка по списку в цикле с обращением к переменной как к полям класса
                if i.name == temp_human:
                    for j in new_house:
                        if j.name == temp_house:
                            i.buy_house(j, temp_discount)
            on_screen_human()

    def on_save():

        with open('list_human.txt', 'w') as text_file:
            for i in new_human:
                text_file.writelines(f'{str(i)}')

        with open('list_house.txt', 'w') as text_file:
            for j in new_house:
                # text_file.writelines(f'{str(j)}\n')
                text_file.writelines(f'{str(j)}')

    # def on_load():
    #     a = 0
    #     with open('list_human.txt', 'r') as text_file:
    #         temp_line = text_file.readlines()
    #         new_human = temp_line
    #         on_screen_human()

    def on_close():  # Кнопка закрытия на крестик

        human_by_house_menu.destroy()

    human_by_house.protocol('WM_DELETE_WINDOW', on_close)

    # end region

    # region Рисование кнопок и подписей вкладки программы

    # Первая вкладка

    lab_by_house = Label(human_by_house, text='Покупка дома человеком(классы)', font='Arial 12 bold',
                         borderwidth=2, relief="solid")
    lab_by_house.place(x=10, y=20, width=580, height=25)

    lab_by_house2 = Label(human_by_house, text='Добавьте людей которые могут купить и дома которые можно купить',
                          font='Arial 12 bold', borderwidth=2, relief="solid")
    lab_by_house2.place(x=10, y=65, width=580, height=25)

    lab_by_house3 = Label(human_by_house, text='Данные человека', font='Arial 9 bold', borderwidth=2, relief="solid")
    lab_by_house3.place(x=10, y=100, width=280, height=25)

    lab_by_house8 = Label(human_by_house, text='Данные дома', font='Arial 9 bold', borderwidth=2, relief="solid")
    lab_by_house8.place(x=300, y=100, width=280, height=25)

    lab_by_house4 = Label(human_by_house, text='Имя', font='Arial 9 bold')
    lab_by_house4.place(x=10, y=135, width=135, height=25)

    lab_by_house5 = Label(human_by_house, text='Возраст', font='Arial 9 bold')
    lab_by_house5.place(x=155, y=135, width=135, height=25)

    lab_by_house6 = Label(human_by_house, text='Название', font='Arial 9 bold')
    lab_by_house6.place(x=300, y=135, width=135, height=25)

    lab_by_house7 = Label(human_by_house, text='Цена', font='Arial 9 bold')
    lab_by_house7.place(x=445, y=135, width=135, height=25)

    entry_by_house = Entry(human_by_house, font='Arial 10 bold', width=15, borderwidth=2)
    entry_by_house.place(x=10, y=170, width=135, height=30)
    entry_by_house2 = Entry(human_by_house, font='Arial 10 bold', width=15, borderwidth=2)
    entry_by_house2.place(x=155, y=170, width=135, height=30)
    entry_by_house3 = Entry(human_by_house, font='Arial 10 bold', width=15, borderwidth=2)
    entry_by_house3.place(x=300, y=170, width=135, height=30)
    entry_by_house4 = Entry(human_by_house, font='Arial 10 bold', width=15, borderwidth=2)
    entry_by_house4.place(x=445, y=170, width=135, height=30)

    button_by_house1 = Button(human_by_house, text='Добавить человека', font='Arial 12 bold ',
                              command=add_human, borderwidth=2)
    button_by_house1.place(x=10, y=210, width=280, height=30)
    button_by_house2 = Button(human_by_house, text='Добавить дом', font='Arial 12 bold ',
                              command=add_home, borderwidth=2)
    button_by_house2.place(x=300, y=210, width=280, height=30)

    lab_by_house9 = Label(human_by_house, text='Выберите человека для начисления зп', font='Arial 9 bold',
                          borderwidth=2, relief="solid")
    lab_by_house9.place(x=25, y=280, width=250, height=25)

    lab_by_house10 = Label(human_by_house, text='Выберите дом и человека для покупки', font='Arial 9 bold',
                           borderwidth=2, relief="solid")
    lab_by_house10.place(x=315, y=280, width=250, height=25)

    combobox_by_house = ttk.Combobox(human_by_house, values=human_name, state="readonly")
    combobox_by_house.place(x=10, y=315, width=135, height=30)

    entry_by_house5 = Entry(human_by_house, font='Arial 10 bold', width=15, borderwidth=2)
    entry_by_house5.place(x=155, y=315, width=135, height=30)

    button_by_house3 = Button(human_by_house, text='Начислить', font='Arial 12 bold ',
                              command=add_earn_money, borderwidth=2)
    button_by_house3.place(x=10, y=355, width=280, height=30)

    combobox_by_house2 = ttk.Combobox(human_by_house, values=house_name, state="readonly")
    combobox_by_house2.place(x=315, y=315, width=120, height=30)

    combobox_by_house3 = ttk.Combobox(human_by_house, values=human_name, state="readonly")
    combobox_by_house3.place(x=445, y=315, width=120, height=30)

    lab_by_house11 = Label(human_by_house, text='Скидка', font='Arial 9 bold')
    lab_by_house11.place(x=315, y=355, width=120, height=30)

    entry_by_house6 = Entry(human_by_house, font='Arial 10 bold', width=15, borderwidth=2)
    entry_by_house6.place(x=445, y=355, width=120, height=30)

    button_by_house3 = Button(human_by_house, text='Купить дом', font='Arial 12 bold ',
                              command=add_by_house, borderwidth=2)
    button_by_house3.place(x=315, y=395, width=250, height=30)

    text_class = Text(human_by_house, font='Arial 10', width=15, borderwidth=2, wrap="word", state="disabled")
    text_class.place(x=10, y=690, width=580, height=100)

    button_save = Button(human_by_house, text='Сохранить данные в файл', font='Arial 12 bold ',
                         command=on_save, borderwidth=2)
    button_save.place(x=10, y=610, width=580, height=30)

    button_exit = Button(human_by_house, text='Выход', font='Arial 12 bold ', command=on_close, borderwidth=2)
    button_exit.place(x=10, y=800, width=580, height=30)

    # endregion


# region Функции вкладки меню


def get_exit():
    human_by_house_menu.destroy()


# endregion

# region Рисование кнопок и подписей вкладки меню


lab_menu = Label(human_by_house_menu, text='Произвольное задание по классам. Покупка дома', font='Arial 15 bold')
lab_menu.place(x=10, y=450, width=580, height=30)

button_main_menu = Button(human_by_house_menu, text='Войти в программу', font='Arial 12 ', command=get_enter,
                          borderwidth=2)
button_main_menu.place(x=10, y=490, width=580, height=30)
button_main_menu2 = Button(human_by_house_menu, text='Выход', font='Arial 12 ', command=get_exit, borderwidth=2)
button_main_menu2.place(x=10, y=530, width=580, height=30)

human_by_house_menu.protocol('WM_DELETE_WINDOW', get_exit)

human_by_house_menu.mainloop()

# endregion
