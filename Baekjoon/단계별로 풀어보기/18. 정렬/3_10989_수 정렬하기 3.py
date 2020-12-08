import sys

input = sys.stdin.readline
print = sys.stdout.write

data = [0 for i in range(10001)]
maxVal = 0

for i in range(int(input())):
    tmp = int(input())
    if tmp > maxVal:
        maxVal = tmp

    data[tmp] += 1

for i in range(1, maxVal + 1):
    for _ in range(data[i]):
        # print(i)
        print("{}\n".format(i))