print("Type in a message, and I'll display it several times.")

message = input("Message: ")
print()

n = int(input("How many times? "))
while n < 10:
    print(f"{n * 10 + 10}. {message}")
    n += 1
    # n += 1 increases the counter value by 1 each time the code runs in the while loop. Removing it results in an infinite loop because n will always be less than 5.
