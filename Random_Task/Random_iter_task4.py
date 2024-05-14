"""Реализуйте итератор колоды карт (52 штуки) CardDeck. Каждая карта представлена в виде строки типа 2 Пик.
При вызове функции next() будет представлена следующая карта. По окончании перебора всех элементов возникнет
ошибка StopIteration."""


class CardDeck:  # Создаем класс с атрибутами
    length = 52
    index = 0
    __SUITS = ['Пик', 'Бубей', 'Червей', 'Крестей']
    __RANKS = [*range(2, 11), 'Валет', 'Дама', 'Король', 'Туз']

    def __len__(self):
        return self.length

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.length:
            raise StopIteration
        else:
            suit = self.__SUITS[self.index // len(self.__RANKS)]
            rank = self.__RANKS[self.index % len(self.__RANKS)]
            self.index += 1
            return f'{rank} {suit}'


deck = CardDeck()
while True:
    print(next(deck))
