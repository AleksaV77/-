def test_category_init(category_1, category_2, category_3):
    assert category_1.name == "Смартфоны"
    assert category_2.name == "Телевизоры"
    assert category_3.name == "Ноутбуки"

    assert category_1.description == "Смартфоны"
    assert category_2.description == "Современный телевизор"
    assert category_3.description == "Ноутбуки, планшеты, компьютеры"

    assert len(category_1.products) == 2
    assert len(category_2.products) == 3

    assert category_1.category_count == 3
    assert category_2.category_count == 3
    assert category_3.category_count == 3

    assert category_1.product_count == 5
    assert category_2.product_count == 5
    assert category_3.product_count == 5
