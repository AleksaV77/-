class Product:
    """Содержит данные о товаре: название, описание, цену, количество в наличии"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

