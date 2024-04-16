from tkinter import *  # Добавляем библиотеку Ткинтер
from tkinter import ttk    # Добавляем модуль Ткинтера
from My_Function import *           # Добавляем библиотеку Function
from collections import Counter  # Добавляем библиотеку collections и метод Counter


lesson_6 = Tk()  # Объявляем класс

lesson_6.title("Расчеты по теме 5")

# Получаем ширину и высоту экрана
screen_width = lesson_6.winfo_screenwidth()
screen_height = lesson_6.winfo_screenheight()

# Вычисляем координаты окна приложения
window_width = 400
window_height = 860
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
lesson_6.geometry(f"{window_width}x{window_height}+{x}+{y}")

lesson_6.resizable(None, None)  # Запрещаем изменять размер окна
lesson_6["bg"] = "gray22"  # gray gray0-99   # Устанавливаем цвет фона

tab_control = ttk.Notebook(lesson_6)   # создаем клас для закладок

tab1 = ttk.Frame(tab_control)   # создаем закладки
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Рекурсия и перевод')
tab_control.add(tab2, text='Простое число и НОД')
tab_control.add(tab3, text='Шифрование')
tab_control.add(tab4, text='Матрицы')
tab_control.pack(expand=1, fill='both')


def get_data_list_numbers():     # Функция получения данных списка чисел

    n = entry_sort_numbers_tab1.get()
    n, check_reserve = check_value(n, 'float')

    if check_reserve is True:
        list_numbers = entry_sort_numbers2_tab1.get()
        list_numbers = list_numbers.split()
        list_numbers = [int(n) for n in list_numbers]

        list_numbers.append(n)

        entry_sort_numbers2_tab1.config(state="normal")
        entry_sort_numbers_tab1.delete(0, END)
        entry_sort_numbers2_tab1.delete(0, END)
        entry_sort_numbers2_tab1.insert(END, list_numbers)
        entry_sort_numbers2_tab1.config(state="readonly")


def get_result_sort_numbers():   # Функция для поиска индекса элемента в сортированном рекурсивным методом

    list_sort_numbers = entry_sort_numbers2_tab1.get()
    list_sort_numbers = list_sort_numbers.split()
    list_sort_numbers = [int(n) for n in list_sort_numbers]

    count_frequency = Counter(list_sort_numbers)
    sort_numbers = list(count_frequency.keys())
    sort_numbers = sorted(sort_numbers)

    entry_sort_numbers3_tab1.config(state="normal")
    entry_sort_numbers3_tab1.delete(0, END)
    entry_sort_numbers3_tab1.insert(END, sort_numbers)
    entry_sort_numbers3_tab1.config(state="readonly")


def sorting_rec_find():  # Функция для бинарного поиска в сортир. списке

    simbol_find = entry_sort_numbers5_tab1.get()

    list_sort = entry_sort_numbers3_tab1.get()
    list_sort = list_sort.split()
    list_sort = [int(n) for n in list_sort]

    low_rec = 0
    high_rec = int(len(list_sort) - 1)
    mid_rec = (low_rec + high_rec) // 2

    index_find, check_list = bin_rec_find(simbol_find, low_rec, high_rec, mid_rec, list_sort, 0)

    entry_sort_numbers6_tab1.config(state="normal")
    entry_sort_numbers6_tab1.delete(0, END)
    entry_sort_numbers6_tab1.insert(END, f' Позиция {simbol_find} - {index_find}')
    entry_sort_numbers6_tab1.config(state="readonly")


def converting_numbers():  # Функция запроса данных для конвертации десятичного числа в двоичное

    n = entry_sort_numbers7_tab1.get()
    n, check_reserve = check_value(n, 'digit')

    if check_reserve is True:

        convert_str: str = ''
        convert_str = func_convert_dec_in_bin(n, convert_str)

        text_rec_tab1.config(state="normal")
        text_rec_tab1.delete('1.0', END)
        text_rec_tab1.insert(END, f' Число {n} -  в двоичной системе счисления - {convert_str}')
        text_rec_tab1.config(state="disabled")


def get_test_prime_number():  # Функция запроса числа на проверку

    n = entry_prime_number2_tab2.get()
    n, check_reserve = check_value(n, 'digit')

    result = func_prime_number(n)

    if result is True:
        entry_prime_number3_tab2.config(state="normal")
        entry_prime_number3_tab2.delete(0, END)
        entry_prime_number3_tab2.insert(END, f' Число {n} - не простое!')
        entry_prime_number3_tab2.config(state="readonly")
    else:
        entry_prime_number3_tab2.config(state="normal")
        entry_prime_number3_tab2.delete(0, END)
        entry_prime_number3_tab2.insert(END, f' Число {n} - простое! ')
        entry_prime_number3_tab2.config(state="readonly")


