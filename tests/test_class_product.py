from src.class_product import Product


def test_product_init(product_1, product_2):
    assert product_1.name == "Xiaomi Redmi Note 11"
    assert product_1.description == "1024GB, Синий"
    assert product_1.price == 31000.0
    assert product_1.quantity == 14

    assert product_2.name == "Xiaomi Redmi Note 10"
    assert product_2.description == ""
    assert product_2.price == 15000.0
    assert product_2.quantity == 5
feature/homework_14_2

def test_new_product(product_dict):
    product_4 = Product.new_product(product_dict)
    assert product_4.name == "Samsung Galaxy S23 Ultra"
    assert product_4.description == "256GB, Серый цвет, 200MP камера"
    assert product_4.price == 170000.0
    assert product_4.quantity == 3

def test_price_str(product_1):
    assert str(product_1.price) == "31000.0"

def test_price_user(capsys, product_3):
    product_3.price = -50.00
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    product_3.price = -50.00
    assert product_3.price == -50.00

def test_price_setter(product_2):
    product_2.price = 15000.0
    assert product_2.price == 15000.0
=======
 develop
