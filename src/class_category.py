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
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        all_products = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {all_products} шт."

    def add_product(self, product: Product):
        """метод для добавления товаров"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += product.quantity
        else:
            raise TypeError

    @property
    def products(self):
        """геттер для вывода списка товаров"""
        products = ""
        for product in self.__products:
            products += f"{str(product)}\n"
        return products
