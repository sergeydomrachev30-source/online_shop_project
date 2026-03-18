from src.category import Category
from src.product import Product


def test_product_init(product_iphone):
    """Тест инициализации товара"""
    assert product_iphone.name == "iPhone 15"
    assert product_iphone.description == "512GB, Gray"
    assert product_iphone.price == 120000.0
    assert product_iphone.quantity == 5


def test_category_init(category_electronics):
    """Тест инициализации категории"""
    assert category_electronics.name == "Электроника"
    assert category_electronics.description == "Гаджеты"
    assert len(category_electronics.products) == 1


def test_category_counters():
    """Тест подсчета количества категорий и продуктов"""

    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("Товар 1", "Опис 1", 100, 1)
    p2 = Product("Товар 2", "Опис 2", 200, 2)
    p3 = Product("Товар 3", "Опис 3", 300, 3)

    _ = Category("Кат 1", "Опис", [p1, p2])
    assert Category.category_count == 1
    assert Category.product_count == 2

    _ = Category("Кат 2", "Опис", [p3])
    assert Category.category_count == 2
    assert Category.product_count == 3
