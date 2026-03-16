# Menu and ordering program

menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 80,
    'Coffee': 60,
    'Salad': 30,
}

def find_menu_key(name):
    """Return canonical menu key for case-insensitive name, or None."""
    name = name.strip().lower()
    for k in menu:
        if k.lower() == name:
            return k
    return None

def add_prices(ordered_items):
    """Return total price for list of ordered menu keys (case-insensitive accepted)."""
    total = 0
    for it in ordered_items:
        key = find_menu_key(it)
        if key:
            total += menu[key]
    return total

def display_menu():
    print("Menu:")
    for k, v in menu.items():
        print(f" - {k}: {v}")
    print()

def main():
    display_menu()
    orders = []
    print("Choose the item you want to order:")
    while True:
        choice = input("> ").strip()
        if not choice:
            print("Please enter an item name.")
            continue

        key = find_menu_key(choice)
        if key:
            orders.append(key)
            print(f"{key} added. Price: {menu[key]}")
        else:
            print("Item not mentioned in menu.")

        another = input("Do you want to order any other item say yes or no: ").strip().lower()
        if not another.startswith('y'):
            break
        print("Name the item again:")

    if orders:
        total = add_prices(orders)
        print(f"Your total price of ordered items is {total}")
    else:
        print("No items ordered.")

    print("Thanks for arriving us")

if __name__ == "__main__":
    main()