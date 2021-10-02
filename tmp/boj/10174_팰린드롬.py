# https://www.acmicpc.net/problem/10174

print('\n'.join(['Yes' if word == word[::-1] else 'No' for word in [input().lower() for _ in range(int(input()))]]))
