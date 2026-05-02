import json

products = []
total_profit = 0


# ----------------
# Load Data
# ----------------
def load_data():
    global products
    try:
        with open("products.json", "r") as file:
            products = json.load(file)
    except:
        products = []


# ----------------
# Save Data
# ----------------
def save_data():
    with open("products.json", "w") as file:
        json.dump(products, file)


# -----------------
# Add Product
# -----------------
def add_product():
    name = input("Enter product name: ")

    try:
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        if price <= 0 or quantity < 0:
            print("Invalid values!")
            return

    except:
        print("Invalid values!")
        return

    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    products.append(product)
    print("Product added successfully!")


# -------------------
# Show Products
# -------------------
def show_products():
    if not products:
        print("No products available.")
        return

    for i, product in enumerate(products):
        print(f"[{i+1}] Name: {product['name']} | Price: ${product['price']} | Qty: {product['quantity']}")


# --------------------
# Delete Product
# --------------------
def delete_product():
    show_products()

    try:
        choice = int(input("Enter product number to delete: ")) - 1

        if 0 <= choice < len(products):
            confirm = input("Are you sure? (y/n): ").strip().lower()

            if confirm in ["y", "yes"]:
                deleted = products.pop(choice)
                print(f"Deleted: {deleted['name']}")
            else:
                print("Cancelled.")
        else:
            print("Invalid number!")

    except:
        print("Invalid input!")


# ------------------
# Sell Product
# ------------------
def sell_product():
    global total_profit

    show_products()

    try:
        choice = int(input("Choose product number: ")) - 1
        quantity = int(input("Enter quantity: "))

        if 0 <= choice < len(products):
            if products[choice]["quantity"] >= quantity:
                total = products[choice]["price"] * quantity
                products[choice]["quantity"] -= quantity
                total_profit += total

                print(f"Total price: ${total}")
            else:
                print("Not enough stock!")
        else:
            print("Invalid product!")

    except:
        print("Invalid input!")


# --------------------
# Search Product
# --------------------
def search_product():
    keyword = input("Enter product name to search: ").strip().lower()

    found = False

    for product in products:
        if keyword in product["name"].strip().lower():
            print(f"Name: {product['name']} - Price: ${product['price']} - Qty: {product['quantity']}")
            found = True

    if not found:
        print("No matching product found.")


# -----------------
# Show Profit
# -----------------
def show_profit():
    print(f"Total Profit: ${total_profit}")


# -------------------
# Main Function
# -------------------
def main():
    while True:
        print("\n--- Store Menu ---")
        print("1. Add Product")
        print("2. Show Products")
        print("3. Delete Product")
        print("4. Sell Product")
        print("5. Search Product")
        print("6. Show Profit")
        print("7. Save & Exit")

        try:
            choice = int(input("Enter choice: "))
        except:
            print("Invalid input! Must be a number.")
            continue

        if choice == 1:
            add_product()
        elif choice == 2:
            show_products()
        elif choice == 3:
            delete_product()
        elif choice == 4:
            sell_product()
        elif choice == 5:
            search_product()
        elif choice == 6:
            show_profit()
        elif choice == 7:
            save_data()
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


# --------------------
# Run Program
# --------------------
load_data()
main()