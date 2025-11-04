string_1 = input("Enter a string: ").lower()
string_2 = input("Enter another string: ").lower()

if string_1 in string_2 or string_2 in string_1:
    print("True")
else:
    print("False")
