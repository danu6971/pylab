def get_ticket_price(age):
    if age < 5:
        return "Free"
    elif age <= 18:
        return "₹100"
    elif age <= 60:
        return "₹200"
    else:
        return "₹150"
age = int(input("Enter your age: "))
print(f"Your ticket price is: {get_ticket_price(age)}")
