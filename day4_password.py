tries = 0
while tries < 3:
    password = input("Enter the password: ")
    if password == "nairobi2026":
        print("Access granted")
        break
    else:
        tries = tries + 1
        print("Wrong, try again")
        if tries == 3:
            print("locked out!")