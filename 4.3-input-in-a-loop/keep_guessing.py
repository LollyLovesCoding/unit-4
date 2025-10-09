import random
num = random.randrange(1, 11)
guess = int(input("I have chosen a number between 1 and 10. Try to guess it: "))
while guess != num:
    guess = int(input("I have chosen a number between 1 and 10. Try to guess it: "))

print("That's right! You're a good guesser.")
