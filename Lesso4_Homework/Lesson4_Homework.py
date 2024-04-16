from math import *  # Добавляем библиотеку math
from tkinter import *  # Добавляем библиотеку Ткинтер
from tkinter import ttk
from tkinter import messagebox as mb  # Добавляем метод библиотеки на всплывающие сообщения

lesson_4 = Tk()  # Объявляем класс

lesson_4.title("Расчеты по теме 4")


def data_check(a, b, c, check_tab):              # Функция проверки для первых 2 заданий(там по 3 переменных)
    if b == '0':  # Проверка на 0

        # Проверяем нет ли нуля в делителе
        mb.showwarning("Предупреждение", "На 0 делить нельзя")
        entry_task2_tab1.delete(0, END)
        check = False

        # Проверка на то что введенные данные - целое число
    elif a.isdigit() is True and b.isdigit() is True and c.isdigit() is True:

        a = int(a)  # Перевод строки в число
        b = int(b)
        c = int(c)
        check = True
    else:
        try:  # Проверка на то что введенные данные число в пл. точкой
            a = float(a)
            b = float(b)
            c = float(c)
            check = True

        except ValueError:  # Перехват ошибки (если данные не числовые)
            mb.showwarning("Предупреждение", "Один из параметров не цифра")
            check = False
            if check_tab == 'tab1':  # Проверка с какой закладки был заход
                entry_task1_tab1.delete(0, END)
                entry_task2_tab1.delete(0, END)
                entry_task3_tab1.delete(0, END)
            else:
                entry_task1_tab2.delete(0, END)
                entry_task2_tab2.delete(0, END)
                entry_task3_tab2.delete(0, END)

    return a, b, c, check  # Возврат оцифрованного значения(целое или плавающее)


def data_check_tab3(r1, v1, r2, v2):  # Функция проверки для 3 задания (там 4 переменных)
    if v1 == '0' or v2 == '0':  # Проверка на 0

        mb.showwarning("Предупреждение", "На 0 делить нельзя")
        entry_task2_tab3.delete(0, END)
        entry_task4_tab3.delete(0, END)
        check = False

        # Проверка на то что введенные данные - целое число
    elif r1.isdigit() is True and v1.isdigit() is True and r2.isdigit() is True and v2.isdigit() is True:

        r1 = int(r1)  # Перевод строки в число
        v1 = int(v1)
        r2 = int(r2)
        v2 = int(v2)
        check = True
    else:
        try:  # Проверка на то что введенные данные число в пл. точкой
            r1 = float(r1)
            v1 = float(v1)
            r2 = float(r2)
            v2 = float(v2)
            check = True

        except ValueError:  # Перехват ошибки (если данные не числовые)
            mb.showwarning("Предупреждение", "Один из параметров не цифра")
            check = False
            entry_task1_tab3.delete(0, END)
            entry_task2_tab3.delete(0, END)
            entry_task3_tab3.delete(0, END)

    return r1, v1, r2, v2, check  # Возврат оцифрованного значения(целое или плавающее)


def get_result_tab1():            # Функция сбора и расчета данных по первому заданию
    a = entry_task1_tab1.get()
    b = entry_task2_tab1.get()
    c = entry_task3_tab1.get()
    a, b, c, check = data_check(a, b, c, 'tab1')

    if check is True:
        result1 = str(((pow(a, 2)) / 3) + ((pow(a, 2) + 4) / b) + (sqrt((pow(a, 2) + 4)) / 4) + (
            sqrt(pow((pow(a, 2) + 4), 3))) / 4)
        result2 = str((pow(cos(pow(c, 2)), 2) + pow(sin(2 * c - 1), 2)) ** (1. / 3))
        result3 = str(cos(c) + sin(c))
        result4 = str((5 * c) + 3 * pow(c, 2) * (sqrt(pow(sin(c), 2))))

        entry_result1_tab1.config(state="normal")   # Смена статуса текстового поля для внесения изменений
        entry_result2_tab1.config(state="normal")
        entry_result3_tab1.config(state="normal")
        entry_result4_tab1.config(state="normal")

        entry_result1_tab1.delete(0, END)
        entry_result2_tab1.delete(0, END)
        entry_result3_tab1.delete(0, END)
        entry_result4_tab1.delete(0, END)

        entry_result1_tab1.insert(END, result1)
        entry_result2_tab1.insert(END, result2)
        entry_result3_tab1.insert(END, result3)
        entry_result4_tab1.insert(END, result4)

        entry_result1_tab1.config(state="readonly")   # Возврат блокировки
        entry_result2_tab1.config(state="readonly")
        entry_result3_tab1.config(state="readonly")
        entry_result4_tab1.config(state="readonly")
    else:
        entry_result1_tab1.delete(0, END)
        entry_result2_tab1.delete(0, END)
        entry_result3_tab1.delete(0, END)
        entry_result4_tab1.delete(0, END)

    return


