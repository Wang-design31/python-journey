import random

secret = random.randint(1, 20)
max_tries = 5
tries = 0

while tries < max_tries:
    guess = int(input("Guess a number between 1 and 20: "))
    tries = tries + 1

    if guess == secret:
        print(f"Correct! You got it in {tries} tries!")
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")

if guess != secret:
    print(f"Game over, the number was {secret}")