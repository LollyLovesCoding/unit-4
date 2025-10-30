message = input("What is your message? ")

print()
print(f"Your message is {len(message)} characters long.")
print(f"The first character is at position 0 and is '{message[0]}'.")
lastpos = len(message) - 1
print(f"The last character is at position {lastpos} and is '{message[lastpos]}'.")
print()
print("Here are all the characters, one at a time:\n")

for i in range(len(message)):
    print(f"\t{i} - '{message[i]}'")

a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0
for i in range(len(message)):
    letter = message[i].lower()
    if letter == 'a':
        a_count += 1
    elif letter == 'e':
        e_count += 1
    elif letter == 'i':
        i_count += 1
    elif letter == 'o':
        o_count += 1
    else:
        u_count += 1

print(f"\nYour message contains the letter 'a' {a_count} times, 'e' {e_count} times, 'i' {i_count} times, 'o' {o_count} times, 'u' {u_count} times.")

# 1. Printing out range(7) prints out the line "range(0, 7)" into the console. Instead, printing out list(range(7)) prints out the list of numbers from 0 to 6.
# 2. Printing out the iterations for the i variable prints out a list of numbers from 0 to 4.
# 3. The length of the message "box" is 3, and the letter "x" is at index 2 because Python starts counting at 0.