def get_result_tab2():     # Функция сбора и расчета данных по второму заданию
    i = entry_task1_tab2.get()
    s = entry_task2_tab2.get()
    n = entry_task3_tab2.get()
    i, s, n, check = data_check(i, s, n, 'tab2')

    if check is True:
        p = (i / 100) / 12
        monthly_payment = s * (p + (p / (pow((1 + p), n) - 1)))

        total_amount = monthly_payment * n
        overpayment = total_amount - s

        entry_result1_tab2.config(state="normal")   # Смена статуса текстового поля для внесения изменений
        entry_result1_tab2.delete(0, END)
        entry_result1_tab2.insert(END, str(monthly_payment))
        entry_result1_tab2.config(state="readonly")   # Возврат блокировки

        entry_result2_tab2.config(state="normal")
        entry_result2_tab2.delete(0, END)
        entry_result2_tab2.insert(END, str(total_amount))
        entry_result2_tab2.config(state="readonly")

        entry_result3_tab2.config(state="normal")
        entry_result3_tab2.delete(0, END)
        entry_result3_tab2.insert(END, str(overpayment))
        entry_result3_tab2.config(state="readonly")


def get_result_tab3():    # Функция сбора и расчета данных по третьему заданию

    r1 = entry_task1_tab3.get()
    v1 = entry_task2_tab3.get()
    r2 = entry_task3_tab3.get()
    v2 = entry_task4_tab3.get()
    r1, v1, r2, v2, check = data_check_tab3(r1, v1, r2, v2)

    if check is True:

        length_year_first_planet = (2 * r1 * pi)/v1
        length_year_second_planet = (2 * r2 * pi) / v2

        if length_year_first_planet > length_year_second_planet:

            entry_result3_tab3.config(state="normal")
            entry_result3_tab3.delete(0, END)
            entry_result3_tab3.insert(END, 'Верно! Длинна года на первой планете больше, чем на второй!')
            entry_result3_tab3.config(state="readonly")

        elif length_year_first_planet == length_year_second_planet:

            entry_result3_tab3.config(state="normal")
            entry_result3_tab3.delete(0, END)
            entry_result3_tab3.insert(END, 'Неверно! Длины года одинаковые на обеих планетах!')
            entry_result3_tab3.config(state="readonly")

        elif length_year_first_planet < length_year_second_planet:

            entry_result3_tab3.config(state="normal")
            entry_result3_tab3.delete(0, END)
            entry_result3_tab3.insert(END, 'Неверно! Длинна года на второй  планете больше, чем на первой!')
            entry_result3_tab3.config(state="readonly")

        entry_result1_tab3.config(state="normal")
        entry_result1_tab3.delete(0, END)
        entry_result1_tab3.insert(END, str(length_year_first_planet))
        entry_result1_tab3.config(state="readonly")

        entry_result2_tab3.config(state="normal")
        entry_result2_tab3.delete(0, END)
        entry_result2_tab3.insert(END, str(length_year_second_planet))
        entry_result2_tab3.config(state="readonly")


# Получаем ширину и высоту экрана
screen_width = lesson_4.winfo_screenwidth()
screen_height = lesson_4.winfo_screenheight()

