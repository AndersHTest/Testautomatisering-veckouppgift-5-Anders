class StockItem:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


class Stock:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)
