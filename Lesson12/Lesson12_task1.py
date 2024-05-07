from dataclasses import dataclass, field, asdict
from typing import List
import operator

product = []

@dataclass
class Product:
    __name: str
    __store_name: str
    __price: int

    def setname(self, name):
        self.__name = name

    def getname(self):
        return self.__name

    name = property(getname, setname)

    def set_store_name(self, store_name):
        self.__store_name = store_name

    def get_store_name(self):
        return self.__store_name

    store_name = property(get_store_name, set_store_name)

    def setprice(self, price):
        self.__price = price

    def getprice(self):
        return self.__price

    price = property(getprice, setprice)



    def __repr__(self):
        return f'{self.name}  магазина {self.store_name} по цене {self.price}'


@dataclass(order=True)
class Store:
    __list: List[Product]
    # __list: List[Product] = field(default_factory=make_default_set)

    def setlist(self, temp_list):
        self.__list = temp_list

    def getlist(self):
        return self.__list

    list = property(getlist, setlist)


    def __repr__(self):
        temp = len(self.list)
        temp_list = [f'{self.list[i].name}  магазина {self.list[i].store_name} по цене {self.list[i].price}\n'
                     for i in range(temp)]
        set_str = 'На складе есть: ' + ' '.join(temp_list)
        return set_str

    def sorted(self, sort_field):
        if sort_field == 'name':
            print(f'Итог сортировки по имени: {sorted(self.__list, key=operator.attrgetter("name"))}')
        elif sort_field == 'store_name':
            print(f'Итог сортировки по названию магазина: {sorted(self.__list, key=operator.attrgetter("store_name"))}')
        elif sort_field == 'price':
            print(f'Итог сортировки по цене: {sorted(self.__list, key=operator.attrgetter("price"))}')

    def get_by_name(self):


product.append(Product('zrill', '21Vek', 500))
product.append(Product('Teapot', 'Electosila', 500))
product.append(Product('dildo', 'Sexshop', 150))
product.append(Product('pan', '21Vek', 26))

# my_store = Store([zrill, teapot, dildo, pan])

my_store = Store(product)

print(my_store.list[0])
print(my_store.list[1])
print(my_store.list[2])
print(f'{my_store.list[3]}\n')

# print(zrill)
# print(teapot)
# print(f'{dildo}\n')

print(my_store)

my_store.sorted('name')
my_store.sorted('store_name')
my_store.sorted('price')

