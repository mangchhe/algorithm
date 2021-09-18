# https://www.acmicpc.net/problem/1759

input = __import__('sys').stdin.readline

def isCipher(s):
    moCnt = 0
    notMoCnt = 0
    for i in s:
        if i in ['a', 'e', 'i', 'o', 'u']:
            moCnt += 1
        else:
            notMoCnt += 1
    if moCnt > 0 and notMoCnt > 1:
        return True
    else:
        return False

def traverse(n, s):
    
    if len(s) == L:
        if isCipher(s):
            print(s)
        return

    if n == C:
        return
    else:
        for i in range(n, C):
            traverse(i + 1, s + words[i])

if __name__ == '__main__':

    L, C = map(int, input().split())
    words = sorted(map(str, input().split()))
    traverse(0, '')
