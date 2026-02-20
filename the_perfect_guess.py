import random

nums = random.randint(1, 40)
a = -1
guesses = 0

while a != nums:
    guesses += 1
    a = int(input("Guess the number (1 to 40): "))

    if a > nums:
        print("Lower number please")
    elif a < nums:
        print("Higher number please")
    else:
        print(f"You guessed the number {nums} correctly in {guesses} attempts!")


