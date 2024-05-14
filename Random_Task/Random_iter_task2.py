""" Инструкция yield позволяет создавать генераторы. В отличие от объявления return в функции, где возвращается
один объект, yield при каждом вызове функции генерирует новый объект Фактически это дает возможность использовать
генераторы в циклах. Самая важная причина применения такой инструкции - экономия памяти, когда не требуется сохранять
 всю последовательность, а можно получать ее элементы по одному.
Ученик написал генератор show_letters(some_str), выводящий все символы строки на печать, но только в том случае,
если они являются буквами (остальные игнорируются). Сократите код функции.

Код – IDE
---
def show_letters(some_str):
____clean_str = ''.join([letter for letter in some_str if letter.isalpha()])
____for symbol in clean_str:
________yield symbol"""


def show_letters(some_str):
    yield from ''.join([letter for letter in some_str if letter.isalpha()])


random_str = show_letters('A!rarterghdrgh!sdf09_w')
print(next(random_str))
print(next(random_str))
print(next(random_str))
