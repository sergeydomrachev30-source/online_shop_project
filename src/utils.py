import json
import os

from .category import Category, Product


def load_data_from_json(file_path: str) -> list[Category]:
    """Читает JSON и возвращает список объектов классов Category"""
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

        categories = []
        for category_data in data:
            products_list = []
            for product_data in category_data["products"]:
                product = Product(
                    name=product_data["name"],
                    description=product_data["description"],
                    price=product_data["price"],
                    quantity=product_data["quantity"],
                )
                products_list.append(product)

            category = Category(
                name=category_data["name"],
                description=category_data["description"],
                products=products_list,
            )
            categories.append(category)
        return categories


if __name__ == "__main__":
    path = "../data/products.json"
    result = load_data_from_json(path)
    for cat in result:
        print(f"Категория: {cat.name}, Товаров: {len(cat.products)}")
