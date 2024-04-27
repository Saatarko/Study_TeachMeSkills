import csv  # Добавляем библиотеку csv
import json # Добавляем библиотеку json
from tkinter import *  # Добавляем библиотеку Ткинтер
import os   # Добавляем библиотеку os
import shutil   # Добавляем библиотеку shutil
import re           # Добавляем библиотеку re
from collections import Counter  # Добавляем библиотеку collections и метод Counter
from tkinter import ttk   # Добавляем метод tkinter

from My_Function import *  # Добавляем библиотеку Function

# region Объявление класса для меню и расчеты окна
# Объявляем класс
lesson_9_main_menu = Tk()

lesson_9_main_menu.title("Домашнее задание по теме 8")

# Получаем ширину и высоту экрана

screen_width = lesson_9_main_menu.winfo_screenwidth()
screen_height = lesson_9_main_menu.winfo_screenheight()

# Вычисляем координаты окна приложения
window_width = 600
window_height = 860
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

lesson_9_main_menu.geometry(f"{window_width}x{window_height}+{x}+{y}")
lesson_9_main_menu.resizable(None, None)  # Запрещаем изменять размер окна
lesson_9_main_menu["bg"] = "gray22"  # gray gray0-99   # Устанавливаем цвет фона

str_for_json_csv = []   # Объявляем глобальную переменную для json и csv


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
    lesson_9_main_menu.withdraw()
    lesson_9 = Toplevel(lesson_9_main_menu)
    lesson_9.title("Домашнее задание по теме 9")
    lesson_9.geometry(f"{window_width}x{window_height}+{x}+{y}")
    lesson_9.resizable(None, None)
    lesson_9["bg"] = "gray90"

    tab_control = ttk.Notebook(lesson_9)  # создаем подкласс для закладок

    tab1 = ttk.Frame(tab_control)  # создаем закладки
    tab2 = ttk.Frame(tab_control)
    tab3 = ttk.Frame(tab_control)

    tab_control.add(tab1, text='Текста и сортировка')
    tab_control.add(tab2, text='Работа с файлам')
    tab_control.add(tab3, text='Json и CSV')

    tab_control.pack(expand=1, fill='both')

    # region функции основной программы

    def get_data_os():          # Функция для получения данных от ОС

        temp_os = os.name      # Функция для получения названия системы
        temp_dir = os.getcwd()   # Функция для получения адреса рабочей директории

        text_os.config(state="normal")
        text_os.delete('1.0', END)
        text_os.insert(END, f' Система {temp_os} \n Рабочая дирректория - {temp_dir} \n')
        text_os.config(state="disabled")

    def check_dir(path):
        if os.path.exists(path) is False:    # Функция для проверки существования файла/директории
            os.mkdir(path)

    def check_info(file):           # Функция для подсчета размера файла
        file_info = os.stat(file)
        file_size = file_info.st_size
        return file_size

    def clean():      # Функция для сортировки по папкам

        path = 'Sort'    # Папка для отсортированных файлов
        path_ex = 'Unsort'  # Папка для несортированных файлов

        if os.path.exists(path) is False:   # Проверка на существование папки
            os.mkdir(path)

        folder_track = f'{path_ex}'  # папка отслеживания

        folder_move = f'{path}'  # папка куда будет переноситься
        video_format = ['mp4', 'mpg', 'avi', 'mpeg', 'mov']    # списки форматов файлов
        archive_format = ['rar', 'zip', '7z']
        text_format = ['txt', 'doc', 'docx']
        pic_format = ['jpg', 'png', 'svg', 'bmp']

        try:
            files = os.listdir(folder_track)      # проверяем директорию на наличие файлов для сортировки
            if len(files) == 0:
                raise ExceptionNullField    # вызываем ошибку если их там нет
        except ExceptionNullField('Сортировочная папка пустая'):
            mb.showwarning(f"Предупреждение", f"Сортировочная папка пустая")
        else:
            count = 0
            sum_size = 0
            for items in files:
                extension = items.split(".")   # разбиваем название файла на название и расширение

                if len(extension) > 1 and str(extension[1].lower()) in pic_format:

                    file = folder_track + "/" + items

                    move_pass = folder_move + "/Photos/" + items    # Создаем адрес директории  для фото
                    new_path = os.path.join(path, "Photos")
                    check_dir(new_path)

                    count += 1                  # Подсчет кол-ва файлов
                    sum_size += check_info(file)   # Подсчет размеров перемещаемых файлов

                    shutil.move(file, move_pass)     # Функция перемщения
                elif len(extension) > 1 and str(extension[1].lower()) in video_format:

                    file = folder_track + "/" + items
                    move_pass = folder_move + "/Video/" + items   # Создаем адрес директории  для видео
                    new_path = os.path.join(path, "Video")
                    check_dir(new_path)

                    count += 1
                    sum_size += check_info(file)

                    shutil.move(file, move_pass)
                elif len(extension) > 1 and str(extension[1].lower()) in text_format:

                    file = folder_track + "/" + items
                    move_pass = folder_move + "/Text/" + items   # Создаем адрес директории  для текста
                    new_path = os.path.join(path, "Text")
                    check_dir(new_path)

                    count += 1
                    sum_size += check_info(file)

                    shutil.move(file, move_pass)
                elif len(extension) > 1 and str(extension[1].lower()) in archive_format:

                    file = folder_track + "/" + items
                    move_pass = folder_move + "/Archive/" + items   # Создаем адрес директории  для архивов
                    new_path = os.path.join(path, "Archive")
                    check_dir(new_path)

                    count += 1
                    sum_size += check_info(file)

                    shutil.move(file, move_pass)

            text_os2.config(state="normal")
            text_os2.delete('1.0', END)
            text_os2.insert(END, f' Было сортировано {count} файлов \n Общим размером - {sum_size // 1000000} Мб\n')
            text_os2.config(state="disabled")

    def use_stop_list():   # Функция фильтровки текста по списку стоп слов
        try:                  # Проверки на то что бы данные были введены и соответствовали требованиям к данным

            file = entry_lab_imt1.get()
            if os.path.isfile(file) is False:
                raise IOError

        except IOError('Не удалось открыть файл'):
            mb.showwarning(f"Предупреждение", f"Не удалось найти/открыть файл")
        else:
            with open(file, 'r') as text_file:
                temp_text = text_file.read()
                res = temp_text.lower()
                try:
                    if os.path.isfile('stop_words.txt') is False:
                        raise IOError
                except IOError('Не удалось открыть файл'):
                    mb.showwarning(f"Предупреждение", f"Не удалось найти/открыть файл")
                else:
                    with open('stop_words.txt', 'r') as stop_text_file:    # открываем файл
                        stop_text_file = stop_text_file.read()
                        stop_text_file = stop_text_file.split(' ')   # сплитим его на отдельные слова
                    for _text in stop_text_file:  # проверяем наличие слова в стоп листе
                        regex = fr"{_text}\w"  # создаем регулярку с переменной
                        temp_str = re.findall(regex, temp_text, re.IGNORECASE)
                        for _word in temp_str:   # прогоняем по циклу и заменяем слова из стоп листа на *
                            temp_change = '*' * len(_word)
                            temp_text = re.sub(regex, temp_change, temp_text, re.IGNORECASE)

            text_os5.config(state="normal")
            text_os5.delete('1.0', END)
            text_os5.insert(END, f'Результаты проверки по запрещенным словам - {temp_text}')
            text_os5.config(state="disabled")

    def get_dupl_number():    # Функция поиска повториений слов в тексте

        try:         # Проверки на то что бы данные были введены и соответствовали требованиям к данным

            file = entry_lab_imt1.get()
            if os.path.isfile(file) is False:
                raise IOError
        except IOError('Не удалось открыть файл'):
            mb.showwarning(f"Предупреждение", f"Не удалось найти/открыть файл")
        else:
            with open(file, 'r') as text_file:
                temp_text = text_file.read()
                res = re.sub(r'[^\w\s]', '', temp_text)
                res = res.split(' ')
                res = list(map(lambda z: z.lower(), res))
                # Вызываем метод Counter и создаем словарь (ключ -элемент, значение повторения)
                count_frequency = Counter(res)

                count_frequency = sorted(count_frequency.items(), key=lambda item: item[1], reverse=True)

                for _word in count_frequency:
                    if len(_word[0]) > 2:  # Отсеиваем предлоги местоимения и прочее 1-2 буквенное
                        result_word = str(_word[0])
                        result_pos = _word[1]
                        break

            text_os5.config(state="normal")
            text_os5.delete('1.0', END)
            text_os5.insert(END, f'Слово "{result_word}" повторялось в тексте чаще всего. {result_pos} раз!')
            text_os5.config(state="disabled")

    def get_change_name():   # Функция замены ФИО в тексте

        try:    # Проверки на то что бы данные были введены и соответствовали требованиям к данным
            temp_text = text_os3.get('1.0', END)
            if temp_text == '':
                raise ExceptionNullField
        except ExceptionNullField('Пустое поле с текcтом'):
            mb.showwarning(f"Предупреждение", f"Поле с текстом для замены - пустое")

        else:
            # Дикая регулярка на проверку ФИО
            temp_text = re.sub(r'[А-ЯЁ][а-яё]{2,}([-][А-ЯЁ][а-яё]{2,})?\s[А-ЯЁ][а-яё]{2,}\s[А-ЯЁ][а-яё]{2,}',
                               'N', temp_text)

            text_os4.config(state="normal")
            text_os4.delete('1.0', END)
            text_os4.insert(END, temp_text)
            text_os4.config(state="disabled")

    def get_disciple():  # Функция загрузки данных из файла учеников и вывод тех у кого оценка ниже 3

        result_list = []
        try:    # Проверки на то что бы данные были введены и соответствовали требованиям к данным

            file = entry_lab_imt2.get()
            if os.path.isfile(file) is False:
                raise IOError
        except IOError('Не удалось открыть файл'):
            mb.showwarning(f"Предупреждение", f"Не удалось найти/открыть файл")
        else:
            with open(file, 'r') as text_file: # Считываем данные из файла
                temp_text = text_file.read()
                temp_text = re.split(r'\n+', temp_text)  # Сплитим по символу переноса строки

                for _word in temp_text:      # Прогоняем данные по списку. Т.к после сплита оценка 3 элемент списка
                    if len(_word) > 0:
                        _word = _word.split()
                        if int(_word[2]) <= 3:
                            result_list.append(_word)

                text_os6.config(state="normal")
                text_os6.delete('1.0', END)
                for result in result_list:
                    text_os6.insert(END, f'{result[0]} {result[1]} имеет оценку за контрольную {result[2]} \n')
                text_os6.config(state="disabled")

    def get_number_and_sum():  # Функция загрузки данных из файла и выбор всеъх чисел с последующим суммированием

        try:    # Проверки на то что бы данные были введены и соответствовали требованиям к данным
            file = entry_lab_imt3.get()
            if os.path.isfile(file) is False:
                raise IOError
        except IOError('Не удалось открыть файл'):
            mb.showwarning(f"Предупреждение", f"Не удалось найти/открыть файл")
        else:
            with open(file, 'r') as text_file:   # Считываем данные из файла
                temp_text = text_file.read()
                number_list = re.findall(r'\d+', temp_text) # Ищем в данных только цифры
                number_list = list(map(lambda z: int(z), number_list))   # Интуем все цифры в списке
                result = sum(number_list)  # Суммируем список

                text_os7.config(state="normal")
                text_os7.delete('1.0', END)
                text_os7.insert(END, f'Сумма числе в строке {temp_text}\n Составляет: {result} ')
                text_os7.config(state="disabled")

    def get_caesar():  # Функция загрузки данных из файла и прогонка через шифрование
        result_list = []
        try:    # Проверки на то что бы данные были введены и соответствовали требованиям к данным
            file = entry_lab_imt4.get()
            if os.path.isfile(file) is False:
                raise IOError
        except IOError('Не удалось открыть файл'):
            mb.showwarning(f"Предупреждение", f"Не удалось найти/открыть файл")
        else:
            with open(file, 'r') as text_file:   # Считываем данные с файла
                temp_text = text_file.read()
                result_text = re.split(r'\n+', temp_text)  # Сплитим по символу переноса строки
                count = 0
                for _word in result_text:
                    if len(_word) > 0:   # Пробегаемся по строкам попутно прогоняя их чреез шифрование цезаря
                        count += 1
                        temp_str = func_encryption(_word, count, 'Русский', 'vishener')
                        temp_str = ''.join(temp_str)
                        result_list.append(temp_str)

                text_os8.config(state="normal")
                text_os8.delete('1.0', END)
                text_os8.insert(END, f'Содержимое файла {result_text}\n после шифрования: {result_list} ')
                text_os8.config(state="disabled")

    def get_json_file():  # Функция загрузки данных из json
        try:    # Проверки на то что бы данные были введены и соответствовали требованиям к данным
            file = entry_lab_imt5.get()
            if os.path.isfile(file) is False:
                raise IOError
        except IOError('Не удалось открыть файл'):
            mb.showwarning(f"Предупреждение", f"Не удалось найти/открыть файл")
        else:
            with open(file, 'r') as text_file:   # Считываем данные с файла

                global str_for_json_csv    # Даем добро на запись и использование глобальной переменной
                str_for_json_csv = json.load(text_file)   # Зписываем данные в глобальную переменную

                text_os9.config(state="normal")
                text_os9.delete('1.0', END)
                text_os9.insert(END, f'Текущий список словарей\n {str_for_json_csv}\n')

                text_os9.config(state="disabled")

    def add_dict_file():   # Функция добавки нового словаря

        try:                 # Проверки на то что бы данные были введены и соответствовали требованиям к данным
            name = entry_lab_imt6.get()
            date = entry_lab_imt7.get()
            height = entry_lab_imt8.get()
            weight = entry_lab_imt9.get()
            car = entry_lab_imt10.get()
            languages = entry_lab_imt11.get()
            global str_for_json_csv
            if not name or not date or not height or not weight or not car or not languages or not str_for_json_csv:
                raise ExceptionNullField('Не все данные заполнены')
        except ExceptionNullField:
            mb.showwarning(f"Ошибка,", 'Не все данные заполнены!')
        else:

            try:
                height, check = value_check_func(height)
                weight, check2 = value_check_func(weight)
                car, check4 = value_check_func(car)
                check3 = check_date_func(date)

                if check is False or check2 is False or check3 is False or check4 is False:
                    raise ExceptionNegativeNumber('Некорректные данные')
            except ExceptionNegativeNumber:
                mb.showwarning(f"Ошибка,", 'Введены некорректные данные')
            else:
                try:

                    if height <= 0 or weight <= 0 or car <= 0:
                        raise ExceptionNegativeNumber('В данных полях не могут быть отрицательные числа')
                except ExceptionNegativeNumber:
                    mb.showwarning(f"Ошибка,", 'В цифровых полях не могут быть отрицательные числа')
                else:
                    if car == 0:
                        car = 'false'
                    else:
                        car = 'true'
                languages = languages.split()

                # Создаем новые словарь из данных
                new_dict = {'name': name, 'birthday': date, 'height': height, 'weight': weight,
                            'car': car, 'languages': languages}

                str_for_json_csv.append(new_dict)  # Добавляем его в список

                text_os10.config(state="normal")
                text_os10.delete('1.0', END)
                text_os10.insert(END, f'Текущий список словарей\n {str_for_json_csv}\n')

                text_os10.config(state="disabled")

    def save_json():  # Функция сохранения данных в формате json
        with open('new_employees.json', 'w') as text_file:
            json.dump(str_for_json_csv, text_file, sort_keys=True, indent=2)

    def save_csv():   # Функция сохранения данных в формате csv
        with open('new_employees.csv', 'w') as text_file:
            writer = csv.DictWriter(
                text_file, fieldnames=list(str_for_json_csv[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
            writer.writeheader()
            for d in str_for_json_csv:
                writer.writerow(d)

    def sorted_dict():    # Функция сортировки данных
        global str_for_json_csv
        result_list = []
        type_sort = combobox_os.get()
        value = entry_lab_imt12.get()


        try:
            if not type_sort or not value or not str_for_json_csv:
                raise ExceptionNullField('Не все данные заполнены')
        except ExceptionNullField:
            mb.showwarning(f"Ошибка,", 'Не все данные заполнены')
        else:
            try:
                if type_sort == 'Год рождения':
                    check = check_date_func(value)
                    if check is False:
                        raise ExceptionNegativeNumber
            except ExceptionNegativeNumber('Неправильный формат даты'):
                mb.showwarning(f"Ошибка,", 'Неправильный формат даты')
            else:
                text_os11.config(state="normal")
                text_os11.delete('1.0', END)

                if type_sort == 'Имя':

                    from_dist = list(map(lambda z: z.get('name'), str_for_json_csv))
                    regex = fr"{value}\s"
                    for word in from_dist:     # Проверки на совпадения имени и значения словаря
                        d = re.search(regex, word)
                        if d is not None:
                            result_list = list([i for i in str_for_json_csv if i['name'] == word])
                    text_os11.insert(END, f'Результат фильтрации по имени\n {result_list}\n')

                elif type_sort == 'Год рождения':
                    value = datetime.strptime(value, '%d.%m.%Y')
                    for word in str_for_json_csv:
                        result_list = list([i for i in str_for_json_csv if
                                            datetime.strptime(i['birthday'], '%d.%m.%Y') <= value])
                    temp_heght = list(map(lambda z: z.get('weight'), result_list))
                    average_heght = (sum(temp_heght)) / len(temp_heght)
                    text_os11.insert(END, f'Результат фильтрации по году рождения\n {result_list}\n.'
                                          f'Средний рот этих сотрудников составляет {average_heght}')

                elif type_sort == 'ЯП':
                    result_list = list([i for i in str_for_json_csv if value in i['languages']])
                    text_os11.insert(END, f'Результат фильтрации по языку\n {result_list}\n')

                text_os11.config(state="disabled")

    def on_close():  # Кнопка закрытия на крестик

        lesson_9_main_menu.destroy()

    lesson_9.protocol('WM_DELETE_WINDOW', on_close)

    # end region

    # region Рисование кнопок и подписей вкладки программы

    # Первая вкладка

    lab_imt = Label(tab1, text='Получение данных об ОС', font='Arial 12 bold',
                    borderwidth=2, relief="solid")
    lab_imt.place(x=10, y=20, width=580, height=25)

    button_os = Button(tab1, text='Получить типа ОС и путь до папки', font='Arial 12 bold ',
                       command=get_data_os, borderwidth=2)
    button_os.place(x=10, y=55, width=580, height=30)

    text_os = Text(tab1, font='Arial 10', width=15, borderwidth=2, wrap="word", state="disabled")
    text_os.place(x=10, y=95, width=580, height=60)

    button_os2 = Button(tab1, text='Сортировать файлы по папкам (поместите файлы в папку Unsort)',
                        font='Arial 12 bold ', command=clean, borderwidth=2)
    button_os2.place(x=10, y=195, width=580, height=30)

    text_os2 = Text(tab1, font='Arial 10', width=15, borderwidth=2, wrap="word", state="disabled")
    text_os2.place(x=10, y=235, width=580, height=60)

    lab_imt2 = Label(tab1, text='Замена ФИО в тексте. Вставьте текст для замены', font='Arial 12 bold',
                     borderwidth=2, relief="solid")
    lab_imt2.place(x=10, y=330, width=580, height=25)

    text_os3 = Text(tab1, font='Arial 10', width=15, borderwidth=2, wrap="word", state="normal")
    text_os3.place(x=10, y=365, width=580, height=60)

    button_os3 = Button(tab1, text='Провести замену', font='Arial 12 bold ',
                        command=get_change_name, borderwidth=2)
    button_os3.place(x=10, y=435, width=580, height=30)

    text_os4 = Text(tab1, font='Arial 10', width=15, borderwidth=2, wrap="word", state="disabled")
    text_os4.place(x=10, y=485, width=580, height=60)

    lab_imt3 = Label(tab1, text='Считывание текста из файла. Поместите файл в раб. директорию',
                     font='Arial 12 bold', borderwidth=2, relief="solid")
    lab_imt3.place(x=10, y=565, width=580, height=25)

    lab_imt4 = Label(tab1, text='Название файла', font='Arial 12 bold',
                     borderwidth=2, relief="solid")
    lab_imt4.place(x=10, y=600, width=275, height=25)

    entry_lab_imt1 = Entry(tab1, font='Arial 10 bold', width=15, borderwidth=2)
    entry_lab_imt1.place(x=295, y=600, width=275, height=25)

    button_os3 = Button(tab1, text='Считать и вывести повторное слово', font='Arial 9 bold',
                        command=get_dupl_number, borderwidth=2)
    button_os3.place(x=10, y=635, width=275, height=30)

    button_os3 = Button(tab1, text='Считать и заменить запрещенные слова', font='Arial 9 bold',
                        command=use_stop_list, borderwidth=2)
    button_os3.place(x=295, y=635, width=275, height=30)

    text_os5 = Text(tab1, font='Arial 10', width=15, borderwidth=2, wrap="word", state="disabled")
    text_os5.place(x=10, y=675, width=580, height=60)

    lab_imt5 = Label(tab2, text='Считывание данных по ученикам из файла. Поместите файл в раб. директорию',
                     font='Arial 10 bold', borderwidth=2, relief="solid")
    lab_imt5.place(x=10, y=10, width=580, height=25)

    lab_imt4 = Label(tab2, text='Название файла', font='Arial 10 bold',
                     borderwidth=2, relief="solid")
    lab_imt4.place(x=10, y=40, width=275, height=25)

    entry_lab_imt2 = Entry(tab2, font='Arial 10 bold', width=15, borderwidth=2)
    entry_lab_imt2.place(x=295, y=40, width=275, height=25)

    button_os3 = Button(tab2, text='Считать и вывести учеников с оценками 3 и ниже', font='Arial 12 bold',
                        command=get_disciple, borderwidth=2)
    button_os3.place(x=10, y=70, width=580, height=30)

    text_os6 = Text(tab2, font='Arial 10', width=15, borderwidth=2, wrap="word", state="disabled")
    text_os6.place(x=10, y=110, width=580, height=60)

    lab_imt6 = Label(tab2, text='Считывание данных из файла и поиск чисел и их суммирования',
                     font='Arial 10 bold', borderwidth=2, relief="solid")
    lab_imt6.place(x=10, y=180, width=580, height=25)

    lab_imt5 = Label(tab2, text='Название файла', font='Arial 10 bold',
                     borderwidth=2, relief="solid")
    lab_imt5.place(x=10, y=215, width=275, height=25)

    entry_lab_imt3 = Entry(tab2, font='Arial 10 bold', width=15, borderwidth=2)
    entry_lab_imt3.place(x=295, y=215, width=275, height=25)

    button_os4 = Button(tab2, text='Считать и вывести данные и сумму', font='Arial 12 bold',
                        command=get_number_and_sum, borderwidth=2)
    button_os4.place(x=10, y=250, width=580, height=30)

    text_os7 = Text(tab2, font='Arial 10', width=15, borderwidth=2, wrap="word", state="disabled")
    text_os7.place(x=10, y=290, width=580, height=60)

    lab_imt7 = Label(tab2, text='Считывание данных из файла и шифрование шифром цезаря',
                     font='Arial 10 bold', borderwidth=2, relief="solid")
    lab_imt7.place(x=10, y=360, width=580, height=25)

    lab_imt6 = Label(tab2, text='Название файла', font='Arial 10 bold',
                     borderwidth=2, relief="solid")
    lab_imt6.place(x=10, y=395, width=275, height=25)

    entry_lab_imt4 = Entry(tab2, font='Arial 10 bold', width=15, borderwidth=2)
    entry_lab_imt4.place(x=295, y=395, width=275, height=25)

    button_os5 = Button(tab2, text='Считать и вывести данные', font='Arial 12 bold',
                        command=get_caesar, borderwidth=2)
    button_os5.place(x=10, y=430, width=580, height=30)

    text_os8 = Text(tab2, font='Arial 10', width=15, borderwidth=2, wrap="word", state="disabled")
    text_os8.place(x=10, y=470, width=580, height=100)

    lab_imt8 = Label(tab3, text='Считывание данных из файла JSON',
                     font='Arial 10 bold', borderwidth=2, relief="solid")
    lab_imt8.place(x=10, y=10, width=580, height=25)

    lab_imt9 = Label(tab3, text='Название файла', font='Arial 10 bold',
                     borderwidth=2, relief="solid")
    lab_imt9.place(x=10, y=45, width=275, height=25)

    entry_lab_imt5 = Entry(tab3, font='Arial 10 bold', width=15, borderwidth=2)
    entry_lab_imt5.place(x=295, y=45, width=275, height=25)

    button_os6 = Button(tab3, text='Считать JSON и вывести данные', font='Arial 12 bold',
                        command=get_json_file, borderwidth=2)
    button_os6.place(x=10, y=80, width=580, height=30)

    text_os9 = Text(tab3, font='Arial 10', width=15, borderwidth=2, wrap="word", state="disabled")
    text_os9.place(x=10, y=120, width=580, height=100)

    lab_imt10 = Label(tab3, text='Добавление нового студента',
                      font='Arial 10 bold', borderwidth=2, relief="solid")
    lab_imt10.place(x=10, y=230, width=580, height=25)

    lab_imt11 = Label(tab3, text='Имя', borderwidth=2, relief="solid")
    lab_imt11.place(x=10, y=265, width=90, height=25)

    lab_imt12 = Label(tab3, text='Дата рожд.', borderwidth=2, relief="solid")
    lab_imt12.place(x=110, y=265, width=90, height=25)

    lab_imt13 = Label(tab3, text='Рост', borderwidth=2, relief="solid")
    lab_imt13.place(x=210, y=265, width=90, height=25)

    lab_imt14 = Label(tab3, text='Вес', borderwidth=2, relief="solid")
    lab_imt14.place(x=310, y=265, width=90, height=25)

    lab_imt15 = Label(tab3, text='Машина (цифр)', borderwidth=2, relief="solid")
    lab_imt15.place(x=410, y=265, width=90, height=25)

    lab_imt16 = Label(tab3, text='ЯП', borderwidth=2, relief="solid")
    lab_imt16.place(x=510, y=265, width=80, height=25)

    entry_lab_imt6 = Entry(tab3, font='Arial 10 bold', width=15, borderwidth=2)
    entry_lab_imt6.place(x=10, y=300, width=90, height=25)

    entry_lab_imt7 = Entry(tab3, font='Arial 10 bold', width=15, borderwidth=2)
    entry_lab_imt7.place(x=110, y=300, width=90, height=25)

    entry_lab_imt8 = Entry(tab3, font='Arial 10 bold', width=15, borderwidth=2)
    entry_lab_imt8.place(x=210, y=300, width=90, height=25)

    entry_lab_imt9 = Entry(tab3, font='Arial 10 bold', width=15, borderwidth=2)
    entry_lab_imt9.place(x=310, y=300, width=90, height=25)

    entry_lab_imt10 = Entry(tab3, font='Arial 10 bold', width=15, borderwidth=2)
    entry_lab_imt10.place(x=410, y=300, width=90, height=25)

    entry_lab_imt11 = Entry(tab3, font='Arial 10 bold', width=15, borderwidth=2)
    entry_lab_imt11.place(x=510, y=300, width=80, height=25)

    button_os7 = Button(tab3, text='Собрать данные и добавить', font='Arial 12 bold',
                        command=add_dict_file, borderwidth=2)
    button_os7.place(x=10, y=335, width=580, height=30)

    text_os10 = Text(tab3, font='Arial 10', width=15, borderwidth=2, wrap="word", state="disabled")
    text_os10.place(x=10, y=375, width=580, height=100)

    button_os8 = Button(tab3, text='Сохранить данные в JSON', font='Arial 12 bold',
                        command=save_json, borderwidth=2)
    button_os8.place(x=10, y=485, width=275, height=30)

    button_os9 = Button(tab3, text='Сохранить данные в CSV', font='Arial 12 bold',
                        command=save_csv, borderwidth=2)
    button_os9.place(x=295, y=485, width=275, height=30)

    lab_imt17 = Label(tab3, text='Выберите элемент для поиска по словарю и укажите значение'
                      , borderwidth=2, relief="solid")
    lab_imt17.place(x=10, y=525, width=580, height=25)

    sort_items = ['Год рождения', 'Имя', 'ЯП']
    combobox_os = ttk.Combobox(tab3, values=sort_items, state="readonly")
    combobox_os.place(x=10, y=560, width=275, height=30)

    entry_lab_imt12 = Entry(tab3, font='Arial 10 bold', width=15, borderwidth=2)
    entry_lab_imt12.place(x=295, y=560, width=275, height=30)

    button_os10 = Button(tab3, text='Провести отбор данных', font='Arial 12 bold',
                         command=sorted_dict, borderwidth=2)
    button_os10.place(x=10, y=600, width=580, height=30)

    text_os11 = Text(tab3, font='Arial 10', width=15, borderwidth=2, wrap="word", state="disabled")
    text_os11.place(x=10, y=640, width=580, height=100)

    button_exit = Button(lesson_9, text='Выход', font='Arial 12 bold ', command=on_close, borderwidth=2)
    button_exit.place(x=10, y=800, width=580, height=30)

    # endregion


# region Функции вкладки меню


def get_exit():
    lesson_9_main_menu.destroy()


# endregion

# region Рисование кнопок и подписей вкладки меню


lab_menu = Label(lesson_9_main_menu, text='Домашнее задание по теме 9', font='Arial 20 bold')
lab_menu.place(x=10, y=450, width=580, height=30)

button_main_menu = Button(lesson_9_main_menu, text='Войти в программу', font='Arial 12 ', command=get_enter,
                          borderwidth=2)
button_main_menu.place(x=10, y=490, width=580, height=30)
button_main_menu2 = Button(lesson_9_main_menu, text='Выход', font='Arial 12 ', command=get_exit, borderwidth=2)
button_main_menu2.place(x=10, y=530, width=580, height=30)

lesson_9_main_menu.protocol('WM_DELETE_WINDOW', get_exit)

lesson_9_main_menu.mainloop()

# endregion
