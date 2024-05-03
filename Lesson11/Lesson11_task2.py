"""Напишите программу с классом Math. При инициализации
атрибутов нет. Реализовать методы addition, subtraction,
multiplication и division. При передаче в методы двух числовых
параметров нужно производить с параметрами
соответствующие действия и печатать ответ."""

class Math:   # Создаем класс Math

    @staticmethod    # Создаем статические методы (т.к им атрибуты класса не нужны они просто принимают значение)
    def addition(a=0, b=0):   # Метод суммирования

        return int(a) + int(b)

    @staticmethod
    def subtraction(a=0, b=0):   # Метод вычитания
        return int(a) - int(b)

    @staticmethod
    def multiplication(a=0, b=0):  # Метод умножения
        return int(a) * int(b)

    @staticmethod
    def division(a=0, b=1):  # Метод деления
        try:
            if b == 0:
                raise ZeroDivisionError
        except ZeroDivisionError:
            print('Делить на 0 нельзя')
        else:
            return int(a) / int(b)


print(Math.addition(5, 4))   # вызываем методы с какими-то атрибутами и смотрим результат
print(Math.subtraction(5, 4))
print(Math.multiplication(5, 4))
print(Math.division(5, 4))
