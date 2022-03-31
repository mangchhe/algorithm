from collections import deque

def solution(s):
    q = deque([])
    
    for i in range(len(s)):
        q.append((i, s[i]))
        
    while len(q) > 1:
        if q[0][1] == q[1][1]:
            q.popleft()
            q.popleft()
        elif q[0][0] > q[-1][0] and q[0][1] == q[-1][1]:
            q.popleft()
            q.pop()
        else:
            if q[0][0] > q[1][0]:
                break
            q.append(q.popleft())
            
    if q:
        return 0
    else:
        return 1
