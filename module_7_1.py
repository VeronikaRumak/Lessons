from pprint import pprint

print()     # Отступ


# Необходимо реализовать 2 класса Product и Shop,
# с помощью которых будет производиться запись в файл с продуктами.

# Объекты класса Product будут создаваться следующим образом -

# Product('Potato', 50.0, 'Vagetables') и обладать следующими свойствами:
class Product:
    def __init__(self, name, weight, category):

        # Атрибут name - название продукта (строка).
        self.name = name

        # Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
        self.weight = weight

        # Атрибут category - категория товара (строка).
        self.category = category

    # Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'.
    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"
# Все данные в строке разделены запятой с пробелами.


# Объекты класса Shop будут создаваться следующим образом -

# Shop() и обладать следующими свойствами:
class Shop:
    # Инкапсулированный атрибут __file_name = 'products.txt'.
    def __init__(self):
        self.__file_name = 'products2.txt'

    # Метод get_products(self), который считывает всю информацию из файла __file_name,
    # закрывает его и возвращает единую строку со всеми товарами из файла __file_name.
    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return str(products)

    # Метод add(self, *products),
    # который принимает неограниченное количество объектов класса Product.
    def add(self, *products):
        file = open(self.__file_name, 'a')

        for product in products:
            # Добавляет в файл __file_name каждый продукт из products,
            # если его ещё нет в файле (по названию).
            if product not in products:
                file.write(product + '\n')

            # Если такой продукт уже есть, то не добавляет и выводит строку
            # 'Продукт <название> уже есть в магазине'.
            else:
                print(f"Продукт {product.name} уже есть в магазине")

        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())











