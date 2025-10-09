# 1
count = 1
total = 0
while count <= 10:
    total += count
    count += 1
print(total)

# 2
count = 100
total = 0
while count <= 200:
    total += count
    count += 1
print(total)

# 3
count = 100
total_1 = 0
while count <= 200:
    total_1 += count
    count += 1
count = 200
total_2 = 0
while count <= 300:
    total_2 += count
    count += 1
print(total_1 - total_2)

# 4
count = 1000
total = 0
while count <= 10000:
    total += count
    count += 5
print(total)

# 5
count = 1
total = 0
while count <= 100:
    if count % 5 == 0 and count % 3 != 0:
        total += count
    count += 1
print(total)
