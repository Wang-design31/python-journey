age = int(input("How old are you? "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

password = input("Enter a password: ")
if password == "nairobi2026":
    print("Access granted.")
else:
    print("Access denied.")

score = int(input("Enter your score: "))

if score >= 70:
    print("Distinction")
elif score >= 50:
    print("Pass")
else:
    print("Fail")