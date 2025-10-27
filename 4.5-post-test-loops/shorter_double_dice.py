import random

print("HERE COMES THE DICE!")

while True:
    num_1 = random.randrange(1, 7)
    num_2 = random.randrange(1, 7)
    total = num_1 + num_2
    print(f"\nRoll #1: {num_1}\nRoll #2: {num_2}\nThe total is {total}!")

    if num_1 == num_2:
        break
