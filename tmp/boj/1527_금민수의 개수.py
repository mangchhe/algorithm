def traverse(n):
    global ans
    if n > B:
        return

    if n >= A and n <= B:
        ans += 1

    traverse(n * 10 + 4)
    traverse(n * 10 + 7)

A, B = map(int, input().split())
ans = 0

traverse(4)
traverse(7)

print(ans)
