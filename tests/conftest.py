import pytest

from src.class_category import Category
from src.class_product import Product
from src.class_smartphone import Smartphone
from src.class_lawngrass import LawnGrass


@pytest.fixture
def category_1():
    return Category(
        name="Смартфоны",
        description="Смартфоны",
        products=[
            Product(
                "Samsung Galaxy S23 Ultra",
                "256GB, Серый цвет, 200MP камера",
                180000.0,
                5),
            Product(
                "Iphone 15",
                "512GB, Gray space",
                210000.0,
                8)
        ]
    )

@pytest.fixture
def category_2():
    return Category(
        name="Телевизоры",
        description="Современный телевизор",
        products=[
            Product(
                "SBER SDX-xxF2139",
                "2024 RU, черный, 60 Гц",
                140000.0,
                3),
            Product(
                "Xiaomi TV A 32",
                "2025, черный, 60 Гц, Android TV",
                250000.0,
                2),
            Product(
                "QD-Mini LED TCL 85X955",
                "144 Гц, QLED, Mini LED",
                299000.0,
                1)
        ]
    )

@pytest.fixture
def category_3():
    return Category(
        name="Ноутбуки",
        description="Ноутбуки, планшеты, компьютеры",
        products=[]
    )

@pytest.fixture
def category_4():
    return Category(
        name="Смартфоны",
        description="Смартфоны",
        products=[
            Product(
                "Iphone 15",
                "512GB, Gray space",
                210000.0,
                8)
        ]
    )

@pytest.fixture
def add_product_1():
    return (
        'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5\n'
        'Iphone 15, 210000.0 руб. Остаток: 8\n'
        'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14\n'
    )

@pytest.fixture
def add_product_2():
    return 'Xiaomi Redmi Note 10, 15000.0 руб. Остаток: 5\n'


@pytest.fixture
def product_1():
    return Product(
        "Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

@pytest.fixture
def product_2():
    return Product(
        "Xiaomi Redmi Note 10", "", 15000.0, 5)

@pytest.fixture
def product_3():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", -50.0, 5)

@pytest.fixture
def product_dict():
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 170000.0,
        "quantity": 3
    }

@pytest.fixture
def test_class_smartphone():
    return Smartphone(
        "Iphone", "512GB, Gray space", 210000.0, 8, "Apple A16 Bionic",
    "Iphone 15", "256 ГБ", "black")

@pytest.fixture
def test_class_smartphone_2():
    return Smartphone(
        "Samsung", "200MP камера", 180000.0, 5, "Android 13",
    "Galaxy S23 Ultra", "256 GB", "black")


@pytest.fixture
def test_class_lawn_grass():
    return LawnGrass(
        "Газонная трава", "спортивный Канада Грин", 3000.0, 8, "Canada",
    "15", "green")

@pytest.fixture
def test_class_lawn_grass_2():
    return LawnGrass(
        "Газонная трава", "Городской газон", 4000.0, 5, "Russia",
    "10", "green")

@pytest.fixture
def user_without_quantity():
    return Category(
        name="Смартфоны",
        description="Смартфоны",
        products=[
            Product(
                "Iphone 15",
                "512GB, Gray space",
                0.0,
                0)
        ]
    )
