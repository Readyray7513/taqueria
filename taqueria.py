def menu():
    # Dictionary of menu items and prices
    return {
        "baja taco": 4.25,
        "burrito": 7.50,
        "bowl": 8.50,
        "nachos": 11.00,
        "quesadilla": 8.50,
        "super burrito": 8.50,
        "super quesadilla": 9.50,
        "taco": 3.00,
        "tortilla salad": 8.00
    }


total = 0.0
menu_items = menu()

while True:
    try:
        order = input("Hello, what would you like to order today? ").strip().lower()
    except EOFError:
        print()
        break
    if order in menu_items:
        total += menu_items[order]
        print(f"Total: ${total:.2f}")