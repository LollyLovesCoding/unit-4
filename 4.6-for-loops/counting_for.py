print("Type in a message, and I'll display it five times.")

message = input("Message: ")

for n in range(2, 21, 2): # 1. Changing the variable name for this loop (n) does not do anything to the code if you print that number in the print statement.
                          # 1. I suppose you chose the variable n because it represents a number and is easy to replicate.
                          # 2. The first number (0) tells the program which number to start counting at, this number is inclusive.
                          # 3. The second number (5) tells the program which number to stop at, but this number is exclusive, meaning it is not counted in the loop.
                          # 3. The third number (1) tells the program by what interval the numbers count. For example, changing this number to 2 counts the even numbers from 0 to 4 (0, 2, 4).
                          # 4. Changing the range function to only have one input (e.g. range(7)) interprets the entered number as the stop number, starting from 0. For example, it will print all the numbers from 0 to 6.
                          # 5. Changing the range function to two inputs (e.g. range(3, 9)) interprets the first numbers as the start number and the second number as the stop number. For example, it will print all the numbers from 3 to 8.
    print(f"{n}. {message}")
