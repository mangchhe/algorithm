from collections import deque

input = __import__('sys').stdin.readline

N = int(input())

balloon = list(map(int, input().split()))
balloonQ = deque([])
for i in range(len(balloon)):
    balloonQ.append([balloon[i], i + 1])

ans = [1]
paper = balloonQ.popleft()[0] 

while balloonQ:

    if paper < 1:
        paper = abs(paper)
        for _ in range(paper):
            balloonQ.appendleft(balloonQ.pop())
    else:
        paper = abs(paper)
        for _ in range(paper - 1):
            balloonQ.append(balloonQ.popleft())
    
    tmp = balloonQ.popleft()
    paper = tmp[0]
    ans.append(tmp[1])

print(' '.join(map(str, ans)))