# Вычисляем координаты окна приложения
window_width = 400
window_height = 860
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
lesson_4.geometry(f"{window_width}x{window_height}+{x}+{y}")

lesson_4.resizable(None, None)  # Запрещаем изменять размер окна
lesson_4["bg"] = "gray22"  # gray gray0-99   # Устанавливаем цвет фона

tab_control = ttk.Notebook(lesson_4)   # Создаем элемент класса - закладки

tab1 = ttk.Frame(tab_control)  # Создаем три закладки
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Задание 1')  # Даем название, размещаем, вставляем поясняющий текст
lab_task1_tab1 = Label(tab1, text='Введите значение переменных для получения результата')
lab_task1_tab1.place(x=30, y=2)

tab_control.add(tab2, text='Задание 2')
lab_task2_tab1 = Label(tab2, text='Введите данные по кредиту для расчета ежемесячных выплат')
lab_task2_tab1.place(x=30, y=2)

tab_control.add(tab3, text='Задание 3')
lab_task3_tab1 = Label(tab3, text='Введите данные двух планет, для расчета и сравнения длинны года')
lab_task3_tab1.place(x=10, y=2)

tab_control.pack(expand=1, fill='both')  # Включаем/размещаем закладки

# Рисуем кнопки и надписи для задания 1

entry_task1_tab1 = Entry(tab1, font='Arial 12 bold', width=15, borderwidth=2)
entry_task1_tab1.place(x=10, y=20, width=110, height=30)

entry_task2_tab1 = Entry(tab1, font='Arial 12 bold', width=15, borderwidth=2)
entry_task2_tab1.place(x=140, y=20, width=110, height=30)

entry_task3_tab1 = Entry(tab1, font='Arial 12 bold', width=15, borderwidth=2)
entry_task3_tab1.place(x=270, y=20, width=110, height=30)

lab_entry1_tab1 = Label(tab1, text='а', font='Arial 12 bold')
lab_entry1_tab1.place(x=10, y=45, width=110, height=25)
lab_entry2_tab1 = Label(tab1, text='b', font='Arial 12 bold')
lab_entry2_tab1.place(x=140, y=45, width=110, height=25)
lab_entry3_tab1 = Label(tab1, text='x', font='Arial 12 bold')
lab_entry3_tab1.place(x=270, y=45, width=110, height=25)

button_result_tab1 = Button(tab1, text='Рассчитать', font='Arial 15 bold', width=25, command=get_result_tab1)
button_result_tab1.place(x=10, y=64, width=365, height=30)

# Добавим изображение
lab_photo1_tab1 = Label(tab1, text='Формула №1')
lab_photo1_tab1.place(x=10, y=100, width=365, height=30)

canvas = Canvas(tab1, height=400, width=700)
img1 = PhotoImage(file="1.png")
image1 = canvas.create_image(0, 0, anchor='nw', image=img1)
canvas.place(x=10, y=135, width=365, height=80)

lab_result1_tab1 = Label(tab1, text='Результат расчета первой формулы')
lab_result1_tab1.place(x=10, y=215, width=365, height=30)

entry_result1_tab1 = Entry(tab1, font='Arial 15 bold', width=15, borderwidth=2, state="readonly")
entry_result1_tab1.place(x=10, y=240, width=365, height=30)

lab_photo2_tab1 = Label(tab1, text='Формула №2')
lab_photo2_tab1.place(x=10, y=275, width=365, height=30)

canvas = Canvas(tab1, height=400, width=700)
img2 = PhotoImage(file="2.png")
image2 = canvas.create_image(0, 0, anchor='nw', image=img2)
canvas.place(x=10, y=310, width=365, height=80)

lab_result2_tab1 = Label(tab1, text='Результат расчета второй формулы')
lab_result2_tab1.place(x=10, y=395, width=365, height=30)

entry_result2_tab1 = Entry(tab1, font='Arial 15 bold', width=15, borderwidth=2, state="readonly")
entry_result2_tab1.place(x=10, y=430, width=365, height=30)

