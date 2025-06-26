from src.class_product import Product


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
feature/homework_14_2
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += sum(product.quantity for product in products)

    def add_product(self, product: Product):
        """метод для добавления товаров"""
        self.__products.append(product)
        Category.product_count += product.quantity

    @property
    def products(self):
        """геттер для вывода списка товаров"""
        products = ""
        for product in self.__products:
            products += f"{product.name}, {product.price} руб. Остаток: {product.quantity}\n"
        return products
=======
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += sum(product.quantity for product in products)

develop
