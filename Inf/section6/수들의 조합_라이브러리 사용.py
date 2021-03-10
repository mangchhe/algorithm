import sys
import itertools as it

# sys.stdin = open('input.txt', 'rt')

if __name__ == '__main__':
    n, k = map(int, input().split())
    data = list(map(int, input().split()))
    m = int(input())
    cnt = 0

    for d in it.combinations(data, k):
        if sum(d) % m == 0:
            cnt += 1

    print(cnt)