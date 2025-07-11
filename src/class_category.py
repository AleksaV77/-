from itertools import product

from unicodedata import category

from src.class_product import Product
from src.exception import ZeroQuantity


class Category:
    """Содержит данные о товаре: название, описание, список товаров категории"""
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        all_products = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {all_products} шт."

    def add_product(self, product: Product):
        """метод для добавления товаров"""
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroQuantity("Нельзя добавить товар с нулевым количеством")
            except ZeroQuantity as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += product.quantity
                print("Товар добавлен")
            finally:
                print("Обработка добавления товара завершена")
        else:
            raise TypeError

    @property
    def products(self):
        """геттер для вывода списка товаров"""
        products = ""
        for product in self.__products:
            products += f"{str(product)}\n"
        return products

    @property
    def category_in_products(self):
        return self.__products

    def average_price_tag(self):
        """Подсчитывает средний ценник всех товаров"""
        try:
            return sum([product.price for product in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0
