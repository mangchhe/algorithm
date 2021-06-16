N = int(input())
visited = []
ans = 0

def func(x):
    global ans
    if len(visited) == N:
        ans += 1
    else:
        for i in range(N):
            for vx, vy in visited:
                if i == vy or abs(vx - x) == abs(vy - i):
                    break
            else:
                visited.append((x, i))
                func(x + 1)
                visited.pop()


func(0)

print(ans)
