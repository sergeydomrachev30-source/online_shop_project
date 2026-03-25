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
    assert len(category_electronics._Category__products) == 1


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


def test_price_setter_valid():
    product = Product("iPhone 15", "512GB", 1000.0, 1)
    product.price = 1200.0
    assert product.price == 1200.0


def test_price_setter_invalid():
    product = Product("iPhone 15", "512GB", 1000.0, 1)
    product.price = -500.0
    assert product.price == 1000.0
    product.price = 0
    assert product.price == 1000.0


def test_new_product_price_increase():
    p1 = Product("Iphone 15", "512GB", 210000.0, 5)
    products_list = [p1]

    new_data = {
        "name": "Iphone 15",
        "description": "512GB",
        "price": 250000.0,
        "quantity": 3,
    }
    result = Product.new_product(new_data, products_list)
    assert result.name == "Iphone 15"
    assert result.description == "512GB"
    assert result.price == 250000.0
    assert result.quantity == 8
    assert len(products_list) == 1


def test_new_product_creation():
    """Тест на создание совершенно нового товара"""
    p1 = Product("Iphone 15", "512GB", 210000.0, 5)
    products_list = [p1]
    assert len(products_list) == 1

    new_data = {
        "name": "Samsung Galaxy",
        "description": "256GB",
        "price": 150000.0,
        "quantity": 10,
    }
    new_obj = Product.new_product(new_data, products_list)
    products_list.append(new_obj)
    assert len(products_list) == 2
    assert products_list[0].name == "Iphone 15"
    assert products_list[1].name == "Samsung Galaxy"
    assert products_list[1].price == 150000.0


def test_category_products_property(category_electronics):
    result = category_electronics.products
    assert "iPhone 15" in result
    assert "120000.0 руб." in result
    assert "Остаток: 5 шт." in result


def test_category_products_display(category_electronics):
    display_string = category_electronics.products

    assert "iPhone 15" in display_string
    assert "120000.0 руб." in display_string


def test_category_add_product():
    cat = Category("Смартфоны", "...", [])
    p = Product("Nokia", "Old", 1000.0, 10)

    cat.add_product(p)

    assert Category.product_count > 0
