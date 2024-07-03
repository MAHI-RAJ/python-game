import random

f=open('file#4.txt','a')

def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it.")

    while True:
        guess = int(input("Enter your guess: "))
        f.write(str(guess))
        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

guessing_game()
f.close()