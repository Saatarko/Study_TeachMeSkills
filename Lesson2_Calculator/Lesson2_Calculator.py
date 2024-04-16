import keyboard

operation_check = False     # Явное задание основных счетчиков (выбор операции)
failed_counter = 0       # счетчик ошибок


def check_function(input_value, check_for_segment):     # Функция проверки введенных значений

    check = False
    while check is False:                  # Пока проверка не пройдена цикл работает

        if switch == '4' and check_for_segment == 'second_number' and input_value == '0':  # Проверка на 0
            check_digital_or_float_or_str = False

        elif input_value.isdigit() is True:      # Проверка на то что введенные данные - целое число
            check_digital_or_float_or_str = True
            check = True
            input_value = int(input_value)                 # Перевод строки в число

        else:
            try:                                             # Проверка на то что введенные данные число в пл. точкой
                input_value = float(input_value)
                check_digital_or_float_or_str = True
                check = True
            except ValueError:                              # Перехват ошибки (если данные не числовые)
                check_digital_or_float_or_str = False

        if check_digital_or_float_or_str is False:           # Вывод - перед нами символы

            if input_value == '0':
                print('Делить на 0 нельзя!')
            else:
                print('Число!!! Это набор символов образованный цифрами от 0 до 9)')
            input_value = input("Введите число заново")

    return input_value           # Возврат оцифрованного значения(целое или плавающее)


def enter_numbers():                      # Функция запроса на ввод данных с клавиатуры

    a = input("Введите первое число")
    a = check_function(a, 'first_number')                 # Вызов функции проверки
    b = input("Введите второе число")
    b = check_function(b, 'second_number')

    return a, b                           # Возвращаем оцифрованные данные после ф-ции проверки


def sum_numbers(a, b):                   # Функция сложения

    res = a + b
    return res


def subtraction_numbers(a, b):          # Функция вычитания

    res = a - b
    return res


def multiplication_numbers(a, b):       # Функция умножения

    res = a * b
    return res


def segmentation_numbers(a, b):     # Функция деления
    res = a / b

    return res


def repeat_operation():           # Функция запроса на повторный вызов меню

    check = False
    end_switch = input("Хотите ли Вы продолжить работать с калькулятором. 1.Да, 2. Нет?")

    while check is False:             # Проверка на введенное значение

        if end_switch == '1' or end_switch.lower() == 'да':
            check = False
            return check, 0
        elif end_switch == '2' or end_switch.lower() == 'нет':
            check = True
            return check, 0
        else:
            print('Надо ввести  цифры 1 или 2. Или слова, да или нет', '\n')
            end_switch = input("Введите  заново")


def console_clear():         # Функция очистки экрана
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


while operation_check is False:         # Основной цикл программы

    if failed_counter == 0:             # Если счетчик ошибок 0 - то чистим консоль и выводим наше меню
        console_clear()
        print('Добро пожаловать в калькулятор в.0.00001324', '\n')

        print('Выберите операцию для вычисления!. Введя ее порядковый номер или написав название!', '\n')
        print('1. Сложение')
        print('2. Вычитание')
        print('3. Умножение')
        print('4. Деление', '\n')

    switch = input("Выберите операцию")                  # Запрос на выбор раздела меню

    if switch == '1' or switch.lower() == 'сложение':     # Проверяем введенные значения и вызываем соот. функции
        print('Вы выбрали операцию сложения', '\n')
        first_number, second_number = enter_numbers()
        result = sum_numbers(first_number, second_number)
        print('Результат сложения:', result, '\n')
        operation_check, failed_counter = repeat_operation()

    elif switch == '2' or switch.lower() == 'вычитание':
        print('Вы выбрали операцию вычитания', '\n')
        first_number, second_number = enter_numbers()
        result = subtraction_numbers(first_number, second_number)
        print('Результат вычитания:', result, '\n')
        operation_check, failed_counter = repeat_operation()

    elif switch == '3' or switch.lower() == 'умножение':
        print('Вы выбрали операцию умножения', '\n')
        first_number, second_number = enter_numbers()
        result = multiplication_numbers(first_number, second_number)
        print('Результат умножения:', result, '\n')
        operation_check, failed_counter = repeat_operation()

    elif switch == '4' or switch.lower() == 'деление':
        print('Вы выбрали операцию деления', '\n')
        first_number, second_number = enter_numbers()
        result = segmentation_numbers(first_number, second_number)
        print('Результат деления:', result, '\n')
        operation_check, failed_counter = repeat_operation()

    else:
        failed_counter += 1    # если ввели некорректный пункт меню наращиваем счетчик ошибок

        if failed_counter >= 5:  # если счетчик сильно большой - то ругаемся на пользователя
            print("""Да сколько можно. Белым по черному написано - выберите операцию введя
             ее порядковый номер или написав название. Т.е для выбора например операции сложения
             необходимо ввести цифру 1 или слово сложение. Нажмите любую клавишу для продолжения!""")
            keyboard.wait()
            failed_counter = 0  # обнуляем счетчик лоя последующей очистки консоли и повторного вывода меню

        else:
            print('Перечитайте условия выбора операции')
