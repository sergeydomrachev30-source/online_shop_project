import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_iphone():
    return Product("iPhone 15", "512GB, Gray", 120000.0, 5)


@pytest.fixture
def category_electronics(product_iphone):
    Category.category_count = 0
    Category.product_count = 0
    return Category("Электроника", "Гаджеты", [product_iphone])
