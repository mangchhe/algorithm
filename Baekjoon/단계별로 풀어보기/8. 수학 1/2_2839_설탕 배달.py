N = int(input())

count = 0

while N != 0:
    if N >= 5:
        N -= 5
        count += 1
    elif N >= 3:
        N -= 3
        count += 1
    else:
        N += 2

print(count)
