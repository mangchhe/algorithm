import heapq

input = __import__("sys").stdin.readline

for _ in range(int(input())):
    l = []
    r = []
    ans = []
    cnt = 1

    for i in range(int(input()) // 10 + 1):
        for j in map(int, input().rstrip().split()):

            if len(l) > len(r):
                heapq.heappush(r, j)
            else:
                heapq.heappush(l, -j)

            if l and r:
                if -l[0] > r[0]:
                    l_n = heapq.heappop(l)
                    r_n = heapq.heappop(r)
                    heapq.heappush(l, -r_n)
                    heapq.heappush(r, -l_n)

            if cnt % 2 == 1:
                ans.append(-l[0])
            cnt += 1

    print(len(ans))

    for i in range(len(ans) // 10 + 1):
        print(" ".join(map(str, ans[i * 10 : (i + 1) * 10])))
