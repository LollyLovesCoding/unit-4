import random

again = "y"
# Deleting the previous line causes the code to still work because the variable "again" is established once more in the while loop.

while True:
    flip = random.randrange(2)  # 0-1

    if flip == 1:
        coin = "HEADS"
    else:
        coin = "TAILS"

    print("You flip a coin and it is... " + coin)

    again = input("Would you like to flip again (y/n)? ")

    if again == "n":
        break
