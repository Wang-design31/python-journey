for i in range(1, 4):
    print(f"Round {i}")
    number = int(input("Enter a number: "))
    for j in range(1, 11):
        result = number * j
        print(f"{number} x {j} = {result}")