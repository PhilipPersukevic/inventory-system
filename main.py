from inventory import Inventory
from product import Product

def main():
    inventory = Inventory()

    while True:
        print("\n=== INVENTORY MENU ===")
        print("1. Add product")
        print("2. List product")
        print("3. Remove product")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            product_id = input("Enter ID: ")
            name = input("Enter name: ")
            category = input("Enter category: ")
            try:
                price = float(input("Enter price: "))
            except ValueError:
                print("Invalid price! Must be a number.")
                continue

            try:
                quantity = int(input("Enter quantity: "))
            except ValueError:
                print("Invalid quantity! Must be an integer.")
                continue
            product = Product(product_id, name, category, price, quantity)
            inventory.add_product(product)

        elif choice == "2":
            inventory.list_products()
        
        elif choice == "3":
            product_id = input("Enter ID to remove: ")
            inventory.remove_product(product_id)

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()