from tkinter import *  # Добавляем библиотеку Ткинтер
from tkinter import ttk  # Добавляем модуль Ткинтера
from tkinter import messagebox as mb

from My_Function import *  # Добавляем библиотеку Function
from functools import reduce

# region Объявление класса для меню и расчеты окна
# Объявляем класс
lesson_8_main_menu = Tk()

lesson_8_main_menu.title("Домашнее задание по теме 8")

# Получаем ширину и высоту экрана

screen_width = lesson_8_main_menu.winfo_screenwidth()
screen_height = lesson_8_main_menu.winfo_screenheight()

# Вычисляем координаты окна приложения
window_width = 600
window_height = 860
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

lesson_8_main_menu.geometry(f"{window_width}x{window_height}+{x}+{y}")
lesson_8_main_menu.resizable(None, None)  # Запрещаем изменять размер окна
lesson_8_main_menu["bg"] = "gray22"  # gray gray0-99   # Устанавливаем цвет фона


class MyException(Exception):
    """Мой класс для исключений"""


class ExceptionNullField(MyException):
    """Класс для исключений на пустые поля"""


class ExceptionStrInNumber(MyException):
    """Класс для исключений на введение строк в цифровые поля"""


class ExceptionNegativeNumber(MyException):
    """Класс для исключений на введение отрицательных чисел """
    pass


