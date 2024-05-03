"""Разработать класс SuperStr, который наследует
функциональность стандартного типа str и содержит два
новых метода:
• Метод is_repeatance(s), который принимает некоторую строку
и возвращает True или False в зависимости от того, может ли
текущая строка быть получена целым количеством повторов
строки s. Считать, что пустая строка не содержит повторов
• Метод is_palindrom(), который возвращает True или False в
зависимости от того, является ли строка палиндромом вне
зависимости от регистра. Пустую строку считать
палиндромом."""


class SuperStr(str):  # Создание класса SuperStr, наследованного от str

    def is_repeatance(self, s):   # метод проверки строки на повторение
        if not isinstance(s, str):
            return False
        n = len(self) // (len(s) or 1)
        return self == n * s

    def is_palindrome(self):   # метод проверки на палиндром
        s = self.lower()
        return s == s[::-1]


temp_str = SuperStr('567567567567')  # создаем элемент класса
print(temp_str)

temp2 = temp_str.is_repeatance('567')  # проверяем на повтор
print(f'Повторы в строке {temp2}')

temp3 = temp_str.is_repeatance('978') # проверяем на повтор
print(f'Повторы в строке {temp3}')

sup2 = SuperStr('abddba')
temp2 = sup2.is_palindrome()  # проверяем на палиндром

print(f'Является ли {sup2} палиндромом - {temp2}')

sup3 = SuperStr('abd1235')
temp3 = sup3.is_palindrome()   # проверяем на палиндром
print(f'Является ли {sup3} палиндромом - {temp3}')
