print("Type in a message, and I'll display it several times.")

count = 0
message = input("Message: ")
print()

n = int(input("How many times? "))
while count < n:
    print(f"{(count + 1) * 10}. {message}")
    count += 1
    # n += 1 increases the counter value by 1 each time the code runs in the while loop. Removing it results in an infinite loop because n will always be less than 5.
