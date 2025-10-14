import random
num = random.randrange(1, 101)
print("I'm thinking of a number between 1-100. You have 7 guesses.")
guesses = 1
guess = int(input("First guess: "))

while num != guess and guesses <= 7:
    if num > guess:
        print("Sorry, you are too low.")
    elif num < guess:
        print("Sorry, that guess is too high.")
    guess = int(input(f"Guess # {guesses}: "))
    guesses += 1

if guess == num:
    print("You guessed it! What are the odds?!?")
else:
    print("Sorry, you didn't guess it in 7 tries. You lose.")
