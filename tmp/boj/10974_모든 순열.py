# https://www.acmicpc.net/problem/10974

# 방법 1

def traverse(nList):
    if len(nList) == N:
        print(' '.join(map(str, nList)))
        return
    else:
        for i in range(1, N + 1):
            if not visited.get(i):
                visited[i] = 1
                nList.append(i)
                traverse(nList)
                nList.pop()
                del visited[i]

N = int(input())
visited = {}

traverse([])

# 방법 2
# 전역 변수로 하나 인자로 넘겨주나 메모리 값이 다른지 확인
# 결론 : 전역 변수나 인자로 넘겨주나 메모리 값은 동일

def traverse():
    if len(nList) == N:
        print(' '.join(map(str, nList)))
        return
    else:
        for i in range(1, N + 1):
            if not visited.get(i):
                visited[i] = 1
                nList.append(i)
                traverse()
                nList.pop()
                del visited[i]

N = int(input())
nList = []
visited = {}

traverse()
