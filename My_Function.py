from datetime import datetime
from tkinter import messagebox as mb


def check_value(a, func_type):
    """Функция проверки значений на число type(a)- list, func_type - 'digit' или 'float'"""
    external_verification = False
    check = False
    list_sizes = ''

    if isinstance(a, str) and a.isdigit() is True:
        list_sizes = list(map(int, a.split()))
        external_verification = True
    elif isinstance(a, list):
        list_sizes = a
        external_verification = True
    else:
        mb.showwarning(f"Предупреждение", 'Некорректные символы. Только цифры!')
        check = False

    if external_verification is True:
        int_list = []

        for i in range(0, len(list_sizes)):

            if func_type == 'digit':
                try:  # Проверка на то что введенные данные число
                    int_list = int(list_sizes[i])

                    check = True

                except ValueError:  # Перехват ошибки (если данные не числовые)
                    mb.showwarning(f"Предупреждение", f"{list_sizes[i]} не цифра")
                    check = False

            elif func_type == 'float':
                try:  # Проверка на то что введенные данные число
                    try:  # Проверка на то что введенные данные число
                        int_list = int(list_sizes[i])

                        check = True

                    except ValueError:  # Перехват ошибки (если данные не числовые)
                        check = False
                    if check is False:
                        int_list = float(list_sizes[i])
                        check = True

                except ValueError:  # Перехват ошибки (если данные не числовые)
                    mb.showwarning(f"Предупреждение", f"{list_sizes[i]} не цифра")
                    check = False
    else:
        int_list = 0
        check = False

    return int_list, check


def calculation_fibonachi(n):
    """Функция расчета чисел Фибоначи n- порядок цифр для отображения"""
    fib1 = 0
    fib2 = 1
    fibo_list = [fib2]

    for i in range(0, n):
        fib1, fib2 = fib2, fib1 + fib2
        fibo_list.append(fib2)

    return fibo_list


def circle_shift(lst, steps):
    """Функция циклического сдвига. lst - список чисел. steps - шаг сдвига"""

    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())

    return lst


