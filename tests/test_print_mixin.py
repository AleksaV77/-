from src.class_product import Product
from src.class_lawngrass import LawnGrass
from src.class_smartphone import Smartphone

def test_print_mixin(capsys):
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", -50.0, 5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, -50.0, 5)"

    Smartphone(
        "Samsung", "200MP камера", 180000.0, 5, "Android 13",
    "Galaxy S23 Ultra", "256 GB", "black")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Samsung, 200MP камера, 180000.0, 5)"

    LawnGrass(
        "Газонная трава", "спортивный Канада Грин", 3000.0, 8, "Canada",
        "15", "green")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газонная трава, спортивный Канада Грин, 3000.0, 8)"
