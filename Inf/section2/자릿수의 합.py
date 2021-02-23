import sys

# sys.stdin = open('input.txt', 'rt')

def digit_sum(x):

    result = 0
    
    while x > 0:
        result += x % 10
        x //= 10

    return result

n = int(input())

data = list(map(int, input().split()))

minVal = 0
idx = 0

for i, d in enumerate(data):
    num = digit_sum(d)
    if minVal < num:
        minVal = num
        idx = i
    
print(data[idx])