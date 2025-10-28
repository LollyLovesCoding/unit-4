import math

print("SQUARE ROOT!")
num = int(input("Enter a number: "))

while True:
    if num < 0:
        print("You can't take the square root of a negative number, that's imaginary!")
    else:
        break
    num = int(input("Try again: "))

sqrt = math.sqrt(num)
print(f"The square root of {num} is {sqrt}.")
