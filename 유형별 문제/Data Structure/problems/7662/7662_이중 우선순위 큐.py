from collections import defaultdict
import heapq

input = __import__("sys").stdin.readline

for _ in range(int(input())):

    ans = []
    nums = defaultdict(int)
    h1 = []
    h2 = []

    for i in range(int(input())):

        o, n = input().split()
        n = int(n)

        if o == "I":
            heapq.heappush(h1, n)
            heapq.heappush(h2, -n)
            nums[n] += 1
        else:
            if n == -1:
                while h1:
                    tmp = heapq.heappop(h1)
                    if nums[tmp] == 0:
                        continue
                    elif nums[tmp] == 1:
                        nums[tmp] -= 1
                        break
                    else:
                        heapq.heappush(h1, tmp)
                        nums[tmp] -= 1
                        break
            else:
                while h2:
                    tmp = -heapq.heappop(h2)
                    if nums[tmp] == 0:
                        continue
                    elif nums[tmp] == 1:
                        nums[tmp] -= 1
                        break
                    else:
                        heapq.heappush(h2, -tmp)
                        nums[tmp] -= 1
                        break

    for i in range(len(h1)):
        if nums[h1[i]] != 0:
            ans.append(h1[i])

    ans.sort()

    if ans:
        print("{} {}".format(ans[-1], ans[0]))
    else:
        print("EMPTY")
