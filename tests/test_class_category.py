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

    assert category_1.product_count == 19
    assert category_2.product_count == 19
    assert category_3.product_count == 19
feature/homework_14_2

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
=======
develop
