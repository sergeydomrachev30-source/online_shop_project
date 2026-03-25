from typing import Any


class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = 0.0
        self.price = price
        self.quantity = quantity

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
