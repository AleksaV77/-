import pytest
from pyexpat.errors import messages

from src.class_category import Category
from src.class_product import Product

def test_category_init(category_1, category_2, category_3):
    assert category_1.name == "Смартфоны"
    assert category_2.name == "Телевизоры"
    assert category_3.name == "Ноутбуки"

    assert category_1.description == "Смартфоны"
    assert category_2.description == "Современный телевизор"
    assert category_3.description == "Ноутбуки, планшеты, компьютеры"

    assert category_1.category_count == 3
    assert category_2.category_count == 3
    assert category_3.category_count == 3

    assert category_1.product_count == 5
    assert category_2.product_count == 5
    assert category_3.product_count == 5


def test_products(category_1, category_2):
    assert (category_1.products ==
        'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5\n'
        'Iphone 15, 210000.0 руб. Остаток: 8\n'
    )
    assert (category_2.products ==
        'SBER SDX-xxF2139, 140000.0 руб. Остаток: 3\n'
        'Xiaomi TV A 32, 250000.0 руб. Остаток: 2\n'
        'QD-Mini LED TCL 85X955, 299000.0 руб. Остаток: 1\n'
    )

def test_add_product(category_1, category_3, add_product_1, add_product_2, product_1, product_2):
    category_1.add_product(product_1)
    assert category_1.products == add_product_1
    category_3.add_product(product_2)
    assert category_3.products == add_product_2

def test_category_str(category_2):
    assert str(category_2) == "Телевизоры, количество продуктов: 6 шт."

def test_add_product_error(category_1):
    with pytest.raises(TypeError):
        category_1.add_product(1)

def test_average_price(category_1, user_without_quantity):
    assert category_1.average_price_tag() == 195000.0
    assert user_without_quantity.average_price_tag() == 0

def test_exception(capsys, category_1):
    assert len(category_1.category_in_products) == 2

    category_1.add_product(Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 0))
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Нельзя добавить товар с нулевым количеством"
    assert message.out.strip().split("\n")[-1] == "Обработка добавления товара завершена"

    category_1.add_product(Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 15))
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Товар добавлен"
    assert message.out.strip().split("\n")[-1] == "Обработка добавления товара завершена"
