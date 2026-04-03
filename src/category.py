from abc import ABC, abstractmethod

from src.product import Product


class BaseCategoryOrder(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Category(BaseCategoryOrder):
    name: str
    description: str
    __products: list[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products  # Этого достаточно
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self):
        result = ""
        for product in self.__products:
            result += f"{str(product)}\n"
        return result.strip()

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError(
                "Добавлять можно только объекты класса Product или его наследников"
            )
        self.__products.append(product)
        Category.product_count += 1


class Order(BaseCategoryOrder):
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity
        self.total_price = self.product.price * self.quantity

    def __str__(self):
        return f"Заказ на {self.product.name}: {self.quantity} шт. Сумма: {self.total_price} руб."


class ClassIterator:
    def __init__(self, category_obj):
        self.products = category_obj._Category__products
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
