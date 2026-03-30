import pytest

from src.category import Category, ClassIterator
from src.product import LawnGrass, Product, Smartphone


def test_product_init(product_iphone):
    """Тест инициализации товара"""
    assert product_iphone.name == "iPhone 15"
    assert product_iphone.description == "512GB, Gray"
    assert product_iphone.price == 210000.0
    assert product_iphone.quantity == 10


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
    assert "210000.0 руб." in result
    assert "Остаток: 10 шт." in result


def test_category_products_display(category_electronics):
    display_string = category_electronics.products

    assert "iPhone 15" in display_string
    assert "210000.0 руб." in display_string


def test_category_add_product():
    cat = Category("Смартфоны", "...", [])
    p = Product("Nokia", "Old", 1000.0, 10)

    cat.add_product(p)

    assert Category.product_count > 0


@pytest.fixture
def product_samsung():
    return Product("Samsung Galaxy S23", "256GB", 180000.0, 5)


@pytest.fixture
def product_iphone():
    return Product("iPhone 15", "512GB, Gray", 210000.0, 10)


@pytest.fixture
def category_smartphones(product_samsung, product_iphone):
    return Category("Смартфоны", "Телефоны", [product_samsung, product_iphone])


def test_product_str(product_samsung):
    assert str(product_samsung) == "Samsung Galaxy S23, 180000.0 руб. Остаток: 5 шт."


def test_product_add(product_samsung, product_iphone):
    assert product_samsung + product_iphone == 3000000.0


def test_category_str(category_smartphones):
    assert str(category_smartphones) == "Смартфоны, количество продуктов: 15 шт."


def test_class_iterator(category_smartphones):
    iterator = ClassIterator(category_smartphones)
    products = []
    for product in iterator:
        products.append(product)

    assert len(products) == 2
    assert products[0].name == "Samsung Galaxy S23"
    assert products[1].name == "iPhone 15"


def test_iterator_stop(category_smartphones):
    iterator = ClassIterator(category_smartphones)
    next(iterator)
    next(iterator)
    with pytest.raises(StopIteration):
        next(iterator)


@pytest.fixture
def smartphone():
    return Smartphone("iPhone 15", "Black", 100000.0, 2, "High", "15", 128, "Black")


@pytest.fixture
def lawn_grass():
    return LawnGrass("Газон", "Зеленый", 500.0, 10, "Russia", "14 days", "Green")


@pytest.fixture
def category():
    return Category("Электроника", "Техника", [])


def test_add_same_classes(smartphone):
    """Тест: можно складывать одинаковые классы"""
    other_phone = Smartphone(
        "Samsung", "White", 80000.0, 1, "High", "S23", 256, "White"
    )
    assert smartphone + other_phone == (100000.0 * 2) + (80000.0 * 1)


def test_add_different_classes_raises_error(smartphone, lawn_grass):
    """Тест: НЕЛЬЗЯ складывать разные классы"""
    with pytest.raises(TypeError):
        smartphone + lawn_grass


def test_category_add_valid_product(category, smartphone, lawn_grass):
    """Тест: можно добавлять наследников Product в категорию"""
    category.add_product(smartphone)
    category.add_product(lawn_grass)
    # Проверяем, что в списке 2 товара
    assert "iPhone 15" in category.products
    assert "Газон" in category.products


def test_category_add_invalid_object_raises_error(category):
    """Тест: НЕЛЬЗЯ добавлять в категорию объекты не из семейства Product"""
    with pytest.raises(TypeError):
        category.add_product("Это просто строка, а не продукт")

    with pytest.raises(TypeError):
        category.add_product(500)
