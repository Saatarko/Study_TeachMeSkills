""" Николаю требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник.
Для этого он решил создать класс TriangleChecker, принимающий только положительные числа.
С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
– Ура, можно построить треугольник!;
– С отрицательными числами ничего не выйдет!;
– Нужно вводить только числа!;
– Жаль, но из этого треугольник не сделать."""

from dataclasses import dataclass  # Добавляем бибилотеку датаклассов


@dataclass
class TriangleChecker:    # Добавляем класс и его атрибуты (потенциальные стороны треугольника)
    side_a: int
    side_b: int
    side_c: int

    def is_triangle(self):  # метод расчета можно ли из указанных отрезов сделать треугольник

        try:
            # создаем список для удобства сортировки

            _list = sorted([int(self.side_a), int(self.side_b), int(self.side_c)])
            if _list[0] < 0 or _list[1] < 0 or _list[2] < 0:    # проверка на отрицательное число
                print('C отрицательными числами ничего не выйдет!')

            # проверка на возможность создания теругольника (две стороны должны быть больше третьей)

            elif (_list[0] + _list[1]) > _list[2]:
                print('Ура, можно построить треугольник!')
            else:
                print('Жаль, но из этого треугольник не сделать.')
        except ValueError:     # ловим ошибку если ввели строку
            print('Нужно вводить только числа!')


triangle = TriangleChecker(5, 6, 10)
triangle.is_triangle()
print(f'Из {triangle} \n')

triangle = TriangleChecker(5, 6, 12)
triangle.is_triangle()
print(f'Из {triangle} \n')

triangle = TriangleChecker('3', '4', '5')
triangle.is_triangle()
print(f'Из {triangle} \n')

triangle = TriangleChecker('3', '4', 'sdfg')
triangle.is_triangle()
print(f'Из {triangle} \n')

triangle = TriangleChecker('3', '4', -12)
triangle.is_triangle()
print(f'Из {triangle} \n')