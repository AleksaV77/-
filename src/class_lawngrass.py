from src.class_product import Product

class LawnGrass(Product):
    """Содержит данные о товаре "газонная трава": название, описание, цена, количество в наличии,
     страна-производитель, срок прорастания, цвет"""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            return self.quantity * self.price + other.quantity * other.price
        raise TypeError
