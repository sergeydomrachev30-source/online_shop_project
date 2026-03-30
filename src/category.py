from src.product import Product


class Category:
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
