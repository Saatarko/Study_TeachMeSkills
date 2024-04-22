from tkinter import *  # Добавляем библиотеку Ткинтер
from tkinter import ttk  # Добавляем модуль Ткинтера
import time
from My_Function import *  # Добавляем библиотеку Function

# region Объявление класса для меню и расчеты окна
# Объявляем класс
lesson_7_main_menu = Tk()

lesson_7_main_menu.title("Домашнее задание по теме 7")

# Получаем ширину и высоту экрана

screen_width = lesson_7_main_menu.winfo_screenwidth()
screen_height = lesson_7_main_menu.winfo_screenheight()

# Вычисляем координаты окна приложения
window_width = 600
window_height = 860
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

lesson_7_main_menu.geometry(f"{window_width}x{window_height}+{x}+{y}")
lesson_7_main_menu.resizable(None, None)  # Запрещаем изменять размер окна
lesson_7_main_menu["bg"] = "gray22"  # gray gray0-99   # Устанавливаем цвет фона

flat_dict = []  # Глобальная переменная для хранения словаря с данными квартиры


# endregion


def get_enter():  # Создаем подкласс (второе окно)
    lesson_7_main_menu.withdraw()
    lesson_7 = Toplevel(lesson_7_main_menu)
    lesson_7.title("Домашнее задание по теме 7")
    lesson_7.geometry(f"{window_width}x{window_height}+{x}+{y}")
    lesson_7.resizable(None, None)
    lesson_7["bg"] = "gray22"
    tab_control = ttk.Notebook(lesson_7)  # создаем подкласс для закладок

    tab1 = ttk.Frame(tab_control)  # создаем закладки
    tab2 = ttk.Frame(tab_control)

    tab_control.add(tab1, text='Списки и функции над ними')
    tab_control.add(tab2, text='Рассчет площади квартиры')
    tab_control.pack(expand=1, fill='both')

    def get_list_deco():
        temp_str = ''
        temp_list = entry_list_deco_tab1.get()
        if temp_list != '':
            temp_str = entry_list_deco2_tab1.get()
            if temp_str != '':
                temp_str += ',' + temp_list
            else:
                temp_str += temp_list

            entry_list_deco2_tab1.config(state="normal")
            entry_list_deco_tab1.delete(0, END)
            entry_list_deco2_tab1.delete(0, END)
            entry_list_deco2_tab1.insert(END, temp_str)
            entry_list_deco2_tab1.config(state="readonly")



    def timeit(func):
        import time

        def wrapper(*args, **kwargs):
            start = time.time()
            return_value = func(*args, **kwargs)
            end = time.time()
            t = (end - start)
            return return_value, t

        return wrapper

    def data_digit():

        text_list_deco_tab1.config(state="normal")
        text_list_deco_tab1.delete('1.0', END)
        text_list_deco_tab1.config(state="disabled")

        temp_str = entry_list_deco2_tab1.get()

        digit_func = timeit(digit_func_count)  # декорируем нашу функцию фукнцией времени

        result_str, t = digit_func(temp_str)  # вызываем отдекорированную функцию принимая уже 2 элемента

        text_list_deco_tab1.config(state="normal")
        text_list_deco_tab1.delete('1.0', END)
        text_list_deco_tab1.insert(END, f'Итоговый список {result_str} был сформирован за время {t:.10f} с')
        text_list_deco_tab1.config(state="disabled")

    def null_filter_func():  # Кнопка очищения полей для списка чисел

        text_list_deco_tab1.config(state="normal")
        text_list_deco_tab1.delete('1.0', END)
        text_list_deco_tab1.config(state="disabled")

        temp_str = entry_list_deco2_tab1.get()

        digit_func = timeit(digit_null_count)  # декорируем нашу функцию функцией времени

        result_str, t = digit_func(temp_str)  # вызываем отдекорированную функцию принимая уже 2 элемента

        text_list_deco_tab1.config(state="normal")
        text_list_deco_tab1.delete('1.0', END)
        text_list_deco_tab1.insert(END, f'Итоговый список {result_str} был сформирован за время {t:.10f} с')
        text_list_deco_tab1.config(state="disabled")

    def str_filter_func():

        text_list_deco_tab1.config(state="normal")
        text_list_deco_tab1.delete('1.0', END)
        text_list_deco_tab1.config(state="disabled")

        temp_str = entry_list_deco2_tab1.get()

        digit_func = timeit(str_count)  # декорируем нашу функцию функцией времени

        result_str, t = digit_func(temp_str)  # вызываем отдекорированную функцию принимая уже 2 элемента

        if  result_str == '':
            text_list_deco_tab1.config(state="normal")
            text_list_deco_tab1.delete('1.0', END)
            text_list_deco_tab1.insert(END, f'Палиндромов не обнаружено, затраченное время {t:.10f} с')
            text_list_deco_tab1.config(state="disabled")
        else:
            text_list_deco_tab1.config(state="normal")
            text_list_deco_tab1.delete('1.0', END)
            text_list_deco_tab1.insert(END, f'Палиндромы в списке {result_str}. Список был сформирован за время {t:.10f} с')
            text_list_deco_tab1.config(state="disabled")


    def add_flat_room():

        temp_name = entry_flat_count3_tab2.get()
        temp_length = entry_flat_count4_tab2.get()
        temp_width = entry_flat_count5_tab2.get()

        temp_length, check_reserve = check_value(temp_length, 'digit')
        temp_width, check_reserve2 = check_value(temp_width, 'digit')

        if check_reserve is True and check_reserve2 is True:
            room_dist = {'name': temp_name, 'length': temp_length, 'width': temp_width}
            flat_dict.append(room_dist)

        entry_flat_count3_tab2.delete(0, END)
        entry_flat_count4_tab2.delete(0, END)
        entry_flat_count5_tab2.delete(0, END)

        text_flat_count3_tab2.config(state="normal")
        text_flat_count3_tab2.delete('1.0', END)
        text_flat_count3_tab2.insert(END, f' Квартира состоит из{flat_dict}')
        text_flat_count3_tab2.config(state="disabled")


    def clear_data():  # Кнопка очищения полей для списка чисел

        entry_list_deco2_tab1.config(state="normal")
        entry_list_deco2_tab1.delete(0, END)
        entry_list_deco2_tab1.config(state="readonly")

    def clear_text_data():

        text_list_deco_tab1.config(state="normal")
        text_list_deco_tab1.delete('1.0', END)
        text_list_deco_tab1.config(state="disabled")

    def on_close():
        lesson_7_main_menu.destroy()

    lesson_7.protocol('WM_DELETE_WINDOW', on_close)

    # region Рисование кнопок и подписей вкладки программы

    # Первая вкладка

    lab_list_deco_tab1 = Label(tab1, text='Всякое интересное со списками декораторами и ф-циями MAP/Filter/Reduce',
                               font='Arial 10 bold', borderwidth=2, relief="solid")
    lab_list_deco_tab1.place(x=10, y=20, width=580, height=25)

    lab_list_deco2_tab1 = Label(tab1, text='Поэлементно добавьте данные', font='Arial 9 bold',
                                borderwidth=2, relief="solid")
    lab_list_deco2_tab1.place(x=10, y=50, width=580, height=25)

    entry_list_deco_tab1 = Entry(tab1, font='Arial 10 bold', width=15, borderwidth=2)
    entry_list_deco_tab1.place(x=10, y=80, width=400, height=30)

    button_list_deco_tab1 = Button(tab1, text='Добавить', font='Arial 10 ', command=get_list_deco, borderwidth=2)
    button_list_deco_tab1.place(x=420, y=80, width=170, height=30)

    lab_list_deco3_tab1 = Label(tab1, text='Итоговый список чисел/строк', font='Arial 9 bold',
                                borderwidth=2, relief="solid")
    lab_list_deco3_tab1.place(x=10, y=120, width=580, height=25)

    entry_list_deco2_tab1 = Entry(tab1, font='Arial 10 bold', width=15, borderwidth=2, state='readonly')
    entry_list_deco2_tab1.place(x=10, y=150, width=400, height=30)

    button_list_deco2_tab1 = Button(tab1, text='Очистить', font='Arial 10 ', command=clear_data, borderwidth=2)
    button_list_deco2_tab1.place(x=420, y=150, width=170, height=30)

    button_list_deco3_tab1 = Button(tab1, text='Строкуем цифр.список', font='Arial 10 ', command=data_digit,
                                    borderwidth=2)
    button_list_deco3_tab1.place(x=10, y=190, width=185, height=30)

    button_list_deco4_tab1 = Button(tab1, text='Filter >0', font='Arial 10 ', command=null_filter_func, borderwidth=2)
    button_list_deco4_tab1.place(x=205, y=190, width=185, height=30)

    button_list_deco5_tab1 = Button(tab1, text='Палиндромы', font='Arial 10 ', command=str_filter_func, borderwidth=2)
    button_list_deco5_tab1.place(x=400, y=190, width=185, height=30)

    lab_list_deco4_tab1 = Label(tab1, text='Итоговый результат', font='Arial 9 bold')
    lab_list_deco4_tab1.place(x=10, y=230, width=580, height=25)

    text_list_deco_tab1 = Text(tab1, font='Arial 10', width=15, borderwidth=2, wrap="char", state="disabled")
    text_list_deco_tab1.place(x=10, y=265, width=440, height=60)

    button_list_deco6_tab1 = Button(tab1, text='Очистить', font='Arial 10 ', command=clear_text_data, borderwidth=2)
    button_list_deco6_tab1.place(x=460, y=265, width=120, height=60)

    button_list_deco6_tab1 = Button(tab1, text='Очистить', font='Arial 10 ', command=clear_text_data, borderwidth=2)
    button_list_deco6_tab1.place(x=460, y=265, width=120, height=60)

    button_list_deco7_tab1 = Button(tab1, text='Выход', font='Arial 12 bold ', command=on_close, borderwidth=2)
    button_list_deco7_tab1.place(x=10, y=800, width=580, height=30)

    lab_flat_count_tab2 = Label(tab2, text='Расчет площади квартиры', font='Arial 10 bold', borderwidth=2,
                                relief="solid")
    lab_flat_count_tab2.place(x=10, y=20, width=580, height=25)

    lab_flat_count2_tab2 = Label(tab2, text='Для расчета добавьте поочередно комнаты с габаритами', font='Arial 9 bold')
    lab_flat_count2_tab2.place(x=10, y=50, width=580, height=25)

    lab_flat_count3_tab2 = Label(tab2, text='Название', font='Arial 9 bold')
    lab_flat_count3_tab2.place(x=10, y=85, width=180, height=25)

    lab_flat_count4_tab2 = Label(tab2, text='Длинна', font='Arial 9 bold')
    lab_flat_count4_tab2.place(x=200, y=85, width=180, height=25)

    lab_flat_count5_tab2 = Label(tab2, text='Ширина', font='Arial 9 bold')
    lab_flat_count5_tab2.place(x=390, y=85, width=180, height=25)

    entry_flat_count3_tab2 = Entry(tab2, font='Arial 10 bold', width=15, borderwidth=2)
    entry_flat_count3_tab2.place(x=10, y=120, width=180, height=30)

    entry_flat_count4_tab2 = Entry(tab2, font='Arial 10 bold', width=15, borderwidth=2)
    entry_flat_count4_tab2.place(x=200, y=120, width=180, height=30)

    entry_flat_count5_tab2 = Entry(tab2, font='Arial 10 bold', width=15, borderwidth=2)
    entry_flat_count5_tab2.place(x=390, y=120, width=180, height=30)

    button_flat_count8_tab1 = Button(tab2, text='Добавить', font='Arial 12 bold ', command=add_flat_room, borderwidth=2)
    button_flat_count8_tab1.place(x=10, y=160, width=580, height=30)

    text_flat_count3_tab2 = Text(tab2, font='Arial 10', width=15, borderwidth=2, wrap="char", state="disabled")
    text_flat_count3_tab2.place(x=10, y=200, width=580, height=60)

    # endregion


# region Функции вкладки меню


def get_exit():
    lesson_7_main_menu.destroy()


# endregion

# region Рисование кнопок и подписей вкладки меню


lab_menu = Label(lesson_7_main_menu, text='Домашнее задание по теме 7', font='Arial 20 bold')
lab_menu.place(x=10, y=450, width=580, height=30)

button_main_menu = Button(lesson_7_main_menu, text='Войти в программу', font='Arial 12 ', command=get_enter,
                          borderwidth=2)
button_main_menu.place(x=10, y=490, width=580, height=30)
button_main_menu2 = Button(lesson_7_main_menu, text='Выход', font='Arial 12 ', command=get_exit, borderwidth=2)
button_main_menu2.place(x=10, y=530, width=580, height=30)

lesson_7_main_menu.protocol('WM_DELETE_WINDOW', get_exit)

lesson_7_main_menu.mainloop()

# endregion
