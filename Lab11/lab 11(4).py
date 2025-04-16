contacts = {
    "Alice": "9876543210",
    "Bob": "8765432109"
}

name = input("Enter contact name: ")
phone = input("Enter phone number: ")

if name in contacts:
    print(f"Updating {name}'s number.")
else:
    print(f"Adding new contact {name}.")

contacts[name] = phone
print("Updated contacts:", contacts)
