from tkinter import messagebox as mb
from datetime import datetime


def check_value(a, func_type):
    """Функция проверки значений на число type(a)- list, func_type - 'digit' или 'float'"""
    external_verification = False
    check = False

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
            s = datetime.strptime(d, '%d.%m.%Y')
            check = True
        except Exception:
            mb.showwarning("Предупреждение", "Формат даты не тот")
            check = False

    return check


def bin_rec_find(value, low, high, mid, a, real_mid):
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
    real_mid = int(real_mid)

    if c[mid] == value:
        check = True

    elif value > c[mid]:

        low = mid

    elif value < c[mid]:

        high = mid

    mid = ((low + high) // 2)
    if check is False:
        bin_rec_find(value, low, high, mid, c, real_mid)

    return mid, check


def func_convert_dec_in_bin(n, s):
    """Функция перевода числа из десятичного в двоичное"""

    global conv_str
    n = int(n)
    s += f'{n - 2 * (n // 2)}'
    temp = n // 2
    c = n - 2 * (n // 2)

    if n == 1:

        s += str(temp)
        conv_str = s[::-1]
    else:

        func_convert_dec_in_bin(temp, s)

    return conv_str


def func_prime_number(n):
    check = False

    if n % 2 == 0:           # Проверяем деление на 2(если делится число не простое)
        check = True
    else:
        for i in range(3, int(n**0.5)+1, 2):
            # Делаем цикл от 3 (т.к 2 и 1 -очевидно исключаются,
            # и проверяем до корня из числа (ибо выше не имеет смысла) плюс только нечетные (ибо четные нет смысла)

            if n % i == 0:
                check = True

    return check


def func_nod(x, y):
    if y == 0:  # делим каждое число
        return x  # return x
    else:
        return func_nod(y, x % y)
