import random       # Добавляем библиотеку рандома
from tkinter import *  # Добавляем библиотеку Ткинтер
from tkinter import ttk    # Добавляем модуль Ткинтера
from My_Function import *           # Добавляем библиотеку Function
from collections import Counter  # Добавляем библиотеку collections и метод Counter
from datetime import datetime, timedelta  # Добавляем библиотеку datetime и метод datetime, timedelta

lesson_5 = Tk()  # Объявляем класс

lesson_5.title("Расчеты по теме 5")

# Получаем ширину и высоту экрана
screen_width = lesson_5.winfo_screenwidth()
screen_height = lesson_5.winfo_screenheight()

# Вычисляем координаты окна приложения
window_width = 400
window_height = 860
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
lesson_5.geometry(f"{window_width}x{window_height}+{x}+{y}")

lesson_5.resizable(None, None)  # Запрещаем изменять размер окна
lesson_5["bg"] = "gray22"  # gray gray0-99   # Устанавливаем цвет фона


def get_data():         # Функция получения данных для расчета чисел фибоначи

    n = entry_fibonachi_tab2.get()

    n, check_reserve = check_value(n, 'digit')   # Проверяем на введение числа

    if check_reserve is True:
        fibo_list = calculation_fibonachi(n)                # Вызываем функцию расчета чисел Фибоначи
        entry_fibonachi_result_tab2.config(state="normal")
        entry_fibonachi_result_tab2.delete(0, END)
        entry_fibonachi_result_tab2.insert(END, f'{fibo_list}')
        entry_fibonachi_result_tab2.config(state="readonly")


def get_data_list_numbers(check):     # Функция получения данных для двух закладок (для числовых последовательностей)

    if check == 'tab2':
        n = entry_list_numbers_tab2.get()
        n, check_reserve = check_value(n, 'float')

        if check_reserve is True:
            list_numbers = entry_list_numbers2_tab2.get()
            list_numbers = list_numbers.split()
            list_numbers = [int(n) for n in list_numbers]  # Цифруем данные в списке

            list_numbers.append(n)

            entry_list_numbers2_tab2.config(state="normal")
            entry_list_numbers2_tab2.delete(0, END)
            entry_list_numbers_tab2.delete(0, END)
            entry_list_numbers2_tab2.insert(END, list_numbers)
            entry_list_numbers2_tab2.config(state="readonly")
    elif check == 'tab3':
        n = entry_sort_numbers_tab3.get()
        n, check_reserve = check_value(n, 'float')

        if check_reserve is True:
            list_numbers = entry_sort_numbers2_tab3.get()
            list_numbers = list_numbers.split()
            list_numbers = [int(n) for n in list_numbers]

            list_numbers.append(n)

            entry_sort_numbers2_tab3.config(state="normal")
            entry_sort_numbers_tab3.delete(0, END)
            entry_sort_numbers2_tab3.delete(0, END)
            entry_sort_numbers2_tab3.insert(END, list_numbers)
            entry_sort_numbers2_tab3.config(state="readonly")


def get_result_data_numbers():     # Функция подсчета максимума и минимума последовательности

    list_numbers = entry_list_numbers2_tab2.get()
    list_numbers = list_numbers.split()
    list_numbers = [int(n) for n in list_numbers]  # Цифруем данные в списке
    sum_list_numbers: int = sum(list_numbers)   # Суммируем элементы списка

    max_value: int = max(list_numbers)  # Ищем максимальный элемент

    min_value: int = min(list_numbers)  # Ищем минимальный элемент

    count_frequency = Counter(list_numbers)  # Вызываем метод Counter и создаем словарь (ключ -элемент, значение -повт)

    # Проверям словарь выписывая только повторы (ит.е у кого значение повторов больше 1).
    new_count_frequency = {k: v for k, v in count_frequency.items() if v != 1}

    if len(new_count_frequency) == 0:
        check = False
    else:
        check = True

    entry_list_numbers_result1_tab2.config(state="normal")
    entry_list_numbers_result1_tab2.delete(0, END)
    entry_list_numbers_result1_tab2.insert(END, sum_list_numbers)
    entry_list_numbers_result1_tab2.config(state="readonly")

    entry_list_numbers_result2_tab2.config(state="normal")
    entry_list_numbers_result2_tab2.delete(0, END)
    entry_list_numbers_result2_tab2.insert(END, max_value)
    entry_list_numbers_result2_tab2.config(state="readonly")

    entry_list_numbers_result3_tab2.config(state="normal")
    entry_list_numbers_result3_tab2.delete(0, END)
    entry_list_numbers_result3_tab2.insert(END, min_value)
    entry_list_numbers_result3_tab2.config(state="readonly")

    text_list_numbers_result4_tab2.config(state="normal")
    text_list_numbers_result4_tab2.delete('1.0', END)

    # По результам проверки выдаем результат, или в цикле создаем строку вписываю туда все повторения
    if check is False:
        text_list_numbers_result4_tab2.insert(END, 'Повторения отсутствуют.')
    else:
        end_str = ''
        for k, v in new_count_frequency.items():
            result4_str = f'Число {k} повторяется {v} раз,'
            end_str = end_str + result4_str

        text_list_numbers_result4_tab2.insert(END, end_str)

    text_list_numbers_result4_tab2.config(state="disabled")


