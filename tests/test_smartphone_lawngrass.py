import pytest


def test_smartphone_init(test_class_smartphone):
    assert test_class_smartphone.name == "Iphone"
    assert test_class_smartphone.description == "512GB, Gray space"
    assert test_class_smartphone.price == 210000.0
    assert test_class_smartphone.quantity == 8
    assert test_class_smartphone.efficiency == "Apple A16 Bionic"
    assert test_class_smartphone.model == "Iphone 15"
    assert test_class_smartphone.memory == "256 ГБ"
    assert test_class_smartphone.color == "black"

def test_lawn_grass_init(test_class_lawn_grass):
    assert test_class_lawn_grass.name == "Газонная трава"
    assert test_class_lawn_grass.description == "спортивный Канада Грин"
    assert test_class_lawn_grass.price == 3000.0
    assert test_class_lawn_grass.quantity == 8
    assert test_class_lawn_grass.country == "Canada"
    assert test_class_lawn_grass.germination_period == "15"
    assert test_class_lawn_grass.color == "green"

def test_smartphone_add(test_class_smartphone, test_class_smartphone_2):
    assert test_class_smartphone + test_class_smartphone_2 == 2580000

def test_lawn_grass_add(test_class_lawn_grass, test_class_lawn_grass_2):
    assert test_class_lawn_grass + test_class_lawn_grass_2 == 44000

def test_smartphone_add_error(test_class_smartphone):
    with pytest.raises(TypeError):
        result = test_class_smartphone + 1

def test_lawn_grass_add_error(test_class_lawn_grass_2):
    with pytest.raises(TypeError):
        result = test_class_lawn_grass_2 + 1

