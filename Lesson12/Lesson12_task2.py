"""ПчёлоСлон
Экземпляр класса инициализируется двумя целыми числами,
первое относится к пчеле, второе – к слону. Класс реализует
следующие методы:
● Fly() – возвращает True, если часть пчелы не меньше части
слона, иначе – False
● Trumpet() – если часть слона не меньше части пчелы,
возвращает строку “tu-tu-doo-doo”, иначе – “wzzzz”
● Eat(meal, value) – может принимать в meal только ”nectar” или
“grass”. Если съедает нектар, то value вычитается из части
слона, пчеле добавляется. Иначе – наоборот. Не может
увеличиваться больше 100 и уменьшаться меньше 0"""

from dataclasses import dataclass  # добавляем библиотеку dataclass


@dataclass          # добавляем класс BeeElephant как датакласс
class BeeElephant:
    bee_gen: int = 50      # делаем значения по умолчанию для генов
    elephant_gen: int = 50

    def fly(self):    # делаем метод fly
        if self.bee_gen >= 50:
            return True
        else:
            return False

    def trumpet(self):  # делаем метод trumpet
        if self.elephant_gen >= 50:
            return print('tu-tu-doo-doo')
        else:
            return print('wzzzz')

    @property         # делаем метод для проверки значения гена пчелы  после еды.Это геттер
    def bee(self):
        return self.bee_gen

    @bee.setter    # делаем метод для проверки значения гена пчелы после еды.Это сеттер
    def bee(self, value):
        if value <= 0:
            self.bee_gen = 0
        elif value >= 100:
            self.bee_gen = 100
        else:
            self.bee_gen = value

    @property     # делаем метод для проверки значения гена слона после еды.Это геттер
    def elephant(self):
        return self.elephant_gen

    @elephant.setter    # делаем метод для проверки значения гена слона после еды.Это сеттер
    def elephant(self, value):
        if value <= 0:
            self.elephant_gen = 0
        elif value >= 100:
            self.elephant_gen = 100
        else:
            self.elephant_gen = value

    def eat(self, meal, value):   # метод кормления
        if meal == 'nectar':
            self.bee += value
            self.elephant -= value
        elif meal == 'grass':
            self.bee -= value
            self.elephant += value


beeElephant = BeeElephant(50, 50)  # создание элемента класса

beeElephant.eat('nectar', 30)   # кормление и игра с генами и вывод на печать резульатата
print(beeElephant.fly())
beeElephant.trumpet()
print(beeElephant)
print('\n')

beeElephant.eat('grass', 60)
print(beeElephant.fly())
beeElephant.trumpet()
print(beeElephant)
print('\n')


beeElephant.eat('grass', 30)   # задание заведомо некорректных результатов
print(beeElephant)
print('\n')

beeElephant.eat('nectar', 110)    # задание заведомо некорректных результатов
print(beeElephant)
print('\n')