def get_result_sort_numbers():   # Функция для поиска индекса элемента в сортированном и сдвин. сортированном

    list_sort_numbers = entry_sort_numbers2_tab3.get()
    list_sort_numbers = list_sort_numbers.split()
    list_sort_numbers = [int(n) for n in list_sort_numbers]

    count_frequency = Counter(list_sort_numbers)
    sort_numbers = list(count_frequency.keys())
    sort_numbers = sorted(sort_numbers)
    sort_numbers_shift = sort_numbers.copy()  # Создаем копию списка, что бы не  менять основной

    # Вызов функции сдвига
    sort_numbers_shift = circle_shift(sort_numbers_shift, (random.randrange(1, 15)))

    entry_sort_numbers3_tab3.config(state="normal")
    entry_sort_numbers3_tab3.delete(0, END)
    entry_sort_numbers3_tab3.insert(END, sort_numbers)
    entry_sort_numbers3_tab3.config(state="readonly")

    entry_sort_numbers4_tab3.config(state="normal")
    entry_sort_numbers4_tab3.delete(0, END)
    entry_sort_numbers4_tab3.insert(END, sort_numbers_shift)
    entry_sort_numbers4_tab3.config(state="readonly")


def sorting_find():  # Функция для бинарного поиска в сортир. списке и сдвинутом списке

    simbol_find = entry_sort_numbers5_tab3.get()

    list_sort = entry_sort_numbers3_tab3.get()

    index_find, check_list = bin_find(simbol_find, list_sort)

    entry_sort_numbers6_tab3.config(state="normal")
    entry_sort_numbers6_tab3.delete(0, END)
    entry_sort_numbers6_tab3.insert(END, f' Позиция {simbol_find} - {index_find}')
    entry_sort_numbers6_tab3.config(state="readonly")

    list_sort_shift = entry_sort_numbers4_tab3.get()
    list_sort_shift = list_sort_shift.split()
    list_sort_shift = [int(n) for n in list_sort_shift]

    list_sort_shift_temp = list_sort_shift.copy()

    max_value = max(list_sort_shift_temp)  # Находим максимальный элемент для сдвинутого списка чтобы его разделить

    temp = list_sort_shift_temp.index(max_value)

    first_list_sort_shift = list_sort_shift_temp[0:temp]  # Делим список на два списка
    second_list_sort_shift = list_sort_shift_temp[temp:]

    # Сначала проверяем один список
    index_find_first_list_sort_shift, check_list_sort_shift1 = bin_find(simbol_find, first_list_sort_shift)

    if check_list_sort_shift1 is True:
        index_find_list_sort_shift = index_find_first_list_sort_shift
    else:    # Если нужный элемент не в нем - то другой
        index_find_second_list_sort_shift, check_list_sort_shift2 = bin_find(simbol_find, second_list_sort_shift)
        index_find_list_sort_shift = index_find_second_list_sort_shift+temp

    entry_sort_numbers7_tab3.config(state="normal")
    entry_sort_numbers7_tab3.delete(0, END)
    entry_sort_numbers7_tab3.insert(END, f' Позиция {simbol_find} - {index_find_list_sort_shift}')
    entry_sort_numbers7_tab3.config(state="readonly")


def clear_data(check):  # Кнопка очищения полей для списка чисел

    if check == 'tab2':
        entry_list_numbers2_tab2.config(state="normal")
        entry_list_numbers2_tab2.delete(0, END)
        entry_list_numbers2_tab2.config(state="readonly")
    elif check == 'tab3':
        entry_sort_numbers2_tab3.config(state="normal")
        entry_sort_numbers2_tab3.delete(0, END)
        entry_sort_numbers2_tab3.config(state="readonly")


def current_date():    # Функция получения текущей даты
    now = datetime.now()
    dt_string = now. strftime("%d.%m.%Y")
    entry3_masha_tab1.delete(0, END)
    entry3_masha_tab1.insert(END, dt_string)


