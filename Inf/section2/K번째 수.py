import sys

#sys.stdin = open('input.txt', 'rt')

t = int(input())

for i in range(t):
    n, s, e, k = map(int, input().split())
    data = list(map(int, input().split()))
    print('#{} {}'.format(i+1, sorted(data[s - 1 : e])[k - 1], sep=''))
    