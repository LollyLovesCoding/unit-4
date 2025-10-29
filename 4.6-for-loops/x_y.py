for x in range(-10, 10, 1):
    print(x, end="\t")
    print(x ** 2)
    print(x + 0.5, end="\t")
    print((x + 0.5) ** 2)
    if x == 9:
        print("10", end="\t")
        print("100")
