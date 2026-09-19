class StockItem:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __repr__(self):
        return f"{self.name}: {self.amount}"


class Stock:
    def __init__(self):
        self.items = []

    def __repr__(self) -> str:
        return str(self.items)

    def add_product(self, product):
        self.items.append(product)

    def remove_product(self, product, amount):
        if product in self.items and product.amount >= amount:
            product.amount -= amount

    def get_items(self):
        return self.items
