import sys
import heapq

# sys.stdin = open('input.txt', 'rt')

list = []

while True:
    n = int(input())
    if n == 0:
        if list:
            print(heapq.heappop(list))
        else:
            print('-1')
    elif n > 0:
        heapq.heappush(list, n)
    else:
        break