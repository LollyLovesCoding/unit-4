stop = int(input("Number: "))
sum = 0

for n in range(1, stop + 1):
    print(n, end=" ")
    sum += n

print(f"\nThe sum is {sum}.")
