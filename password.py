or_password = "123456"
password = input("Enter your password: ")
n = 0
if password == or_password:
    print("OK")
    print("Yes")
    name = input("Enter your name: ")
    if name == "admin":
        print("Hi, admin")
    else:
        print("Hi, user!")
else:
    print("Error")
    n = n + 1
    if n > 5:
        print("Too many tries")
    else:
        print("Try again")
