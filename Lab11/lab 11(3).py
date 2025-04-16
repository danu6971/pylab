inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 8
}

item = input("Enter item to sell: ").lower()
quantity = int(input("Enter quantity to sell: "))

if item in inventory:
    if inventory[item] >= quantity:
        inventory[item] -= quantity
        print(f"Sold {quantity} {item}(s). Remaining stock: {inventory[item]}")
    else:
        print(f"Not enough stock. Only {inventory[item]} {item}(s) left.")
else:
    print("Item not found in inventory.")
