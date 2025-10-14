import random
num = random.randrange(1, 11)
print("I have chosen a number between 1 and 10. Try to guess it. ")
guess = int(input("Your guess: "))
guesses = 1

while num != guess:
    print("That is incorrect. Guess again.")
    guess = int(input("Your guess: "))
    guesses += 1

if guesses <= 5:
    rating = "good"
    only = " only"
elif guesses <= 10:
    rating = "bad"
    only = ""
else:
    rating = "horrible"
    only = ""

print(f"That's right! You're a {rating} guesser.\nIt{only} took you {guesses} tries.")
