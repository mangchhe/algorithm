'''
※ 입력
6

※ 출력
4
'''

from collections import deque

result = deque(val for val in range(1,int(input())+1))

while len(result) != 1:

    result.popleft()
    result.append(result.popleft())

print(result.pop())