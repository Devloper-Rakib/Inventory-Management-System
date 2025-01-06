from management import InventoryManagementSystem

def main():
    system = InventoryManagementSystem()

    while True:
        print("\n--- Inventory Management System ---")
        print("1. Add Product")
        print("2. Stock Update")
        print("3. Sell Product")
        print("4. Stock History")
        print("5. Delete Products")
        print("6. Search Products")
        print("7. Show all Products")
        print("8. Exit")

        choice = input(">>> ")

        if choice == '1':
            item_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            category = input("Enter Product Category: ")
            quantity = int(input("Enter Product Quantity: "))
            price_per_unit = float(input("Enter Product Price per Unit: "))
            system.add_product(item_id, name, category, quantity, price_per_unit)

        elif choice == '2':
            item_id = input("Enter Product ID: ")
            amount = int(input("Enter Quantity to Add (+) or Remove (-): "))
            system.update_stock(item_id, amount)

        elif choice == '3':
            item_id = input("Enter Product ID: ")
            quantity = int(input("Enter Quantity to Sell: "))
            system.sell_product(item_id, quantity)

        elif choice == '4':
            item_id = input("Enter Product ID: ")
            system.show_stock_history(item_id)

        elif choice == '5':
            item_id = input("Enter Product ID to Delete: ")
            system.delete_product(item_id)

        elif choice == '6':
            item_id = input("Enter Product ID: ")
            system.search_product(item_id)

        elif choice == '7':
            system.show_all_products()

        elif choice == '8':
            break

        else:
            print("Invalid number.")


main()
