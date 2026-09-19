class StockItem:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


class Stock:
    def __init__(self):
        self.items = []
        self.cart = []

    def add_product(self, product):
        self.items.append(product)

    def add_product_to_cart(self, name, amount):
        if name.amount - amount >= 0:
            name.amount -= amount
            self.cart.append(f"{name.name}: {amount} st")
            return True
        else:
            return False


    def get_product_amount(self, name):
        a = []
        for i in self.items:
            if i.name == name:
                a.append(i.amount)
        if not a:
            return 0
        else:
            return a[0]

    def return_product(self, name, amount):
        name.amount += amount
        for i in range(amount):
            self.cart.append(name)

    def get_cart_items(self):
        b = []
        for i in self.cart:
            b.append(i)

        c = ""
        for i in range(len(b)):
            c += str(f"{b[i]}")
        return c
