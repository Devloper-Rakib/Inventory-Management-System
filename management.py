from inventory import InventoryItem

class InventoryManagementSystem:
    def __init__(self):
        self.inventory = {}

    def add_product(self, item_id, name, category, quantity, price_per_unit):
        if item_id in self.inventory:
            print("Product ID already exists. Please use a another ID.")
        else:
            self.inventory[item_id] = InventoryItem(item_id, name, category, quantity, price_per_unit)
            print(f"Product '{name}' added successfully.")

    def update_stock(self, item_id, amount):
        product = self.inventory.get(item_id)
        if product:
            product.update_quantity(amount, "Stock Update")
        else:
            print("Product not found.")

    def sell_product(self, item_id, quantity):
        product = self.inventory.get(item_id)
        if product:
            if product.update_quantity(-quantity, "Sale"):
                print(f"Sold {quantity} of '{product.name}'.")
        else:
            print("Product not found.")

    def show_stock_history(self, item_id):
        product = self.inventory.get(item_id)
        if product:
            print(f"\n--- Stock History for '{product.name}' ---")
            for operation, amount in product.history:
                print(f"{operation}: {amount}")
        else:
            print("Product not found.")

    def delete_product(self, item_id):
        if item_id in self.inventory:
            removed_item = self.inventory.pop(item_id)
            print(f"Product '{removed_item.name}' deleted from the inventory.")
        else:
            print("Product not found.")

    def search_product(self, item_id):
        product = self.inventory.get(item_id)
        if product:
            product.display()
        else:
            print("Product not found.")

    def show_all_products(self):
        if self.inventory:
            print("\n--- All Products ---")
            for product in self.inventory.values():
                product.display()
        else:
            print("The inventory is empty.")
