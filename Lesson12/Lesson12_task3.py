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
        temp = [i for i in range(0, len(self.pass_last_name))]
        self.dict_seats = dict(zip(self.pass_last_name, temp))

        if len(self.pass_last_name) <= self.max_seats:
            self.free_seats = True
        else:
            raise 'Пассажиров больше чем мест. Автобус никуда не поедет'

    @property  # делаем метод для проверки значения скорости после изменения.Это геттер
    def name_list(self):
        return self.pass_last_name

    @name_list.setter  # делаем метод для проверки значения скорости после изменения.Это сеттер
    def name_list(self, value):
        if len(value) > self.max_seats:
            zero_people = len(value) - self.max_seats
            temp = value[-zero_people:]
            print(f'Всем людям места не хватило, остались {zero_people} человек(а) - {temp}')
            self.pass_last_name = value[0: -zero_people]
        temp_list = self.dict_seats.values()
        temp_list = [x for x in range(0,self.max_seats) if x not in temp_list]

    # def __isub__(self, other):
    #     self.pass_last_name = [x for x in self.pass_last_name if x not in other]

    def change_pass_status(self, in_out, name: list):
        if in_out == 'вход':
            self.name_list += name
        elif in_out == 'выход':
            try:
                if set(name).issubset(self.pass_last_name) is True:
                    self.pass_last_name = [x for x in self.pass_last_name if x not in name]

                else:
                    raise TypeError
            except TypeError:
                print(f'Не все указанные в списке {name} есть в автобусе')

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


# bus = Bus(60, 4, 120, ['денис сергеев', 'антуан попов', 'фекла копытная'])
bus = Bus(60, 5, 120, ['денис сергеев', 'антуан попов', 'фекла копытная'])
bus.change_speed('увеличить', 20)  # проверка метода изменения скорости
print(f'{bus}\n')
bus.change_speed('увеличить', 150)
print(f'{bus}\n')
bus.change_speed('уменьшить', 180)
print(f'{bus}\n')

bus.change_pass_status('вход', ['александр пушкин', 'сергей есенин'])
print(f'{bus.pass_last_name}\n')

bus.change_pass_status('выход', ['фекла копытная', 'антуан попов'])
print(f'{bus.pass_last_name}\n')

bus.change_pass_status('выход', ['свинорыл'])