def get_enter():  # Создаем подкласс (второе окно)
    lesson_8_main_menu.withdraw()
    lesson_8 = Toplevel(lesson_8_main_menu)
    lesson_8.title("Домашнее задание по теме 8")
    lesson_8.geometry(f"{window_width}x{window_height}+{x}+{y}")
    lesson_8.resizable(None, None)
    lesson_8["bg"] = "gray90"

    # region функции основной программы

    def calculate_imt():

        try:
            weight = entry_lab_imt.get()
            height = entry_lab_imt2.get()
            if not weight or not height:
                raise ExceptionNullField("Одно из полей пустое")
        except ExceptionNullField:
            mb.showwarning(f"Ошибка,", 'Не все данные заполнены!')
        else:
            try:
                height, check = value_check_func(height)
                weight, check2 = value_check_func(weight)
                if check is False or check2 is False:
                    raise ExceptionStrInNumber("Вместо цифры в поле -строка")
                elif height < 0 or weight < 0:
                    raise ExceptionNegativeNumber("Для данного поля отрицательно число не допустимо")
                elif height == 0 or weight == 0:
                    raise ZeroDivisionError("Нулевое значение в цировом поле или деление на 0")
            except ExceptionStrInNumber:
                mb.showwarning(f"Ошибка,", 'Вы ввели не число')
            except ExceptionNegativeNumber:
                mb.showwarning(f"Ошибка,", 'Не может быть отрицательных чисел')

                # да, вес не приводит к делению на 0, но удобно использовать для обоих случаев
            except ZeroDivisionError:
                mb.showwarning(f"Ошибка,", 'Рост и вес не могут быть нулевыми')
            else:

                try:

                    imt = weight / ((height / 100) ** 2)
                    imt_from_dist = list(map(lambda z: z.get('imt'), imt_dict))
                    temp = list(filter(lambda s: s >= imt, imt_from_dist))
                    result_list = list([i for i in imt_dict if i['imt'] == temp[0]])

                    result_list_type = list(map(lambda z: z.get('type'), result_list))
                    result_list_risk = list(map(lambda z: z.get('risk'), result_list))

                    result_list_type = ' '.join(result_list_type)
                    result_list_risk = ' '.join(result_list_risk)

                    if result_list_type == 'Дефицит массы тела':
                        diseases = 'Но повышены риски развития остеопороза, анемии.'
                    elif result_list_type == 'Нормальная масса тела':
                        diseases = 'Все супер продолжайте в том же духе.'
                    else:
                        diseases = ('Могут возникнуть проблемы с сердечно-сосудистой системой, '
                                    'развиться диабет, гипертония.')

                    text_lab.config(state="normal")
                    text_lab.delete('1.0', END)
                    text_lab.insert(END, f'Индекс массы тела составляет {imt} \n'
                                         f'Тип массы тела - {result_list_type} \nРиск'
                                         f' заболеваний связанных с избыточным весом- {result_list_risk}. {diseases}')
                    text_lab.config(state="disabled")

                except ZeroDivisionError:
                    mb.showwarning(f"Ошибка,", 'Рост и вес не могут быть нулевыми')

    def on_close():  # Кнопка закрытия на крестик

        lesson_8_main_menu.destroy()

    lesson_8.protocol('WM_DELETE_WINDOW', on_close)

    imt_dict = [  # список словарей для результатов по IMt
        {"imt": 18, "type": "Дефицит массы тела", "risk": "Низкий"},
        {"imt": 25, "type": "Нормальная масса тела", "risk": "Обычный", },
        {"imt": 30, "type": "Избыточная масса тела (предожирение)", "risk": "Низкий"},
        {"imt": 35, "type": "Ожирение I степени", "risk": "Высокий"},
        {"imt": 40, "type": "Ожирение II степени", "risk": "Очень высокий"},
        {"imt": 100, "type": "Ожирение III степени", "risk": "Чрезвычайно высокий"}
    ]

    # end region

    # region Рисование кнопок и подписей вкладки программы

    # Первая вкладка

    lab_imt = Label(lesson_8, text='Расчет Индекса Массы Тела (ИМТ) и операции над числами', font='Arial 12 bold',
                    borderwidth=2, relief="solid")
    lab_imt.place(x=10, y=20, width=580, height=25)

    lab_imt2 = Label(lesson_8, text='Для расчета ИМТ введите массу тела и рост', font='Arial 9 bold', borderwidth=2,
                     relief="solid")
    lab_imt2.place(x=10, y=55, width=580, height=25)

    lab_imt2 = Label(lesson_8, text='Масса тела в кг', font='Arial 9 bold')
    lab_imt2.place(x=10, y=90, width=280, height=25)

    lab_imt3 = Label(lesson_8, text='Рост в см', font='Arial 9 bold')
    lab_imt3.place(x=300, y=90, width=280, height=25)

    entry_lab_imt = Entry(lesson_8, font='Arial 10 bold', width=15, borderwidth=2)
    entry_lab_imt.place(x=10, y=125, width=280, height=30)

    entry_lab_imt2 = Entry(lesson_8, font='Arial 10 bold', width=15, borderwidth=2)
    entry_lab_imt2.place(x=300, y=125, width=280, height=30)

    button_lab_imt = Button(lesson_8, text='Рассчитать', font='Arial 12 bold ', command=calculate_imt, borderwidth=2)
    button_lab_imt.place(x=10, y=165, width=580, height=30)

    text_lab = Text(lesson_8, font='Arial 10', width=15, borderwidth=2, wrap="word", state="disabled")
    text_lab.place(x=10, y=205, width=580, height=100)

    lab_imt4 = Label(lesson_8, text='Операции над числами', font='Arial 9 bold', borderwidth=2,
                     relief="solid")
    lab_imt4.place(x=10, y=315, width=580, height=25)

    lab_imt5 = Label(lesson_8, text='Введите первое число', font='Arial 9 bold')
    lab_imt5.place(x=10, y=350, width=280, height=25)

    lab_imt6 = Label(lesson_8, text='Введите второе число', font='Arial 9 bold')
    lab_imt6.place(x=300, y=350, width=280, height=25)

    entry_lab_imt3 = Entry(lesson_8, font='Arial 10 bold', width=15, borderwidth=2)
    entry_lab_imt3.place(x=10, y=385, width=280, height=30)

    entry_lab_imt4 = Entry(lesson_8, font='Arial 10 bold', width=15, borderwidth=2)
    entry_lab_imt4.place(x=300, y=385, width=280, height=30)

    button_plus = Button(lesson_8, text='Сложить', font='Arial 12 bold ', command=lambda: calculate_number('+'), borderwidth=2)
    button_plus.place(x=10, y=425, width=280, height=30)
    button_minus = Button(lesson_8, text='Вычесть', font='Arial 12 bold ', command=calculate_imt, borderwidth=2)
    button_minus.place(x=300, y=425, width=280, height=30)
    button_multiply = Button(lesson_8, text='Умножить', font='Arial 12 bold ', command=calculate_imt, borderwidth=2)
    button_multiply.place(x=10, y=465, width=280, height=30)
    button_divide = Button(lesson_8, text='Разделить', font='Arial 12 bold ', command=calculate_imt, borderwidth=2)
    button_divide.place(x=300, y=465, width=280, height=30)

    # endregion


# region Функции вкладки меню


def get_exit():
    lesson_8_main_menu.destroy()


# endregion

# region Рисование кнопок и подписей вкладки меню


lab_menu = Label(lesson_8_main_menu, text='Домашнее задание по теме 8', font='Arial 20 bold')
lab_menu.place(x=10, y=450, width=580, height=30)

button_main_menu = Button(lesson_8_main_menu, text='Войти в программу', font='Arial 12 ', command=get_enter,
                          borderwidth=2)
button_main_menu.place(x=10, y=490, width=580, height=30)
button_main_menu2 = Button(lesson_8_main_menu, text='Выход', font='Arial 12 ', command=get_exit, borderwidth=2)
button_main_menu2.place(x=10, y=530, width=580, height=30)

lesson_8_main_menu.protocol('WM_DELETE_WINDOW', get_exit)

lesson_8_main_menu.mainloop()

# endregion
