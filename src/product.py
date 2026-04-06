from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name, description, price, quantity):
        """у каждого продукта должны быть эти 4 свойства"""
        pass

    @abstractmethod
    def __str__(self):
        """каждый продукт должен уметь печатать инфо о себе"""
        pass


class MixinLog:
    def __init__(self, *args, **kwargs):
        print(f"Был создан объект: {self.__repr__()}")
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"


class Product(MixinLog, BaseProduct):
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.__price = 0.0
        self.price = price
        self.quantity = quantity

        super().__init__(name, description, price, quantity)

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Можно складывать только товары одного класса")
        return (self.quantity * self.price) + (other.price * other.quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            user_answer = input(f"Цена на {self.name} понижается. Вы согласны? (y/n): ")
            if user_answer.lower() == "y":
                self.__price = new_price
        else:
            self.__price = new_price

    @classmethod
    def new_product(
        cls, product_params: dict[str, Any], products_list: list["Product"]
    ):
        if product_params["quantity"] <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        for product in products_list:
            if product.name == product_params["name"]:
                product.quantity += product_params["quantity"]
                product.price = product_params["price"]
                return product

        return cls(
            product_params["name"],
            product_params["description"],
            product_params["price"],
            product_params["quantity"],
        )


class Smartphone(Product):

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
