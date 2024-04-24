from tkinter import *  # Добавляем библиотеку Ткинтер
from tkinter import ttk  # Добавляем модуль Ткинтера
from My_Function import *  # Добавляем библиотеку Function
from importlib import import_module

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
        print(f'Заработано: {money}. Итого в наличии {self.money}')

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.money < price:
            print(f'К сожалению денег на дом не хватает. Нужно еще {price - self.money}')
        else:
            self.__make_deal(house, price)


class House:

    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        print(f'Цена за дом: {self._price} со скидкой {discount} составляет {final_price}')
        return final_price


class SmallHouse(House):
    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)

        self._price = price


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
        for human in new_human:
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

            except ExceptionStrInNumber:
                mb.showwarning(f"Ошибка,", 'Вы ввели не число')

            else:

                new_hum = Human(name, age)
                new_human.append(new_hum)

                entry_by_house.delete(0, END)
                entry_by_house2.delete(0, END)
                on_screen_human()
                d = repr(new_human)
                for i in new_human:         # Прогонка по списку в цикле с обращениемк к переменной как к полям класса
                                                # код верменный всунутьв кнопку
                    if i.name == 'Alex':
                        i.earn_money(5000)
                a = 0

    def add_home():

        try:
            house_name = entry_by_house3.get()
            price = entry_by_house4.get()
            if not house_name or not price:
                raise ExceptionNullField("Одно из полей пустое")  # Генерация ошибки если поле пустое
        except ExceptionNullField:
            mb.showwarning(f"Ошибка,", 'Не все данные заполнены!')
        else:
            try:
                price, check = value_check_func(price)
                if check is False:
                    raise ExceptionStrInNumber("Вместо цифры в поле -строка")  # Генерация ошибки если поле строка

            except ExceptionStrInNumber:
                mb.showwarning(f"Ошибка,", 'Вы ввели не число')

            else:
                new_house.append(House(house_name, price))
                text_class.config(state="normal")
                text_class.delete('1.0', END)
                text_class.insert(END, f'{new_house}')
                text_class.config(state="disabled")

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

    lab_by_house10 = Label(human_by_house, text='Выберите человека и дом для покупки', font='Arial 9 bold',
                           borderwidth=2, relief="solid")
    lab_by_house10.place(x=315, y=280, width=250, height=25)

    # combobox_tab3 = ttk.Combobox(human_by_house, values = Human.name, state="readonly")
    # combobox_tab3.place(x=10, y=120, width=480, height=30)

    #
    # button_lab_imt = Button(lesson_8, text='Рассчитать', font='Arial 12 bold ', command=calculate_imt, borderwidth=2)
    # button_lab_imt.place(x=10, y=165, width=580, height=30)
    #
    text_class = Text(human_by_house, font='Arial 10', width=15, borderwidth=2, wrap="word", state="disabled")
    text_class.place(x=10, y=690, width=580, height=100)

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

#
# if __name__ == '__main__':
#     # Human.defaultinfo()
#     Deniska = Human('Дениска', 42)
#     Deniska.info()
#     Deniska.earn_money(5000)
#     # Human.defaultinfo()
#     # a = 0
#     #
#     lof_house = SmallHouse(15000)
#     Deniska.buy_house(lof_house, 10)
#     #
#     Deniska.earn_money(20000)
#     Deniska.buy_house(lof_house, 10)
#     Deniska.info()