def bin_find(value, a):
    """Функция бинарного поиска, value - искомое значение, a - список чисел"""

    if isinstance(a, str):  # Проверяем что мы получили, если строка, сплитим ее до списка, и цифруем
        c = a.split()
        c = [int(n) for n in c]
    else:
        c = a  # если нет, то нет

    check = False
    value = int(value)

    mid = len(c) // 2
    low = 0
    high = len(c) - 1

    while c[mid] != value and low <= high:
        if value > c[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if c[mid] == value:
        check = True

    return mid, check


def check_date_func(d):
    """Функция проверки даты. d- дата. Если формат даты совпадает с маской, то функция возвращает True"""
    check = False
    if len(d.split('.')) == 3:
        try:
            datetime.strptime(d, '%d.%m.%Y')
            check = True
        except ValueError:  # Перехват ошибки (если данные не числовые):
            mb.showwarning("Предупреждение", "Формат даты не тот")
            check = False

    return check


def bin_rec_find(value, low, high, mid, a):
    """Функция бинарного рекурсивного поиска, value - искомое значение, low и high - верхняя и нижняя  границы списка
    , a - список чисел, state - статус вызова, снаружи или рекурсия"""

    if isinstance(a, str):  # Проверяем что мы получили, если строка, сплитим ее до списка, и цифруем
        c = a.split()
        c = [int(n) for n in c]
    else:
        c = a  # если нет, то нет

    check = False
    value = int(value)
    low = int(low)
    high = int(high)
    mid = int(mid)

    if c[mid] == value:
        check = True

    elif value > c[mid]:

        low = mid

    elif value < c[mid]:

        high = mid

    mid = ((low + high) // 2)
    if check is False:
        bin_rec_find(value, low, high, mid, c)

    return mid, check


def func_convert_dec_in_bin(n, s):
    """Функция перевода числа из десятичного в двоичное. n-само число, s- строка с результатами функции для рекурсии"""

    n = int(n)
    s += f'{n - 2 * (n // 2)}'
    temp = n // 2

    if n == 1:

        s += str(temp)
        s = s[::-1]

        return s
    else:
        return func_convert_dec_in_bin(temp, s)


def func_prime_number(n):
    """Функция проверки на то простое ли число. n - число для проверки"""
    check = False

    if n % 2 == 0:  # Проверяем деление на 2(если делится число не простое)
        check = True
    else:
        for i in range(3, int(n ** 0.5) + 1, 2):
            # Делаем цикл от 3 (т.к 2 и 1 -очевидно исключаются,
            # и проверяем до корня из числа (ибо выше не имеет смысла) плюс только нечетные (ибо четные нет смысла)

            if n % i == 0:
                check = True

    return check


def func_nod(x, y):
    """Функция определения Наименьшего Общего Делителя (НОД), х, y - числа для поиска"""
    if y == 0:  # делим каждое число
        return x  # return x
    else:
        return func_nod(y, x % y)


def func_encryption(enc_str, key, lang, type):
    """Функция шифрования и дешифрования по методу Цезаря.enc_str -
    текст для шифрования,key -ключ, lang- язык текста """
    dictionary = dictionary_upper = ''

    if lang == 'Русский':
        dictionary, dictionary_upper = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    elif lang == 'Английский':
        dictionary, dictionary_upper = "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result_str, temp_dict = [], ""

    for i in range(len(enc_str)):

        if enc_str[i] in dictionary:  # Проверяем нижний регистр
            temp_dict = dictionary

        elif enc_str[i] in dictionary_upper:  # Проверяем верхний регистр
            temp_dict = dictionary_upper

        else:
            result_str.append(enc_str[i])  # Если там нет, значит это или спец знак или цифра

        if enc_str[i] in temp_dict:
            # Цикл перебора азбуки
            for j in range(len(temp_dict)):
                # Если порядковый номер буквы + ключ находятся  в диапазоне от 0 до конца словаря
                # и если буква из текста совпадает с буквой из азбуки, то:
                if 0 <= j + key < len(temp_dict) and enc_str[i] == temp_dict[j]:
                    # В результат добавляется буква со сдвигом key (зашифрованная буква)
                    result_str.append(temp_dict[j + key])
                    break
                # Если порядковый номер буквы + ключ выходит из диапазона азбуки, превышая его
                # и если буква из текста совпадает с буквой из азбуки, то:
                elif j + key >= len(temp_dict) and enc_str[i] == temp_dict[j]:
                    # В результат добавляется буква со сдвигом key,
                    # при этом преводя порядковый номер буквы к диапазону азбуки (зашифрованая буква)
                    result_str.append(temp_dict[((j + key) % (len(temp_dict) - 1)) - 1])
                    break
                # Если порядковый номер буквы + ключ выходит из диапазона азбуки, недотягивает до него
                # и если буква из текста совпадает с буквой из азбуки, то:
                elif j + key < 0 and enc_str[i] == temp_dict[j]:
                    # В результат добавляется буква со сдвигом key,
                    # при этом приводя порядковый номер буквы к диапазону азбуки (зашифрованная буква)
                    result_str.append(temp_dict[(j + key) % len(temp_dict)])
                    break
    if type == 'caesar':
        result_str = ' '.join(result_str)
        result_str = result_str.replace(' ', '')

    return result_str


def func_encrypted_vishener(enc_str, key, lang):
    """Функция шифрования и дешифрования по методу Вишенера.enc_str -
        текст для шифрования, key -ключ, lang- язык текста """

    dictionary, new_dictionary = '', ''
    enc_str = enc_str.upper()
    key = key.upper()
    massive = []
    temp_str = ''

    if lang == 'Русский':
        dictionary = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        massive = [func_encryption(dictionary, i, lang, 'vishener') for i in range(len(dictionary))]
        print('')
    elif lang == 'Английский':
        dictionary = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        massive = [func_encryption(dictionary, i, lang, 'vishener') for i in range(len(dictionary))]

    for i in range(len(enc_str)):

        try:
            temp_index_x = dictionary.index(enc_str[i])
            temp_index_y = dictionary.index(key[i])
            temp_str += massive[temp_index_x][temp_index_y]
        except ValueError:  # Перехват ошибки (означает что в тексте какой-то символ или пробел):
            temp_str += enc_str[i]

    return temp_str


def func_decrypted_vishener(enc_str, key, lang):
    """Функция шифрования и дешифрования по методу Вишенера.enc_str -
        текст для шифрования, key -ключ, lang- язык текста """

    dictionary, temp_str_mass = '', list
    enc_str = enc_str.upper()
    key = key.upper()
    massive = []
    temp_str, temp_str_mass = '', ''

    if lang == 'Русский':
        dictionary = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        massive = [func_encryption(dictionary, i, lang, 'vishener') for i in range(len(dictionary))]
        print('')
    elif lang == 'Английский':
        dictionary = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        massive = [func_encryption(dictionary, i, lang, 'vishener') for i in range(len(dictionary))]
    temp_str_mass = func_encryption(dictionary, 0, lang, 'vishener')

    for i in range(len(key)):

        try:
            temp_index_y = dictionary.index(key[i])
            for j in range(len(temp_str_mass)):
                if massive[j][temp_index_y] == enc_str[i]:

                    temp_str += temp_str_mass[j]
                    break
                elif massive[j][temp_index_y] != enc_str[i] and j == 32:
                    temp_str += enc_str[i]
        except ValueError:  # Перехват ошибки (означает что в тексте какой-то символ или пробел):
            temp_str += enc_str[i]

    return temp_str


def digit_func_count(temp_str):
    """Функция фильтровки списка и выдача цифровых элементов в виде строк. temp_str - список данных.
     Возвращает отфильтрованную строку result_str"""

    list_numbers = temp_str.split(sep=',')

    out_filter_list_numbers = list(filter(lambda s: s.isdigit() is True or s.lstrip("-").isdigit() is True,
                                          list_numbers))

    # Сначала поэлементно цифруем, чтобы выйти на условие задачи
    result_str = list(map(int, out_filter_list_numbers))
    result_str = list(map(str, result_str))  # Теперь переводим поэлементно в строку

    return result_str


def digit_null_count(temp_str):
    """Функция фильтровки списка и выдача цифровых элементов >0 в виде строк . temp_str - список данных.
     Возвращает отфильтрованную строку result_str"""

    list_numbers = temp_str.split(sep=',')

    out_filter_list_numbers = list(
        filter(lambda s: s.isdigit() is True, list_numbers))  # Доп проверку на отрицат не делаем ибо "-" символ

    # Сначала поэлементно цифруем, чтобы выйти на условие задачи
    result_str = list(map(int, out_filter_list_numbers))
    result_str = list(map(str, result_str))  # Теперь переводим поэлементно в строку

    return result_str


def str_count(temp_str):
    """Функция фильтровки списка и выдача строковых элементов являющихся палиндромом. temp_str - список данных.
     Возвращает отфильтрованную строку result_str"""

    list_numbers = temp_str.split(sep=',')

    # Проверяем на полином (т.е слово наоборот) и проверяем чтобы это была не 1 буква (ибо она
    # тоже подойдет под условие)
    out_filter_list_numbers = list(filter(lambda s: (s.isdigit() is False or s.lstrip("-").isdigit()
                                                     is False) and s == s[::-1] and len(s) > 1, list_numbers))

    if len(out_filter_list_numbers) == 0:
        out_filter_list_numbers = ''

    return out_filter_list_numbers


def value_check_func(a):
    check = False
    if isinstance(a, int) is True or  isinstance(a, float) is True:
        check = True
        return a, check

    elif a.isdigit() is True or a.lstrip("-").isdigit() is True:
        check = True
        try:
            a = int(a)
        except ValueError:
            a = float(a)

        return a, check

    elif isinstance(a, str):
        check = False

    return a, check
