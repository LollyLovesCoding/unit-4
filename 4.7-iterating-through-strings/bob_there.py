string = input("Enter a string: ")
i = 0

while i < len(string) - 2:
    if string[i] == "b" and string[i + 2] == "b":
        break
    i += 1

print("True")
