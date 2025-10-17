# 1
n = -1
while n < 10:
    n += 1
    if n == 7:
        continue
    print(n)

# 2
n = 4
total = 0
while n < 20:
    n += 1
    if n % 3 == 0:
        continue
    total += n
print(total)

# 3
start_n = int(input("Starting number: ")) - 1
end_n = int(input("Ending number: "))
total = 0
while start_n <= end_n:
    start_n += 1
    if start_n == 13 or start_n == 31:
        break
    total += start_n
print(total)

# 4
while True:
    word = input("Enter a word: ")
    print(f"Your word: {word}")
    if word == "stop":
        break
print("Goodbye!")
