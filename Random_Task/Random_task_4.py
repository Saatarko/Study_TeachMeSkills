""" Строки в Питоне сравниваются на основании значений символов. Т.е. если мы захотим выяснить, что больше:
Apple или Яблоко, – то Яблоко окажется бОльшим. А все потому, что английская буква A имеет значение 65
 (берется из таблицы кодировки), а русская буква Я – 1071 (с помощью функции ord() это можно выяснить).
 Такое положение дел не устроило Анну. Она считает, что строки нужно сравнивать по количеству входящих в них символов.
Для этого девушка создала класс RealString и реализовала озвученный инструментарий. Сравнивать между собой можно как
 объекты класса, так и обычные строки с экземплярами класса RealString. К слову, Анне понадобилось только 3 метода
 внутри класса (включая __init__()) для воплощения задуманного."""

from dataclasses import dataclass  # импортируем библиотеку датаклассов


@dataclass
class RealString:    # создаем класс
    _string: str

    def count(self, other):    # создаем метод сравнения строк
        if not isinstance(other, RealString):  # если передаваемая строка не атрибут класса присваиваем ее в RealString
            other = RealString(other)
        if len(self._string) < len(other._string):    # длинны строк
            print(f'Строка "{self._string}" короче строки "{other._string}"')
        elif len(self._string) == len(other._string):
            print(f'Строка "{self._string}" равна строке "{other._string}"')
        else:
            print(f'Строка "{self._string}" длиннее строки"{other._string}"')


str1 = RealString('Молоко')
str2 = RealString('Абрикосы растут')
str3 = 'Золото'
print(f'\n')
RealString.count(str1, str3)
print(f'\n')
RealString.count(str1, str2)


