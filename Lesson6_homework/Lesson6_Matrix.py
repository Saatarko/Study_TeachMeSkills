from tkinter import *  # Добавляем библиотеку Ткинтер
from tkinter import ttk  # Добавляем модуль Ткинтера

import numpy as np

from My_Function import *  # Добавляем библиотеку Function


# region Объявление класса для меню и расчеты окна
# Объявляем класс
lesson_6_main_menu = Tk()

lesson_6_main_menu.title("Расчеты по теме 6. Матрицы")

# Получаем ширину и высоту экрана

screen_width = lesson_6_main_menu.winfo_screenwidth()
screen_height = lesson_6_main_menu.winfo_screenheight()

# Вычисляем координаты окна приложения
window_width = 990
window_height = 860
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

lesson_6_main_menu.geometry(f"{window_width}x{window_height}+{x}+{y}")
lesson_6_main_menu.resizable(None, None)  # Запрещаем изменять размер окна
lesson_6_main_menu["bg"] = "gray22"  # gray gray0-99   # Устанавливаем цвет фона

matrix = []  # Глобальная переменная для хранения матрицы(чтобы не гонять ее по функциям)
matrix_one = []  # Глобальная переменная для хранения матрицы единиц и нулей(чтобы не гонять ее по функциям)


# endregion


