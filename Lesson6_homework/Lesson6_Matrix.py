from tkinter import *  # Добавляем библиотеку Ткинтер
from tkinter import ttk  # Добавляем модуль Ткинтера

from typing import List

from My_Function import *  # Добавляем библиотеку Function
from tkinter import messagebox as mb
import random  # Добавляем библиотеку рандома
import numpy as np

lesson_6 = Tk()  # Объявляем класс

lesson_6.title("Расчеты по теме 6. Матрицы")

# Получаем ширину и высоту экрана
screen_width = lesson_6.winfo_screenwidth()
screen_height = lesson_6.winfo_screenheight()

# Вычисляем координаты окна приложения
window_width = 960
window_height = 860
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
lesson_6.geometry(f"{window_width}x{window_height}+{x}+{y}")

lesson_6.resizable(None, None)  # Запрещаем изменять размер окна
lesson_6["bg"] = "gray22"  # gray gray0-99   # Устанавливаем цвет фона

tab_control = ttk.Notebook(lesson_6)  # создаем подкласс для закладок

tab1 = ttk.Frame(tab_control)  # создаем закладки

tab_control.add(tab1, text='Матрицы')
tab_control.pack(expand=1, fill='both')

matrix = []  # Глобальная переменная для хранения матрицы(чтобы не гонять ее по функциям)


def get_data_matrix():
    line = entry_matrix1_tab1.get()
    column = entry_matrix2_tab1.get()
    line, check_reserve = check_value(line, 'digit')
    column, check_reserve2 = check_value(column, 'digit')

    if check_reserve is True and check_reserve2 is True:
        if line > 6 or column > 6:
            mb.showwarning(f"Предупреждение", 'Русским по белому же написано максимальные размеры 6*6')
        elif line == 0 or column == 0:
            mb.showwarning(f"Предупреждение", 'Один из размеров матрицы не задан')
        else:
            global matrix
            matrix = np.random.randint(0, 99, (line, column))
            text_matrix1_tab1.config(state="normal")
            text_matrix1_tab1.delete('1.0', END)
            text_matrix1_tab1.insert(END, matrix)
            text_matrix1_tab1.config(state="disabled")


def get_data_matrix_minmax():


    min_value = int(np.min(matrix))
    min_value_index = np.where(matrix == min_value)
    temp = ' '.join(map(str, min_value_index))

    max_value = int(np.max(matrix))
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

    total = int(np.sum(matrix))

    total_x = np.sum(matrix, axis=0)  # axis=0 - по столбцам
    total_column = [int((n / total) * 100) for n in total_x]

    text_matrix2_tab1.config(state="normal")
    text_matrix2_tab1.delete('1.0', END)
    text_matrix2_tab1.insert(END, f'Общая сумма равна - {total}, '
                                  f'процентное соотношение сумм в столбцах {total_column}')
    text_matrix2_tab1.config(state="disabled")

# Рисование кнопок и подписей
# Первая вкладка


lab_matrix1_tab1 = Label(tab1, text='Всякое интересное с матрицами', font='Arial 14 bold', borderwidth=2,
                         relief="solid")
lab_matrix1_tab1.place(x=10, y=10, width=940, height=30)

lab_matrix2_tab1 = Label(tab1, text='Создание матрицы', font='Arial 12 bold')
lab_matrix2_tab1.place(x=10, y=50, width=480, height=30)

lab_matrix3_tab1 = Label(tab1, text='Введите размеры матрицы M*N (не более 6:6)', font='Arial 10', borderwidth=2,
                         relief="solid")
lab_matrix3_tab1.place(x=10, y=90, width=480, height=30)

lab_matrix4_tab1 = Label(tab1, text='M (строк)', font='Arial 9', borderwidth=2, relief="solid")
lab_matrix4_tab1.place(x=10, y=130, width=230, height=30)

lab_matrix5_tab1 = Label(tab1, text='N (столбцов)', font='Arial 9', borderwidth=2, relief="solid")
lab_matrix5_tab1.place(x=260, y=130, width=230, height=30)

entry_matrix1_tab1 = Entry(tab1, font='Arial 10 bold', width=15, borderwidth=2)
entry_matrix1_tab1.place(x=10, y=170, width=230, height=30)

entry_matrix2_tab1 = Entry(tab1, font='Arial 10 bold', width=15, borderwidth=2)
entry_matrix2_tab1.place(x=260, y=170, width=230, height=30)

button_matrix1_tab1 = Button(tab1, text='Создать матрицу', font='Arial 10 ', command=get_data_matrix, borderwidth=2)
button_matrix1_tab1.place(x=10, y=205, width=480, height=30)

text_matrix1_tab1 = Text(tab1, font='Arial 10', width=15, borderwidth=2, wrap="char", state="disabled")
text_matrix1_tab1.place(x=10, y=240, width=480, height=100)

lab_matrix6_tab1 = Label(tab1, text='Поиск минимального и максимального эл-т', font='Arial 12 bold')
lab_matrix6_tab1.place(x=10, y=350, width=480, height=30)

button_matrix2_tab1 = Button(tab1, text='Рассчитать', font='Arial 10 ', command=get_data_matrix_minmax, borderwidth=2)
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

# lab_matrix9_tab1 = Label(tab1, text='Умножение матрицы на элементы строки', font='Arial 12 bold')
# lab_matrix9_tab1.place(x=10, y=560, width=480, height=30)
#
# button_matrix4_tab1 = Button(tab1, text='Рассчитать', font='Arial 10 ', command=get_data_matrix_sum, borderwidth=2)
# button_matrix4_tab1.place(x=10, y=595, width=480, height=30)
#
# text_matrix3_tab1 = Text(tab1, font='Arial 10', width=15, borderwidth=2, wrap="char", state="disabled")
# text_matrix3_tab1.place(x=10, y=630, width=480, height=100)

lesson_6.mainloop()
