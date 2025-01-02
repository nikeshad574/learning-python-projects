import random

number = random.randint(0, 100)
tries = 0

while True:
    guess = input("\nGuess The Number From 0 - 100: ")

    if guess.isdigit():
        guess = int(guess)
    else:
        print("Must be Number!")
        continue

    if guess == number:
        print("You found the Number")
        break
    elif guess > number:
        print("Too High")
    elif guess < number:
        print("Too Low")
    tries+=1
    
print(f"You had to try for {tries} times.")