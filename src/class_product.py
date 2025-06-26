class Product:
    """Содержит данные о товаре: название, описание, цену, количество в наличии"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
feature/homework_14_2
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_dict):
        """Взвращает созданный объект класса Product"""
        name = product_dict["name"]
        description = product_dict["description"]
        price = product_dict["price"]
        quantity = product_dict["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            user = input("введите 'y' если ходите понизить цену или 'n' для отмены: ")
            if user == "y":
                print("цена снижена")
            else:
                print('Цена осталась прежней')
        else:
            print('Цена осталась прежней')
=======
        self.price = price
        self.quantity = quantity

develop
