import csv
from product import Product

class Inventory:
    def __init__(self, csv_file = "products.csv"):
        self.products = []
        self.csv_file = csv_file
        self.load_from_csv()

    def add_product(self, product):
        self.products.append(product)
        print(f"Product '{product.name}' added!")
        self.save_to_csv()

    def list_products(self):
        if not self.products:
            print("Inventory is empty!")
            return
        print("\n--- Inventory List ---")
        for product in self.products:
            print(product)

    def find_product(self, id):
        for product in self.products:
            if product.id == id:
                return product
        return None
    
    def remove_product(self, id):
        product = self.find_product(id)
        if product:
            self.products.remove(product)
            print(f"Product '{product.name}' removed!")
            self.save_to_csv()
        else:
            print("Product not found!")

    def save_to_csv(self):
        with open(self.csv_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "name", "category", "price", "quantity"])
            for p in self.products:
                writer.writerow([p.id, p.name, p.category, p.price, p.quantity])
            
    def load_from_csv(self):
        try:
            with open(self.csv_file, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    product = Product(
                        row["id"],
                        row["name"],
                        row["category"],
                        float(row["price"]),
                        int(row["quantity"])
                    )
                    self.products.append(product)
        except FileNotFoundError:
            self.products = []