def masha_date_result():      # Функция расчета для покупки смартфона

    summa = entry_masha_tab1.get()
    contribution = entry2_masha_tab1.get()
    start_date = entry3_masha_tab1.get()
    if len(summa) != 0 or len(contribution) != 0 or len(start_date) != 0:   # Проверяем не пустые ли поля
        summa, check_reserve = check_value(summa, 'digit')
        contribution, check_reserve = check_value(contribution, 'float')
        check_date = check_date_func(start_date)
    else:
        mb.showwarning(f"Предупреждение", 'Не все данные заполнены!')
        check_date = False

    if check_date is False:
        entry3_masha_tab1.delete(0, END)
    elif check_date is True and (summa != 0 or contribution != 0):

        count_day = int(((summa // contribution)//6)*7)  # Расчитываем дни с учетом, что вовскресенье выходной
        start_date_str = datetime.strptime(start_date, '%d.%m.%Y')
        delta = timedelta(days=count_day)
        end_date = start_date_str + delta

    text_masha_tab1.config(state="normal")
    text_masha_tab1.delete('1.0', END)
    text_masha_tab1.insert(END, f'Окончательная дата расчета - {end_date:%d.%m.%Y}, '
                                f'или через {count_day} дней. Учтено, что воскресные деньги на киношку!')
    text_masha_tab1.config(state="disabled")


tab_control = ttk.Notebook(lesson_5)   # создаем клас для закладок

tab1 = ttk.Frame(tab_control)   # создаем закладки
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Маша и телефон')
tab_control.add(tab2, text='Списки чисел')
tab_control.add(tab3, text='Бинарный поиск')
tab_control.pack(expand=1, fill='both')

# Рисование кнопок и подписей

lab_entry_fibonachi_tab2 = Label(tab2, text='Вывод последовательности Фибоначи', font='Arial 10 bold')
lab_entry_fibonachi_tab2.place(x=10, y=10, width=380, height=25)

lab_entry_fibonachi_tab2 = Label(tab2, text='Введите требуемую длинну последовательности ', font='Arial 9')
lab_entry_fibonachi_tab2.place(x=10, y=40, width=290, height=40)

entry_fibonachi_tab2 = Entry(tab2, font='Arial 10 bold', width=15, borderwidth=2)
entry_fibonachi_tab2.place(x=310, y=40, width=80, height=40)

button_entry_fibonachi_tab2 = Button(tab2, text='Рассчитать и отобразить', font='Arial 10 ', command=get_data)
button_entry_fibonachi_tab2.place(x=10, y=90., width=380, height=30)

lab_entry_fibonachi_tab2 = Label(tab2, text='Последовательность Фибоначи', font='Arial 10')
lab_entry_fibonachi_tab2.place(x=10, y=130, width=380, height=30)

entry_fibonachi_result_tab2 = Entry(tab2, font='Arial 10 bold', width=15, borderwidth=2, state="readonly")
entry_fibonachi_result_tab2.place(x=10, y=170, width=380, height=30)

canvas_tab2 = Canvas(tab2, width=380, height=10, bg="gray", cursor="pencil")
canvas_tab2.place(x=10, y=215)

lab_list_numbers1_tab2 = Label(tab2, text='Вывод данных по списку чисел', font='Arial 10 bold')
lab_list_numbers1_tab2.place(x=10, y=280, width=380, height=30)
lab_list_numbers2_tab2 = Label(tab2, text='Чтобы добавить число в список введите его в поле', font='Arial 9')
lab_list_numbers2_tab2.place(x=10, y=320, width=380, height=15)
lab_list_numbers2_tab2 = Label(tab2, text=' и нажмите кнопку добавить', font='Arial 9')
lab_list_numbers2_tab2.place(x=10, y=340, width=380, height=15)

entry_list_numbers_tab2 = Entry(tab2, font='Arial 10 bold', width=15, borderwidth=2)
entry_list_numbers_tab2.place(x=10, y=360, width=180, height=30)

button_list_numbers_tab2 = Button(tab2, text='Добавить', font='Arial 10 ',
                                  command=lambda: get_data_list_numbers('tab2'))
button_list_numbers_tab2.place(x=200, y=360., width=180, height=30)

lab_list_numbers3_tab2 = Label(tab2, text='Итоговый список чисел', font='Arial 10')
lab_list_numbers3_tab2.place(x=10, y=400, width=380, height=30)

entry_list_numbers2_tab2 = Entry(tab2, font='Arial 10 bold', width=15, borderwidth=2, state="readonly")
entry_list_numbers2_tab2.place(x=10, y=435, width=250, height=30)

button2_list_numbers_tab2 = Button(tab2, text='Очистить список', font='Arial 10',
                                   command=lambda: clear_data('tab2'))
button2_list_numbers_tab2.place(x=270, y=435, width=120, height=30)

button2_list_numbers_tab2 = Button(tab2, text='Расчитать данные по списку', font='Arial 10 ',
                                   command=get_result_data_numbers)
button2_list_numbers_tab2.place(x=10, y=470., width=380, height=30)

entry_list_numbers_result1_tab2 = Entry(tab2, font='Arial 10', width=15, borderwidth=2, state="readonly")
entry_list_numbers_result1_tab2.place(x=10, y=505, width=125, height=30)
entry_list_numbers_result2_tab2 = Entry(tab2, font='Arial 10', width=15, borderwidth=2, state="readonly")
entry_list_numbers_result2_tab2.place(x=140, y=505, width=125, height=30)
entry_list_numbers_result3_tab2 = Entry(tab2, font='Arial 10', width=15, borderwidth=2, state="readonly")
entry_list_numbers_result3_tab2.place(x=270, y=505, width=125, height=30)
lab_list_numbers_result1_tab2 = Label(tab2, text='Cумма чисел', font='Arial 9')
lab_list_numbers_result1_tab2.place(x=10, y=540, width=125, height=15)
lab_list_numbers_result2_tab2 = Label(tab2, text='MAX элемент', font='Arial 9')
lab_list_numbers_result2_tab2.place(x=140, y=540, width=125, height=15)
lab_list_numbers_result3_tab2 = Label(tab2, text='MIN элемент', font='Arial 9')
lab_list_numbers_result3_tab2.place(x=270, y=540, width=125, height=15)
lab_list_numbers_result4_tab2 = Label(tab2, text='Результаты проверки на уникальные данные', font='Arial 9')
lab_list_numbers_result4_tab2.place(x=10, y=560, width=380, height=15)

text_list_numbers_result4_tab2 = Text(tab2, font='Arial 10', width=15, borderwidth=2, wrap="word", state="disabled")
text_list_numbers_result4_tab2.place(x=10, y=580, width=380, height=60)

lab_sort_numbers1_tab3 = Label(tab3, text='Бинарный поиск по сортированному списку', font='Arial 10 bold')
lab_sort_numbers1_tab3.place(x=10, y=10, width=380, height=15)

lab_sort_numbers2_tab3 = Label(tab3, text='Вывод данных по списку чисел', font='Arial 10')
lab_sort_numbers2_tab3.place(x=10, y=30, width=380, height=30)
lab_sort_numbers3_tab3 = Label(tab3, text='Чтобы добавить число в список введите его в поле', font='Arial 9')
lab_sort_numbers3_tab3.place(x=10, y=65, width=380, height=15)
lab_sort_numbers4_tab3 = Label(tab3, text=' и нажмите кнопку добавить', font='Arial 9')
lab_sort_numbers4_tab3.place(x=10, y=85, width=380, height=15)

entry_sort_numbers_tab3 = Entry(tab3, font='Arial 10 bold', width=15, borderwidth=2)
entry_sort_numbers_tab3.place(x=10, y=110, width=180, height=30)

button_sort_numbers_tab3 = Button(tab3, text='Добавить', font='Arial 10 ',
                                  command=lambda: get_data_list_numbers('tab3'))
button_sort_numbers_tab3.place(x=200, y=110, width=180, height=30)

lab_sort_numbers5_tab3 = Label(tab3, text='Итоговый список чисел', font='Arial 10')
lab_sort_numbers5_tab3.place(x=10, y=145, width=380, height=30)

entry_sort_numbers2_tab3 = Entry(tab3, font='Arial 10 bold', width=15, borderwidth=2, state="readonly")
entry_sort_numbers2_tab3.place(x=10, y=180, width=240, height=30)

button2_sort_numbers2_tab3 = Button(tab3, text='Очистить список', font='Arial 10',
                                    command=lambda: clear_data('tab3'))
button2_sort_numbers2_tab3.place(x=255, y=180, width=120, height=30)

button2_sort_numbers3_tab3 = Button(tab3, text='Отсортировать и получить списки', font='Arial 10 ',
                                    command=get_result_sort_numbers)
button2_sort_numbers3_tab3.place(x=10, y=215, width=380, height=30)

lab_sort_numbers6_tab3 = Label(tab3, text='Сортированный список', font='Arial 10')
lab_sort_numbers6_tab3.place(x=10, y=250, width=380, height=30)

entry_sort_numbers3_tab3 = Entry(tab3, font='Arial 10 bold', width=15, borderwidth=2, state="readonly")
entry_sort_numbers3_tab3.place(x=10, y=290, width=380, height=30)

lab_sort_numbers7_tab3 = Label(tab3, text='Сортированный список со смещением (рандом)', font='Arial 10')
lab_sort_numbers7_tab3.place(x=10, y=325, width=380, height=30)

entry_sort_numbers4_tab3 = Entry(tab3, font='Arial 10 bold', width=15, borderwidth=2, state="readonly")
entry_sort_numbers4_tab3.place(x=10, y=360, width=380, height=30)

lab_sort_numbers8_tab3 = Label(tab3, text='Введите элемент для поиска', font='Arial 10')
lab_sort_numbers8_tab3.place(x=10, y=395, width=240, height=30)

entry_sort_numbers5_tab3 = Entry(tab3, font='Arial 10 bold', width=15, borderwidth=2)
entry_sort_numbers5_tab3.place(x=245, y=395, width=120, height=30)

button2_sort_numbers4_tab3 = Button(tab3, text='Поиск по обоим спискам', font='Arial 10 ',
                                    command=sorting_find)
button2_sort_numbers4_tab3.place(x=10, y=430, width=380, height=30)

lab_sort_numbers8_tab3 = Label(tab3, text='Позиция элемента в обоих списках', font='Arial 10')
lab_sort_numbers8_tab3.place(x=10, y=465, width=380, height=30)

lab_sort_numbers9_tab3 = Label(tab3, text='Поз. в сорт. списке', font='Arial 9')
lab_sort_numbers9_tab3.place(x=10, y=500, width=180, height=15)

lab_sort_numbers10_tab3 = Label(tab3, text='Поз. в списке со сдвигом', font='Arial 9')
lab_sort_numbers10_tab3.place(x=190, y=500, width=180, height=15)

entry_sort_numbers6_tab3 = Entry(tab3, font='Arial 10 bold', width=15, borderwidth=2, state="readonly")
entry_sort_numbers6_tab3.place(x=10, y=520, width=180, height=30)

entry_sort_numbers7_tab3 = Entry(tab3, font='Arial 10 bold', width=15, borderwidth=2, state="readonly")
entry_sort_numbers7_tab3.place(x=190, y=520, width=180, height=30)

lab_masha_tab1 = Label(tab1, text='Маша хочет купить новый телефон', font='Arial 12')
lab_masha_tab1.place(x=10, y=10, width=380, height=15)

canvas = Canvas(tab1, height=350, width=250)
img1 = PhotoImage(file="1.png")
image1 = canvas.create_image(0, 0, anchor='nw', image=img1)
canvas.place(x=80, y=45, width=250, height=315)

lab2_masha_tab1 = Label(tab1, text='Стоимость', font='Arial 9')
lab2_masha_tab1.place(x=10, y=360, width=180, height=15)

entry_masha_tab1 = Entry(tab1, font='Arial 10 bold', width=15, borderwidth=2)
entry_masha_tab1.place(x=10, y=380, width=180, height=30)

lab3_masha_tab1 = Label(tab1, text='Возмож. ежедневный взнос', font='Arial 9')
lab3_masha_tab1.place(x=200, y=360, width=180, height=15)

entry2_masha_tab1 = Entry(tab1, font='Arial 10 bold', width=15, borderwidth=2)
entry2_masha_tab1.place(x=200, y=380, width=180, height=30)

lab3_masha_tab1 = Label(tab1, text='Дата начала сбора денег (в формате ДД.ММ.ГГ)', font='Arial 9')
lab3_masha_tab1.place(x=10, y=415, width=350, height=15)

entry3_masha_tab1 = Entry(tab1, font='Arial 10 bold', width=15, borderwidth=2)
entry3_masha_tab1.place(x=10, y=440, width=180, height=30)

button_masha_tab1 = Button(tab1, text='Подставить текущую дату', font='Arial 10 ',
                           command=current_date)
button_masha_tab1.place(x=200, y=440, width=180, height=30)

button2_masha_tab1 = Button(tab1, text='Рассчитать дату покупки смартфона', font='Arial 10 ',
                            command=masha_date_result)
button2_masha_tab1.place(x=10, y=475, width=380, height=30)

text_masha_tab1 = Text(tab1, font='Arial 10', width=15, borderwidth=2, wrap="word", state="disabled")
text_masha_tab1.place(x=10, y=510, width=380, height=30)

lesson_5.mainloop()
