"""3. Класс «Автобус».
Класс содержит свойства:
● Скорость
● Максимальное количество посадочных мест
● Максимальная скорость
● Список фамилий пассажиров
● Флаг наличия свободных мест
● Словарь мест в автобусе
Методы:
● Посадка и высадка одного или нескольких пассажиров
● Увеличение и уменьшение скорости на заданное значение
● Операции in, += и -= (посадка и высадка пассажира по
фамилии)"""

from dataclasses import dataclass, field  # добавляем библиотеку dataclass


@dataclass
class Bus:
    _speed: int
    max_seats: int
    max_speed: int
    pass_last_name: list
    free_seats: bool = field(init=False)
    dict_seats: dict = field(init=False)

    def __post_init__(self):
        # temp = [i for i in range(0, len(self.pass_last_name))]
        #
        # self.dict_seats = {key: temp for key in self.pass_last_name}

        self.dict_seats = dict.fromkeys(range(len(self.pass_last_name)), self.pass_last_name)  # нао думиать
        if len(self.pass_last_name) <= self.max_seats:
            self.free_seats = True
        else:
            raise 'Пассажиров больше чем мест. Автобус никуда не поедет'

    @property  # делаем метод для проверки значения скорости после изменения.Это геттер
    def name_list(self):
        return self.pass_last_name

    @name_list.setter  # делаем метод для проверки значения скорости после изменения.Это сеттер
    def name_list(self, value):
        if len(self.pass_last_name + value) > self.max_seats:
            zero_people = self.pass_last_name + value - self.max_seats
            print(f'Всем людям места не хватило, остались {zero_people}')
            value = value[0, -zero_people]
        else:
            self.pass_last_name += value
        if set(value).issubset(self.pass_last_name) is True:
            self.pass_last_name -= value
        else:
            raise 'Несоответствущий список пассажиров или мест'

    def change_pass_status(self, in_out, name: list):
        if in_out == 'вход':
            self.pass_last_name += name
        elif in_out == 'выход':
            result = [x for x in name if x not in self.pass_last_name]

    def get_in(self):
        pass

    def get_out(self):
        pass

    @property  # делаем метод для проверки значения скорости после изменения.Это геттер
    def speed(self):
        return self._speed

    @speed.setter  # делаем метод для проверки значения скорости после изменения.Это сеттер
    def speed(self, value):
        if value <= 0:
            self._speed = 0
        elif value >= self.max_speed:
            self._speed = self.max_speed
        else:
            self._speed = value

    def change_speed(self, vector, value):  # метод изменения скорости
        if vector == 'увеличить':
            self.speed += value
        elif vector == 'уменьшить':
            self.speed -= value


bus = Bus(60, 50, 120, ['денис сергеев', 'антуан попов', 'фекла копытная'])
bus.change_speed('увеличить', 20)  # проверка метода изменения скорости
print(f'{bus}\n')
bus.change_speed('увеличить', 150)
print(f'{bus}\n')
bus.change_speed('уменьшить', 180)
print(f'{bus}\n')