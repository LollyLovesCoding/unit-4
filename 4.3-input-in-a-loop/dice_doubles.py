import random
print("HERE COMES THE DICE!")
num_1 = random.randrange(1, 7)
num_2 = random.randrange(1, 7)
total = num_1 + num_2
print(f"\nRoll #1: {num_1}\nRoll #2: {num_2}\nThe total is {total}!")

while num_1 != num_2:
    num_1 = random.randrange(1, 7)
    num_2 = random.randrange(1, 7)
    total = num_1 + num_2
    print(f"\nRoll #1: {num_1}\nRoll #2: {num_2}\nThe total is {total}!")
