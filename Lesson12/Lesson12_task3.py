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
class Bus:                  # добавляем нужные атрибуты класcа
    _speed: int
    max_seats: int
    max_speed: int
    pass_last_name: list
    free_seats: bool = field(init=False)  # эти два атрибута инициируются позже (зачем нужен free_seats непонятно)
    dict_seats: dict = field(init=False)

    def __post_init__(self):
        temp = [i for i in range(1, len(self.pass_last_name) + 1)]   # создаем список пустых мест
        self.dict_seats = dict(zip(self.pass_last_name, temp))     # из двух списков(мест и фамилий) делаем словарь
        try:
            if len(self.pass_last_name) <= self.max_seats:   # делаем проверку для флага пустых мест
                self.free_seats = True
            else:

                self.free_seats = False
                raise TypeError
        except TypeError('Пассажиров больше чем мест. Автобус никуда не поедет'):
            print('Пассажиров больше чем мест. Автобус никуда не поедет')

    @property  # делаем метод для проверки значения скорости после изменения.Это геттер
    def name_list(self):
        return self.pass_last_name

    @name_list.setter  # делаем метод для проверки значения скорости после изменения.Это сеттер
    def name_list(self, value):
        if len(value) > self.max_seats:    # проверяем если фамилий (т,е пассажиров) больше мест, то надо высаживать
            zero_people = len(value) - self.max_seats  # кол-во лишних человеков
            temp = value[-zero_people:]   # список фамилий минус лишние люди
            print(f'Всем людям места не хватило, остались {zero_people} человек(а) - {temp}')
            self.pass_last_name = value[0: -zero_people]  # сохраняем новый список фамилий в атрибут класса
        temp_list = list(self.dict_seats.values())    # берем список мест из словаря ((Т.е тех кто заняты)
        list_number = [i for i in range(1, len(self.pass_last_name) + 1)]   # формируем общий список мест в автобусе

        # отсеиваем по обоим спискам получая список не занятых мест
        temp_list = [x for x in list_number if x not in temp_list]
        temp_key = list(self.dict_seats.keys())           # берем список фамилий из словаря ((Т.е тех уже сидит)
        name = [x for x in self.pass_last_name if x not in temp_key]    # фильтруем и получаем тех кто только вошел
        temp_list = temp_list[0:len(name)]  # сокращаем список пустых мест по кол-ву вошедших
        temp_dict = dict(zip(name, temp_list))   # создаем новый словарь из списка пустых мест и вошедших
        self.dict_seats = {**self.dict_seats, **temp_dict}    # соединяем новый словарь и словарь уже сидящих
        if len(self.pass_last_name) == self.max_seats:   # проверяем на остаток пустых мест
            self.free_seats = False

    def change_pass_status(self, in_out, name: list):   # метод входа и выхода людей
        if in_out == 'вход':
            self.name_list += name    # люди вошли (вызываем геттер)
        elif in_out == 'выход':
            try:
                # люди вышли.проверяем есть ли выходные фамилии вообще в списке

                if set(name).issubset(self.pass_last_name) is True:

                    # выкидываем тх кто вышел
                    self.pass_last_name = [x for x in self.pass_last_name if x not in name]
                    for i in name:
                        del self.dict_seats[i]
                        self.free_seats = True

                else:
                    raise TypeError   # ошибка если указанной фамилии в списке нет( указанного чела нет в автобусе)
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


bus = Bus(60, 5, 120, ['денис сергеев', 'антуан попов', 'фекла копытная'])   # создаем экземпляр класса
bus.change_speed('увеличить', 20)  # проверка метода изменения скорости
print(f'{bus}\n')
bus.change_speed('увеличить', 150)
print(f'{bus}\n')
bus.change_speed('уменьшить', 180)
print(f'{bus}\n')

bus.change_pass_status('вход', ['александр пушкин', 'сергей есенин'])   # люди вошли. проверяем
print(f'{bus.pass_last_name}')
print(f'{bus.dict_seats}\n')

bus.change_pass_status('выход', ['фекла копытная', 'антуан попов'])  # люди вышли. проверяем

print(f'{bus.pass_last_name}')
print(f'{bus.dict_seats}\n')

bus.change_pass_status('выход', ['свинорыл'])   # выход человека которого нет в автобусе

bus.change_pass_status('вход', ['федор достоевский', 'михаил булгаков'])
print(f'{bus.pass_last_name}')
print(f'{bus.dict_seats}\n')

# люди вошли больше чем мест. проверяем

bus.change_pass_status('вход', ['фекла копытная', 'антуан попов', 'александр блок', 'эрих мария ремарк'])

print(f'{bus.pass_last_name}')
print(f'{bus.dict_seats}\n')
