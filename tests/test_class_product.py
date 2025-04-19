def test_product_init(product_1, product_2):
    assert product_1.name == "Xiaomi Redmi Note 11"
    assert product_1.description == "1024GB, Синий"
    assert product_1.price == 31000.0
    assert product_1.quantity == 14

    assert product_2.name == "Xiaomi Redmi Note 10"
    assert product_2.description == ""
    assert product_2.price == 15000.0
    assert product_2.quantity == 5