lab_photo3_tab1 = Label(tab1, text='Формула №3')
lab_photo3_tab1.place(x=10, y=465, width=365, height=30)

canvas = Canvas(tab1, height=400, width=700)
img3 = PhotoImage(file="2.png")
image3 = canvas.create_image(0, 0, anchor='nw', image=img3)
canvas.place(x=10, y=500, width=365, height=80)

lab_result3_tab1 = Label(tab1, text='Результат расчета третьей формулы')
lab_result3_tab1.place(x=10, y=580, width=365, height=30)

entry_result3_tab1 = Entry(tab1, font='Arial 15 bold', width=15, borderwidth=2, state="readonly")
entry_result3_tab1.place(x=10, y=620, width=365, height=30)

lab_photo4_tab1 = Label(tab1, text='Формула №4')
lab_photo4_tab1.place(x=10, y=650, width=365, height=30)

canvas = Canvas(tab1, height=400, width=700)
img4 = PhotoImage(file="2.png")
image4 = canvas.create_image(0, 0, anchor='nw', image=img3)
canvas.place(x=10, y=685, width=365, height=80)

lab_result4_tab1 = Label(tab1, text='Результат расчета четвертой формулы')
lab_result4_tab1.place(x=10, y=765, width=365, height=30)

entry_result4_tab1 = Entry(tab1, font='Arial 15 bold', width=15, borderwidth=2, state="readonly")
entry_result4_tab1.place(x=10, y=800, width=365, height=30)

entry_task1_tab1 = Entry(tab1, font='Arial 12 bold', width=15, borderwidth=2)
entry_task1_tab1.place(x=10, y=20, width=110, height=30)

entry_task2_tab1 = Entry(tab1, font='Arial 12 bold', width=15, borderwidth=2)
entry_task2_tab1.place(x=140, y=20, width=110, height=30)

entry_task3_tab1 = Entry(tab1, font='Arial 12 bold', width=15, borderwidth=2)
entry_task3_tab1.place(x=270, y=20, width=110, height=30)

# Рисуем кнопки и надписи для задания 2

entry_task1_tab2 = Entry(tab2, font='Arial 12 bold', width=15, borderwidth=2)
entry_task1_tab2.place(x=10, y=20, width=110, height=30)

entry_task2_tab2 = Entry(tab2, font='Arial 12 bold', width=15, borderwidth=2)
entry_task2_tab2.place(x=140, y=20, width=110, height=30)

entry_task3_tab2 = Entry(tab2, font='Arial 12 bold', width=15, borderwidth=2)
entry_task3_tab2.place(x=270, y=20, width=110, height=30)

lab_entry1_tab2 = Label(tab2, text='i', font='Arial 12 bold')
lab_entry1_tab2.place(x=10, y=45, width=110, height=25)
lab_entry2_tab2 = Label(tab2, text='s', font='Arial 12 bold')
lab_entry2_tab2.place(x=140, y=45, width=110, height=25)
lab_entry3_tab2 = Label(tab2, text='n', font='Arial 12 bold')
lab_entry3_tab2.place(x=270, y=45, width=110, height=25)

lab_entry4_tab2 = Label(tab2, text='i - годовая процентная ставка', font='Arial 12')
lab_entry4_tab2.place(x=10, y=75, width=380, height=25)
lab_entry5_tab2 = Label(tab2, text='s - сумма займа', font='Arial 12')
lab_entry5_tab2.place(x=10, y=105, width=380, height=25)
lab_entry6_tab2 = Label(tab2, text='n - количество месяцев на которые взят кредит', font='Arial 12')
lab_entry6_tab2.place(x=10, y=135, width=380, height=25)

button_result_tab2 = Button(tab2, text='Рассчитать', font='Arial 12', width=25, command=get_result_tab2)
button_result_tab2.place(x=10, y=175, width=365, height=30)

lab_result2_tab2 = Label(tab2, text='Итоговая сумма составляет:', font='Arial 12')
lab_result2_tab2.place(x=10, y=210, width=380, height=25)

