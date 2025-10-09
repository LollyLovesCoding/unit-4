PIN = 12345 # If PIN was stored as an integer rather than a string, we would have to convert the user's input to an integer in order to evaluate.

print("WELCOME TO THE BANK OF GALLO.")
entry = int(input("ENTER YOUR PIN: ")) # Convert string to integer to compare

while entry != PIN:
    # A while loop is similar to an if statement in the sense that they both evaluate a condition that is either True or False. If the condition evaluates to True, the statement inside gets executed.
    # A while loop is different from an if statement since an if statement only evaluates once, whereas a while loop repeatedly evaluates a condition while it is True.
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = int(input("ENTER YOUR PIN: ")) # Convert string to integer to compare
    # Commenting the above line results in an infinite loop if you enter the PIN wrong because the PIN will never evaluate to the actual PIN if the user doesn't get a chance to enter it again.

print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")
