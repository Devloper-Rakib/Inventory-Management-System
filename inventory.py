class InventoryItem:
    def __init__(self, item_id, name, category, quantity, price_per_unit):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        self.history = []

    def update_quantity(self, change, operation):
        if self.quantity + change < 0:
            print(f"Please input a valid number for updating '{self.name}'. Current stock: {self.quantity}.")
            return False
        else:
            self.quantity += change
            self.history.append((operation, abs(change)))  # Log the operation
            print(f"Stock updated for '{self.name}'. New quantity: {self.quantity}.")
            return True

    def display(self):
        print(f"ID: {self.item_id} | Name: {self.name} | Category: {self.category} | "
              f"Quantity: {self.quantity} | Price: {self.price_per_unit:.2f}TK")
