start = int(input("Count from: "))
stop = int(input("Count to: "))
increment = int(input("Count by: "))

for n in range(start, stop + 1, increment):
    print(n, end=" ")
