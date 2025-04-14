def check_login(username, password):
    if username == "admin" and password == "1234":
        return "Login successful"
    else:
        return "Invalid credentials"
username = input("Enter username:")
password = input("Enter password:")
print(check_login(username, password))
