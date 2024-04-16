from tkinter import *              # Добавляем библиотеку Ткинтер
from tkinter import messagebox as mb    # Добавляем метод библиотеки на всплывающие сообщения

calc = Tk()              # Объявляем класс

calc.title("Калькулятор")

# Получаем ширину и высоту экрана
screen_width = calc.winfo_screenwidth()
screen_height = calc.winfo_screenheight()

# Вычисляем координаты окна приложения
window_width = 400
window_height = 625
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
calc.geometry(f"{window_width}x{window_height}+{x}+{y}")

calc.resizable(None, None)   # Запрещаем изменять размер окна

calc["bg"] = "gray22"  # gray gray0-99   # Устанавливаем цвет фона

# Добавляем функцию вывода нажатого символа и его параллельной проверки


def insert_data(text):
    check_str = entry.get()   # переносим данные из текстового поля в строку
    if check_str == '':
        last_char = 0
    else:
        # Получаем последний символ в текстовом поле для проверки на введение двух операторов
        last_char = check_str[len(check_str) - 1]

    if ((text == '+' or text == '-' or text == '*' or text == '/') and
            (last_char == '+' or last_char == '-' or last_char == '*' or last_char == '/')):
        mb.showwarning("Предупреждение", "Нельзя вводить несколько операторов подряд!!!!")
    else:
        # Если все в порядке добавляем введенную цифру/оператор в конец текстового поля
        entry.insert(END, text)


def get_result():  # Считаем результат
    try:
        result = eval(entry.get())  # Используем функцию/метод eval для расчета данных по всей строке целиком
        entry.delete(0, END)
        entry.insert(END, result)

    except ZeroDivisionError:   # Перехват ошибки деления на 0
        mb.showwarning("Предупреждение", "На 0 делить нельзя")
        entry.delete(0, END)


def clean_textbox():  # Функция очистки текстового поля
    entry.delete(0, END)


# Рисуем кнопки калькулятора


button_list = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '+', '-', '*', '/', '=', 'CE', '.')

entry = Entry(font='Arial 15 bold', width=15, borderwidth=2)
entry.place(x=5, y=10, width=385, height=105)

button_1 = Button(text=button_list[0], font='Arial 15 bold', width=15,
                  command=lambda: insert_data(button_list[0]))
button_1.place(x=5, y=135, width=70, height=105)

button_2 = Button(text=button_list[1], font='Arial 15 bold', width=15,
                  command=lambda: insert_data(button_list[1]))
button_2.place(x=85, y=135, width=70, height=105)

button_3 = Button(text=button_list[2], font='Arial 15 bold', width=15,
                  command=lambda: insert_data(button_list[2]))
button_3.place(x=165, y=135, width=70, height=105)

button_4 = Button(text=button_list[3], font='Arial 15 bold', width=15,
                  command=lambda: insert_data(button_list[3]))
button_4.place(x=5, y=260, width=70, height=105)

button_5 = Button(text=button_list[4], font='Arial 15 bold', width=15,
                  command=lambda: insert_data(button_list[4]))
button_5.place(x=85, y=260, width=70, height=105)

button_6 = Button(text=button_list[5], font='Arial 15 bold', width=15,
                  command=lambda: insert_data(button_list[5]))
button_6.place(x=165, y=260, width=70, height=105)

button_7 = Button(text=button_list[6], font='Arial 15 bold', width=15,
                  command=lambda: insert_data(button_list[6]))
button_7.place(x=5, y=385, width=70, height=105)

button_8 = Button(text=button_list[7], font='Arial 15 bold', width=15,
                  command=lambda: insert_data(button_list[7]))
button_8.place(x=85, y=385, width=70, height=105)

button_9 = Button(text=button_list[8], font='Arial 15 bold', width=15,
                  command=lambda: insert_data(button_list[8]))
button_9.place(x=165, y=385, width=70, height=105)

button_null = Button(text=button_list[9], font='Arial 15 bold', width=15,
                     command=lambda: insert_data(button_list[9]))
button_null.place(x=5, y=505, width=70, height=105)

button_point = Button(text=button_list[16], font='Arial 15 bold', width=15,
                      command=lambda: insert_data(button_list[16]))
button_point.place(x=85, y=505, width=70, height=105)

button_plus = Button(text=button_list[10], font='Arial 15 bold', width=15,
                     command=lambda: insert_data(button_list[10]))
button_plus.place(x=245, y=135, width=70, height=105)

button_minus = Button(text=button_list[11], font='Arial 15 bold', width=15,
                      command=lambda: insert_data(button_list[11]))
button_minus.place(x=325, y=135, width=70, height=105)

button_multiplication = Button(text=button_list[12], font='Arial 15 bold', width=15,
                               command=lambda: insert_data(button_list[12]))
button_multiplication.place(x=245, y=260, width=70, height=105)

button_separation = Button(text=button_list[13], font='Arial 15 bold', width=15,
                           command=lambda: insert_data(button_list[13]))
button_separation.place(x=325, y=260, width=70, height=105)

button_ce = Button(text=button_list[15], font='Arial 15 bold', width=25,
                   command=clean_textbox)
button_ce.place(x=165, y=505, width=70, height=105)

button_result = Button(text=button_list[14], font='Arial 15 bold', width=25,
                       command=get_result)
button_result.place(x=245, y=385, width=150, height=225)


calc.mainloop()