def get_nod():  # Функция запроса числа на проверку

    first_num = entry_prime_number4_tab2.get()
    first_num, check_reserve = check_value(first_num, 'digit')

    second_num = entry_prime_number5_tab2.get()
    second_num, check_reserve = check_value(second_num, 'digit')

    result = func_nod(first_num, second_num)

    if result == 0:
        entry_prime_number6_tab2.config(state="normal")
        entry_prime_number6_tab2.delete(0, END)
        entry_prime_number6_tab2.insert(END, f' Общих делителей -нет')
        entry_prime_number6_tab2.config(state="readonly")
    else:
        entry_prime_number6_tab2.config(state="normal")
        entry_prime_number6_tab2.delete(0, END)
        entry_prime_number6_tab2.insert(END, f' НОД для {first_num} и {second_num} - {result} ')
        entry_prime_number6_tab2.config(state="readonly")


def clear_data():  # Кнопка очищения полей для списка чисел

    entry_sort_numbers2_tab1.config(state="normal")
    entry_sort_numbers2_tab1.delete(0, END)
    entry_sort_numbers2_tab1.config(state="readonly")


# Рисование кнопок и подписей


lab_sort_numbers1_tab1 = Label(tab1, text='Бинарный рекурсивный поиск по сортированному списку', font='Arial 10 bold')
lab_sort_numbers1_tab1.place(x=10, y=10, width=380, height=15)

lab_sort_numbers2_tab1 = Label(tab1, text='Вывод данных по списку чисел', font='Arial 10')
lab_sort_numbers2_tab1.place(x=10, y=30, width=380, height=30)
lab_sort_numbers3_tab1 = Label(tab1, text='Чтобы добавить число в список введите его в поле', font='Arial 9')
lab_sort_numbers3_tab1.place(x=10, y=65, width=380, height=15)
lab_sort_numbers4_tab1 = Label(tab1, text=' и нажмите кнопку добавить', font='Arial 9')
lab_sort_numbers4_tab1.place(x=10, y=85, width=380, height=15)

entry_sort_numbers_tab1 = Entry(tab1, font='Arial 10 bold', width=15, borderwidth=2)
entry_sort_numbers_tab1.place(x=10, y=110, width=180, height=30)

button_sort_numbers_tab1 = Button(tab1, text='Добавить', font='Arial 10 ', command=get_data_list_numbers)
button_sort_numbers_tab1.place(x=200, y=110, width=180, height=30)

lab_sort_numbers5_tab1 = Label(tab1, text='Итоговый список чисел', font='Arial 10')
lab_sort_numbers5_tab1.place(x=10, y=145, width=380, height=30)

entry_sort_numbers2_tab1 = Entry(tab1, font='Arial 10 bold', width=15, borderwidth=2, state="readonly")
entry_sort_numbers2_tab1.place(x=10, y=180, width=240, height=30)

button2_sort_numbers2_tab1 = Button(tab1, text='Очистить список', font='Arial 10', command=clear_data)
button2_sort_numbers2_tab1.place(x=255, y=180, width=120, height=30)

button2_sort_numbers3_tab1 = Button(tab1, text='Отсортировать и получить список', font='Arial 10 ',
                                    command=get_result_sort_numbers)
button2_sort_numbers3_tab1.place(x=10, y=215, width=380, height=30)

lab_sort_numbers6_tab1 = Label(tab1, text='Сортированный список', font='Arial 10')
lab_sort_numbers6_tab1.place(x=10, y=250, width=380, height=30)

entry_sort_numbers3_tab1 = Entry(tab1, font='Arial 10 bold', width=15, borderwidth=2, state="readonly")
entry_sort_numbers3_tab1.place(x=10, y=290, width=380, height=30)

lab_sort_numbers8_tab1 = Label(tab1, text='Введите элемент для поиска', font='Arial 10')
lab_sort_numbers8_tab1.place(x=10, y=315, width=240, height=30)

entry_sort_numbers5_tab1 = Entry(tab1, font='Arial 10 bold', width=15, borderwidth=2)
entry_sort_numbers5_tab1.place(x=245, y=315, width=120, height=30)

