a = input("Enter a string: ")
b = input("Enter another string: ")
i = 0
result = ""

while i < len(a) and i < len(b):
    result += a[i] + b[i]
    i += 1

if len(a) > len(b):
    result += a[i:]
else:
    result += b[i:]

print(result)
