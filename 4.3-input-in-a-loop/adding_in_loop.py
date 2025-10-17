total = 0
print("I will add up the numbers you give me.")

num = int(input("Number: "))
total += num
print(f"The total so far is {total}")

while num != 0:
    num = int(input("Number: "))
    total += num
    if num != 0:
        print(f"The total so far is {total}")

print(f"The total is {total}")