button2_sort_numbers4_tab1 = Button(tab1, text='Поиск в списке', font='Arial 10 ',
                                    command=sorting_rec_find)
button2_sort_numbers4_tab1.place(x=10, y=350, width=380, height=30)

lab_sort_numbers8_tab1 = Label(tab1, text='Позиция элемента ', font='Arial 10')
lab_sort_numbers8_tab1.place(x=10, y=385, width=380, height=30)

lab_sort_numbers9_tab1 = Label(tab1, text='Позиция списке', font='Arial 9')
lab_sort_numbers9_tab1.place(x=10, y=420, width=380, height=15)

entry_sort_numbers6_tab1 = Entry(tab1, font='Arial 10 bold', width=15, borderwidth=2, state="readonly")
entry_sort_numbers6_tab1.place(x=10, y=440, width=380, height=30)

lab_sort_numbers10_tab1 = Label(tab1, text='Перевод десятичного числа в двоичное', font='Arial 10 bold')
lab_sort_numbers10_tab1.place(x=10, y=500, width=380, height=15)

lab_sort_numbers11_tab1 = Label(tab1, text='Введите десятичное число для перевода в двоичное', font='Arial 9 ')
lab_sort_numbers11_tab1.place(x=10, y=550, width=380, height=15)

entry_sort_numbers7_tab1 = Entry(tab1, font='Arial 10 bold', width=15, borderwidth=2)
entry_sort_numbers7_tab1.place(x=10, y=570, width=380, height=30)

button2_sort_numbers5_tab1 = Button(tab1, text='Перевод', font='Arial 10 ',
                                    command=converting_numbers)
button2_sort_numbers5_tab1.place(x=10, y=605, width=380, height=30)

lab_sort_numbers11_tab1 = Label(tab1, text='Итоговый результат', font='Arial 9 ')
lab_sort_numbers11_tab1.place(x=10, y=640, width=380, height=15)

text_rec_tab1 = Text(tab1, font='Arial 10', width=15, borderwidth=2, wrap="char", state="disabled")
text_rec_tab1.place(x=10, y=660, width=380, height=60)


lab_prime_number1_tab2 = Label(tab2, text='Проверка на то простое ли число и поиск НОД', font='Arial 10 bold')
lab_prime_number1_tab2.place(x=10, y=10, width=380, height=15)

lab_prime_number2_tab2 = Label(tab2, text='Введите число для определения простое оно или нет', font='Arial 9')
lab_prime_number2_tab2.place(x=10, y=30, width=380, height=30)

entry_prime_number2_tab2 = Entry(tab2, font='Arial 10 bold', width=15, borderwidth=2)
entry_prime_number2_tab2.place(x=10, y=65, width=380, height=30)

button_prime_number2_tab2 = Button(tab2, text='Проверить', font='Arial 10 ', command=get_test_prime_number)
button_prime_number2_tab2.place(x=10, y=100, width=180, height=30)

entry_prime_number3_tab2 = Entry(tab2, font='Arial 10 bold', width=15, borderwidth=2, state="readonly")
entry_prime_number3_tab2.place(x=10, y=135, width=380, height=30)

lab_prime_number3_tab2 = Label(tab2, text='Введите числа для поиска НОД', font='Arial 10 bold')
lab_prime_number3_tab2.place(x=10, y=170, width=380, height=30)

lab_prime_number4_tab2 = Label(tab2, text='Первое число', font='Arial 9')
lab_prime_number4_tab2.place(x=10, y=205, width=180, height=30)

lab_prime_number5_tab2 = Label(tab2, text='Второе число', font='Arial 9')
lab_prime_number5_tab2.place(x=200, y=205, width=180, height=30)

entry_prime_number4_tab2 = Entry(tab2, font='Arial 10 bold', width=15, borderwidth=2)
entry_prime_number4_tab2.place(x=10, y=240, width=180, height=30)

entry_prime_number5_tab2 = Entry(tab2, font='Arial 10 bold', width=15, borderwidth=2)
entry_prime_number5_tab2.place(x=200, y=240, width=180, height=30)


button_prime_number3_tab2 = Button(tab2, text='Проверить', font='Arial 10 ', command=get_nod)
button_prime_number3_tab2.place(x=10, y=275, width=380, height=30)

entry_prime_number6_tab2 = Entry(tab2, font='Arial 10 bold', width=15, borderwidth=2, state="readonly")
entry_prime_number6_tab2.place(x=10, y=310, width=380, height=30)


lesson_6.mainloop()