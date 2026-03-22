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

    @property
    def products(self):
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт. \n"
        return result.strip()

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1
