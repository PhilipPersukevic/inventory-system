class Product:
    def __init__(self, id, name, category, price, quantity):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"[{self.id}] {self.name} ({self.category}) - {self.price}$ x {self.quantity}"