import random

secret = random.randint(1, 20)

guess = int(input("Guess a number between 1 and 20: "))

if guess == secret:
    print("Correct!")
elif guess < secret:
    print("Too low")
else:
    print("Too high")
    import random

secret = random.randint(1, 20)

tries = 0

while True:
    guess = int(input("Guess a number between 1 and 20: "))
    tries = tries + 1

    if guess == secret:
        print("Correct!")
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")

print(f"You got it in {tries} tries!")