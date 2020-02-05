N = int(input())

count = 0

for i in range(1, N +1):
    if i < 100:
        count += 1
    else:
        tmp = str(i)
        if int(tmp[2]) - int(tmp[1]) == int(tmp[1]) - int(tmp[0]):
            count += 1

print(count)