entry_result2_tab2 = Entry(tab2, font='Arial 12 bold', width=15, borderwidth=2, state="readonly")
entry_result2_tab2.place(x=10, y=240, width=380, height=25)

lab_result3_tab2 = Label(tab2, text='Переплата составит:', font='Arial 12')
lab_result3_tab2.place(x=10, y=270, width=380, height=25)

entry_result3_tab2 = Entry(tab2, font='Arial 12 bold', width=15, borderwidth=2, state="readonly")
entry_result3_tab2.place(x=10, y=300, width=380, height=25)

lab_result1_tab2 = Label(tab2, text='Ежемесячный платеж по кредиту составляет:', font='Arial 12')
lab_result1_tab2.place(x=10, y=330, width=380, height=25)

entry_result1_tab2 = Entry(tab2, font='Arial 12 bold', width=15, borderwidth=2, state="readonly")
entry_result1_tab2.place(x=10, y=360, width=380, height=50)

# Рисуем кнопки и надписи для задания 3

entry_task1_tab3 = Entry(tab3, font='Arial 12 bold', width=15, borderwidth=2)
entry_task1_tab3.place(x=10, y=20, width=80, height=30)

entry_task2_tab3 = Entry(tab3, font='Arial 12 bold', width=15, borderwidth=2)
entry_task2_tab3.place(x=100, y=20, width=80, height=30)

entry_task3_tab3 = Entry(tab3, font='Arial 12 bold', width=15, borderwidth=2)
entry_task3_tab3.place(x=190, y=20, width=80, height=30)

entry_task4_tab3 = Entry(tab3, font='Arial 12 bold', width=15, borderwidth=2)
entry_task4_tab3.place(x=280, y=20, width=80, height=30)

lab_entry1_tab3 = Label(tab3, text='R (млн.км)', font='Arial 12')
lab_entry1_tab3.place(x=10, y=55, width=80, height=30)
lab_entry2_tab3 = Label(tab3, text='V (км/ч)', font='Arial 12')
lab_entry2_tab3.place(x=100, y=55, width=80, height=30)
lab_entry3_tab3 = Label(tab3, text='R (млн.км)', font='Arial 12')
lab_entry3_tab3.place(x=190, y=55, width=80, height=30)
lab_entry4_tab3 = Label(tab3, text='V (км/ч)', font='Arial 12')
lab_entry4_tab3.place(x=280, y=55, width=80, height=30)
lab_entry5_tab3 = Label(tab3, text='Первая планета', font='Arial 12')
lab_entry5_tab3.place(x=10, y=90, width=180, height=30)
lab_entry6_tab3 = Label(tab3, text='Вторая планета', font='Arial 12')
lab_entry6_tab3.place(x=190, y=90, width=180, height=30)


button_result_tab3 = Button(tab3, text='Рассчитать', font='Arial 15', width=25, command=get_result_tab3)
button_result_tab3.place(x=10, y=125, width=365, height=30)

lab_entry7_tab3 = Label(tab3, text='Длинна года на первой планете', font='Arial 12')
lab_entry7_tab3.place(x=10, y=160, width=365, height=30)

entry_result1_tab3 = Entry(tab3, font='Arial 12', width=15, borderwidth=2, state="readonly")
entry_result1_tab3.place(x=10, y=200, width=365, height=30)

lab_entry8_tab3 = Label(tab3, text='Длинна года на второй планете', font='Arial 12')
lab_entry8_tab3.place(x=10, y=240, width=365, height=30)

entry_result2_tab3 = Entry(tab3, font='Arial 12', width=15, borderwidth=2, state="readonly")
entry_result2_tab3.place(x=10, y=290, width=365, height=30)

lab_entry9_tab3 = Label(tab3, text='Верно ли, что длинна года на первой планете больше?', font='Arial 10')
lab_entry9_tab3.place(x=10, y=330, width=365, height=30)

entry_result3_tab3 = Entry(tab3, font='Arial 11', width=15, borderwidth=2, state="readonly")
entry_result3_tab3.place(x=10, y=370, width=365, height=30)

lesson_4.mainloop()