def get_enter():   # Создаем подкласс (второе окно)
    lesson_6_main_menu.withdraw()
    lesson_6 = Toplevel(lesson_6_main_menu)
    lesson_6.title("Расчеты по теме 6. Матрицы")
    lesson_6.geometry(f"{window_width}x{window_height}+{x}+{y}")
    lesson_6.resizable(None, None)
    lesson_6["bg"] = "gray22"
    tab_control = ttk.Notebook(lesson_6)  # создаем подкласс для закладок

    tab1 = ttk.Frame(tab_control)  # создаем закладки
    tab2 = ttk.Frame(tab_control)

    tab_control.add(tab1, text='Матрицы. Часть1')
    tab_control.add(tab2, text='Матрицы. Часть2')
    tab_control.pack(expand=1, fill='both')

    def on_close():
        mb.showinfo(f"Не-а", 'Выход на кнопку - ВЫХОД!')

    lesson_6.protocol('WM_DELETE_WINDOW', on_close)

    # region Функции основной программы
    def get_data_matrix():  # Функция получения данных из матрицы
        line = entry_matrix1_tab1.get()
        column = entry_matrix2_tab1.get()
        line, check_reserve = check_value(line, 'digit')
        column, check_reserve2 = check_value(column, 'digit')

        if check_reserve is True and check_reserve2 is True:  # Проверка на размерность
            if line > 5 or column > 5:
                mb.showwarning(f"Предупреждение", 'Русским по белому же написано максимальные размеры 5*5')
            elif line == 0 or column == 0:
                mb.showwarning(f"Предупреждение", 'Один из размеров матрицы не задан')
            else:
                global matrix   # Разрешение на изменение глобальной переменной
                matrix = np.random.randint(0, 99, (line, column))  # Создание матрицы с рандомными числами
                text_matrix1_tab1.config(state="normal")
                text_matrix1_tab1.delete('1.0', END)
                text_matrix1_tab1.insert(END, matrix)
                text_matrix1_tab1.config(state="disabled")

    def get_data_matrix_minmax():
        try:
            if not matrix:   # Проверка на создание матрицы
                mb.showwarning(f"Предупреждение", 'Матрица не создана')
        except ValueError:
            min_value = int(np.min(matrix))   # Поиск минимального значения и переформатирование результата в строку
            min_value_index = np.where(matrix == min_value)
            temp = ' '.join(map(str, min_value_index))

            max_value = int(np.max(matrix))  # Поиск максимального значения и переформатирование результата в строку
            max_value_index = np.where(matrix == max_value)
            temp2 = ' '.join(map(str, max_value_index))

            entry_matrix3_tab1.config(state="normal")
            entry_matrix3_tab1.delete(0, END)
            entry_matrix3_tab1.insert(END, f' Мин значение {min_value} - в позиции {temp}')
            entry_matrix3_tab1.config(state="readonly")

            entry_matrix4_tab1.config(state="normal")
            entry_matrix4_tab1.delete(0, END)
            entry_matrix4_tab1.insert(END, f' Мах значение {max_value} - в позиции {temp2}')
            entry_matrix4_tab1.config(state="readonly")

    def get_data_matrix_sum():
        try:
            if not matrix:   # Проверка на создание матрицы
                mb.showwarning(f"Предупреждение", 'Матрица не создана')
        except ValueError:
            total = int(np.sum(matrix))  # Запрос суммы элементов матрицы

            total_x = np.sum(matrix, axis=0)  # axis=0 - по столбцам
            total_column = [int((n / total) * 100) for n in total_x]  # расчет процентажа

            text_matrix2_tab1.config(state="normal")
            text_matrix2_tab1.delete('1.0', END)
            text_matrix2_tab1.insert(END, f'Общая сумма равна - {total}, '
                                          f'процентное соотношение сумм в столбцах {total_column}')
            text_matrix2_tab1.config(state="disabled")

    def get_data_for_multiplier_matrix():

        column = entry_matrix5_tab1.get()
        column, check_reserve = check_value(column, 'digit')

        if check_reserve is True:

            try:
                if not matrix:     # Проверка на создание матрицы
                    mb.showwarning(f"Предупреждение", 'Матрица не создана')
            except ValueError:
                row, col = matrix.shape
                matrix_vector = np.zeros(col, dtype=int)    # Создание нулевой матрицы для выбивания строки
                matrix_vector[column] = 1  # Присвоение значения 1 той строке которую надо выбить в матрице
                matrix_transpose = np.transpose(matrix)  # Транспонирование матрицы чтобы столбцы стали строками
                desired_column = np.dot(matrix_vector, matrix_transpose)  # умножение матриц и результат - вектор

                # генератор который создает матрицу согласно заданию (перемножая на нужный столбик) получ. список
                matrix_transpose = [[matrix[i][j] * desired_column[i] for i in range(0, row)] for j in range(0, row)]
                matrix_transpose = np.array(matrix_transpose)  # перегонка списка в массив

                desired_column = desired_column.reshape(row, 1)  # переформатирование массива в массив нужной формы

                text_matrix3_tab1.config(state="normal")
                text_matrix3_tab1.delete('1.0', END)
                text_matrix3_tab1.insert(END, f' Результатом умножения соответвующих элементов матрицы:'
                                              f'\n {matrix} \n'
                                              f' на столбец:\n {desired_column}\n является:\n {matrix_transpose}\n')
                text_matrix3_tab1.config(state="disabled")

    def get_data_for_sum_row_matrix():

        column = entry_matrix6_tab1.get()
        column, check_reserve = check_value(column, 'digit')

        if check_reserve is True:

            try:
                if not matrix:
                    mb.showwarning(f"Предупреждение", 'Матрица не создана')
            except ValueError:
                row, col = matrix.shape
                matrix_vector = np.zeros(col, dtype=int)   # Создание нулевой матрицы для выбивания строки
                matrix_vector[column] = 1   # Присвоение значения 1 той строке которую надо выбить в матрице
                desired_column = np.dot(matrix_vector, matrix)  # умножение матриц и результат - вектор

                # генератор который создает матрицу согласно заданию (перемножая на нужный столбик) получ. список
                matrix_transpose = [[matrix[i][j] + desired_column[j] for i in range(0, row)] for j in range(0, row)]
                matrix_transpose = np.array(matrix_transpose)   # перегонка списка в массив

                text_matrix4_tab1.config(state="normal")
                text_matrix4_tab1.delete('1.0', END)
                text_matrix4_tab1.insert(END, f' Результатом сложения соответвующих элементов матрицы:'
                                              f'\n {matrix} \n'
                                              f' с строкой:\n {desired_column}\n является:\n {matrix_transpose}\n')
                text_matrix4_tab1.config(state="disabled")

    def get_matrix_search():

        number = entry_matrix7_tab1.get()
        number, check_reserve = check_value(number, 'digit')  # вызов функции проверки значения

        text_matrix5_tab1.config(state="normal")
        text_matrix5_tab1.delete('1.0', END)
        text_matrix5_tab1.config(state="disabled")

        if check_reserve is True:

            try:
                if not matrix:  # проверка на создание матрицы
                    mb.showwarning(f"Предупреждение", 'Матрица не создана')
            except ValueError:
                number_index = np.where(matrix == number)  # поиск элемента в матрице, результат - хреновый кортеж

                if len(number_index) == 0:
                    mb.showwarning(f"Предупреждение", 'Совпадений не найдено!!')
                else:
                    text_matrix5_tab1.config(state="normal")
                    row, col = matrix.shape

                    n = np.array(sum(map(list, number_index), []))  # перегон результата поиска(кортежа) в массив

                    # перегон массива в список и разворот его на оборот (нужные элементы находятся от середины до конца
                    n = list(n)[::-1]
                    n = n[0:int((len(n) / 2))]   # отрезания первой половины списка (нужные нам значения

                    text_matrix5_tab1.insert(END, f' Искомый элемент находится в столбце(цах):\n')
                    for i in n:
                        matrix_vector = np.zeros(col, dtype=int)  # Создание нулевой матрицы для выбивания строки
                        matrix_vector[i] = 1   # Присвоение значения 1 той строке которую надо выбить в матрице
                        temp_matrix = np.transpose(matrix)  # Транспонируем матрицу
                        desired_column = np.dot(matrix_vector, temp_matrix)  # умножаем матрицу получаем вектор
                        desired_column = desired_column.reshape(col, 1)  # меняем форму вектора
                        text_matrix5_tab1.insert(END, f' {desired_column} \n')

                    text_matrix5_tab1.config(state="disabled")

    def get_diagonal():

        try:
            if not matrix:  # Проверка на наличии матрицы
                mb.showwarning(f"Предупреждение", 'Матрица не создана')
        except ValueError:
            my_sum = sum(np.diag(matrix))  # Считаем главную диагональ

            # Поворачиваем матрицу и считаем диагональ(которая будет побочной)
            my_prod = np.prod(np.diag(np.rot90(matrix)))
            entry_matrix8_tab1.config(state="normal")
            entry_matrix8_tab1.delete(0, END)
            entry_matrix8_tab1.insert(END, f' {my_sum}')
            entry_matrix8_tab1.config(state="readonly")

            entry_matrix9_tab1.config(state="normal")
            entry_matrix9_tab1.delete(0, END)
            entry_matrix9_tab1.insert(END, f' {my_prod}')
            entry_matrix9_tab1.config(state="readonly")

    def get_one_matrix():

        line = entry_matrix10_tab1.get()
        column = entry_matrix11_tab1.get()
        line, check_reserve = check_value(line, 'digit')  # Проверяем значения на цифры
        column, check_reserve2 = check_value(column, 'digit')

        if check_reserve is True and check_reserve2 is True:  # Проверяем соответствие размерности матрицы условиям
            if line > 5 or column > 5:
                mb.showwarning(f"Предупреждение", 'Русским по белому же написано максимальные размеры 5*5')
            elif line == 0 or column == 0:
                mb.showwarning(f"Предупреждение", 'Один из размеров матрицы не задан')
            else:
                global matrix_one
                matrix_one = np.random.randint(0, 2, (line, column))
                text_matrix6_tab2.config(state="normal")
                text_matrix6_tab2.delete('1.0', END)
                text_matrix6_tab2.insert(END, matrix_one)
                text_matrix6_tab2.config(state="disabled")

    def get_add_column():

        try:
            if not matrix_one:     # Проверка на наличии матрицы
                mb.showwarning(f"Предупреждение", 'Матрица не создана')
        except ValueError:
            row, col = matrix_one.shape
            temp_list = []

            matrix_vector = np.zeros(col, dtype=int)  # создаем нулевую матрицу

            # Прогоняем цикл в котором поочередно выбиваем каждую строку и считаем сумму. Если четная, то в новом
            # столбце будет 0, если нечетная, то 1

            for i in range(0, col):
                matrix_vector[i] = 1
                desired_column = np.dot(matrix_vector, matrix_one)
                total = np.sum(desired_column)  # сумма строки
                if total % 2 == 0:
                    temp_list.append(0)
                else:
                    temp_list.append(1)

            temp_list = np.array(temp_list)  # перегоняем список в массив
            arr_expanded = np.column_stack((matrix_one, temp_list))  # добавляем итоговый  столбец

            text_matrix7_tab2.config(state="normal")
            text_matrix7_tab2.delete('1.0', END)
            text_matrix7_tab2.insert(END, arr_expanded)
            text_matrix7_tab2.config(state="disabled")

    def get_exit_menu():

        lesson_6_main_menu.deiconify()
        lesson_6.withdraw()

    # endregion

    # region Рисование кнопок и подписей вкладки программы

    # Первая вкладка

    lab_matrix1_tab1 = Label(lesson_6, text='Всякое интересное с матрицами', font='Arial 14 bold', borderwidth=2,
                             relief="solid")
    lab_matrix1_tab1.place(x=10, y=20, width=940, height=25)

    lab_matrix2_tab1 = Label(lesson_6, text='Создание матрицы', font='Arial 12 bold')
    lab_matrix2_tab1.place(x=10, y=50, width=480, height=15)

    lab_matrix3_tab1 = Label(lesson_6, text='Введите размеры матрицы M*N (не более 5:5)', font='Arial 10',
                             borderwidth=2, relief="solid")
    lab_matrix3_tab1.place(x=10, y=90, width=480, height=30)

    lab_matrix4_tab1 = Label(lesson_6, text='M (строк)', font='Arial 9', borderwidth=2, relief="solid")
    lab_matrix4_tab1.place(x=10, y=130, width=230, height=30)

    lab_matrix5_tab1 = Label(lesson_6, text='N (столбцов)', font='Arial 9', borderwidth=2, relief="solid")
    lab_matrix5_tab1.place(x=260, y=130, width=230, height=30)

    entry_matrix1_tab1 = Entry(lesson_6, font='Arial 10 bold', width=15, borderwidth=2)
    entry_matrix1_tab1.place(x=10, y=170, width=230, height=30)

    entry_matrix2_tab1 = Entry(lesson_6, font='Arial 10 bold', width=15, borderwidth=2)
    entry_matrix2_tab1.place(x=260, y=170, width=230, height=30)

    button_matrix1_tab1 = Button(lesson_6, text='Создать матрицу', font='Arial 10 ', command=get_data_matrix,
                                 borderwidth=2)
    button_matrix1_tab1.place(x=10, y=205, width=480, height=30)

    text_matrix1_tab1 = Text(lesson_6, font='Arial 10', width=15, borderwidth=2, wrap="char", state="disabled")
    text_matrix1_tab1.place(x=10, y=240, width=480, height=100)

    lab_matrix6_tab1 = Label(tab1, text='Поиск минимального и максимального эл-т', font='Arial 12 bold')
    lab_matrix6_tab1.place(x=10, y=350, width=480, height=30)

    button_matrix2_tab1 = Button(tab1, text='Рассчитать', font='Arial 10 ', command=get_data_matrix_minmax,
                                 borderwidth=2)
    button_matrix2_tab1.place(x=10, y=385, width=480, height=30)

    lab_matrix7_tab1 = Label(tab1, text='Минимальный', font='Arial 9')
    lab_matrix7_tab1.place(x=10, y=420, width=480, height=30)

    entry_matrix3_tab1 = Entry(tab1, font='Arial 10 bold', width=15, borderwidth=2, state='readonly')
    entry_matrix3_tab1.place(x=10, y=455, width=480, height=30)

    lab_matrix8_tab1 = Label(tab1, text='Максимальный', font='Arial 9')
    lab_matrix8_tab1.place(x=10, y=490, width=480, height=30)

    entry_matrix4_tab1 = Entry(tab1, font='Arial 10 bold', width=15, borderwidth=2, state='readonly')
    entry_matrix4_tab1.place(x=10, y=525, width=480, height=30)

    lab_matrix8_tab1 = Label(tab1, text='Сумма элементов массива и % соотношение в сумме', font='Arial 12 bold')
    lab_matrix8_tab1.place(x=10, y=560, width=480, height=30)

    button_matrix3_tab1 = Button(tab1, text='Рассчитать', font='Arial 10 ', command=get_data_matrix_sum, borderwidth=2)
    button_matrix3_tab1.place(x=10, y=595, width=480, height=30)

    text_matrix2_tab1 = Text(tab1, font='Arial 10', width=15, borderwidth=2, wrap="char", state="disabled")
    text_matrix2_tab1.place(x=10, y=630, width=480, height=100)

    lab_matrix9_tab1 = Label(tab1, text='Умножение матрицы на элементы строки', font='Arial 12 bold')
    lab_matrix9_tab1.place(x=500, y=50, width=450, height=15)

    lab_matrix10_tab1 = Label(tab1, text='Выберите на какой столбец будем умножать', font='Arial 9', borderwidth=2,
                              relief="solid")
    lab_matrix10_tab1.place(x=500, y=70, width=450, height=30)

    entry_matrix5_tab1 = Entry(tab1, font='Arial 10 bold', width=15, borderwidth=2)
    entry_matrix5_tab1.place(x=500, y=110, width=210, height=30)

    button_matrix4_tab1 = Button(tab1, text='Рассчитать', font='Arial 10 ',
                                 command=get_data_for_multiplier_matrix, borderwidth=2)
    button_matrix4_tab1.place(x=740, y=110, width=210, height=30)

    text_matrix3_tab1 = Text(tab1, font='Arial 10', width=15, borderwidth=2, wrap="char", state="disabled")
    text_matrix3_tab1.place(x=500, y=150, width=450, height=280)

    lab_matrix11_tab1 = Label(tab1, text='Сложение матрицы с элементами строки', font='Arial 12 bold')
    lab_matrix11_tab1.place(x=500, y=440, width=450, height=30)

    lab_matrix12_tab1 = Label(tab1, text='Выберите с какой строкой будем складывать', font='Arial 9', borderwidth=2,
                              relief="solid")
    lab_matrix12_tab1.place(x=500, y=480, width=450, height=30)

    entry_matrix6_tab1 = Entry(tab1, font='Arial 10 bold', width=15, borderwidth=2)
    entry_matrix6_tab1.place(x=500, y=520, width=210, height=30)

    button_matrix5_tab1 = Button(tab1, text='Рассчитать', font='Arial 10 ',
                                 command=get_data_for_sum_row_matrix, borderwidth=2)
    button_matrix5_tab1.place(x=740, y=520, width=210, height=30)

    text_matrix4_tab1 = Text(tab1, font='Arial 10', width=15, borderwidth=2, wrap="char", state="disabled")
    text_matrix4_tab1.place(x=500, y=560, width=450, height=280)

    lab_matrix13_tab1 = Label(tab2, text='Поиск элемента в массиве и вывод результатов ', font='Arial 12 bold')
    lab_matrix13_tab1.place(x=10, y=350, width=480, height=30)

    lab_matrix14_tab1 = Label(tab2, text='Введите число для поиска', font='Arial 9')
    lab_matrix14_tab1.place(x=10, y=390, width=235, height=30)

    entry_matrix7_tab1 = Entry(tab2, font='Arial 10 bold', width=15, borderwidth=2)
    entry_matrix7_tab1.place(x=255, y=390, width=235, height=30)

    button_matrix6_tab1 = Button(tab2, text='Найти', font='Arial 10 ', command=get_matrix_search,
                                 borderwidth=2)
    button_matrix6_tab1.place(x=10, y=430, width=480, height=30)

    text_matrix5_tab1 = Text(tab2, font='Arial 10', width=15, borderwidth=2, wrap="char", state="disabled")
    text_matrix5_tab1.place(x=10, y=470, width=480, height=280)

    lab_matrix15_tab1 = Label(tab2, text='Поиск суммы главной и побочной диагонали', font='Arial 12 bold')
    lab_matrix15_tab1.place(x=500, y=50, width=450, height=15)

    button_matrix7_tab1 = Button(tab2, text='Расчитать', font='Arial 10 ', command=get_diagonal,
                                 borderwidth=2)
    button_matrix7_tab1.place(x=500, y=70, width=450, height=30)

    lab_matrix16_tab1 = Label(tab2, text='Главная диагональ', font='Arial 9 bold')
    lab_matrix16_tab1.place(x=500, y=110, width=220, height=15)

    lab_matrix17_tab1 = Label(tab2, text='Побочная диагональ', font='Arial 9 bold')
    lab_matrix17_tab1.place(x=730, y=110, width=220, height=15)

    entry_matrix8_tab1 = Entry(tab2, font='Arial 10 bold', width=15, borderwidth=2, state='readonly')
    entry_matrix8_tab1.place(x=500, y=130, width=220, height=30)

    entry_matrix9_tab1 = Entry(tab2, font='Arial 10 bold', width=15, borderwidth=2, state='readonly')
    entry_matrix9_tab1.place(x=730, y=130, width=220, height=30)

    lab_matrix18_tab1 = Label(tab2, text='Создание матрицы из 0 и 1 и добавление столбца', font='Arial 12')
    lab_matrix18_tab1.place(x=500, y=170, width=450, height=15)

    lab_matrix19_tab1 = Label(tab2, text='при добавление столбца сумма 1 в строке будет четной', font='Arial 9')
    lab_matrix19_tab1.place(x=500, y=190, width=450, height=15)

    lab_matrix20_tab1 = Label(tab2, text='Введите размеры матрицы M*N (не более 5:5)', font='Arial 10',
                              borderwidth=2, relief="solid")
    lab_matrix20_tab1.place(x=500, y=210, width=450, height=30)

    lab_matrix21_tab1 = Label(tab2, text='M (строк)', font='Arial 9', borderwidth=2, relief="solid")
    lab_matrix21_tab1.place(x=500, y=245, width=220, height=30)

    lab_matrix22_tab1 = Label(tab2, text='N (столбцов)', font='Arial 9', borderwidth=2, relief="solid")
    lab_matrix22_tab1.place(x=730, y=245, width=220, height=30)

    entry_matrix10_tab1 = Entry(tab2, font='Arial 10 bold', width=15, borderwidth=2)
    entry_matrix10_tab1.place(x=500, y=285, width=220, height=30)

    entry_matrix11_tab1 = Entry(tab2, font='Arial 10 bold', width=15, borderwidth=2)
    entry_matrix11_tab1.place(x=730, y=285, width=220, height=30)

    button_matrix8_tab1 = Button(tab2, text='Создать матрицу', font='Arial 10 ', command=get_one_matrix,
                                 borderwidth=2)
    button_matrix8_tab1.place(x=500, y=325, width=450, height=30)

    text_matrix6_tab2 = Text(tab2, font='Arial 10', width=15, borderwidth=2, wrap="char", state="disabled")
    text_matrix6_tab2.place(x=500, y=360, width=450, height=100)

    button_matrix9_tab1 = Button(tab2, text='Добавить', font='Arial 10 ', command=get_add_column,
                                 borderwidth=2)
    button_matrix9_tab1.place(x=500, y=470, width=450, height=30)

    text_matrix7_tab2 = Text(tab2, font='Arial 10', width=15, borderwidth=2, wrap="char", state="disabled")
    text_matrix7_tab2.place(x=500, y=510, width=450, height=100)

    button_exit = Button(tab2, text='Выход', font='Arial 12 ', command=get_exit_menu, borderwidth=2)
    button_exit.place(x=150, y=750, width=210, height=30)

    # endregion


# region Функции вкладки меню


def get_exit():
    lesson_6_main_menu.destroy()


# endregion

# region Рисование кнопок и подписей вкладки меню


lab_menu = Label(lesson_6_main_menu, text='Расчеты по теме 6. Матрицы', font='Arial 20 bold')
lab_menu.place(x=10, y=450, width=960, height=30)

button_main_menu = Button(lesson_6_main_menu, text='Войти в программу', font='Arial 12 ', command=get_enter,
                          borderwidth=2)
button_main_menu.place(x=10, y=490, width=960, height=30)
button_main_menu2 = Button(lesson_6_main_menu, text='Выход', font='Arial 12 ', command=get_exit, borderwidth=2)
button_main_menu2.place(x=10, y=530, width=960, height=30)

lesson_6_main_menu.protocol('WM_DELETE_WINDOW', get_exit)

lesson_6_main_menu.mainloop()

# endregion
