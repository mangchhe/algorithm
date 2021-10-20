# https://www.acmicpc.net/problem/2776

for _ in range(int(input())):
    N = int(input())
    note1 = {s : 1 for s in input().split()}
    M = int(input())
    for s in input().split(): print(1) if note1.get(s) else print(0)
