import heapq

input = __import__("sys").stdin.readline

h1 = []
h2 = []
problem_seq = {}
problems = {}

for _ in range(int(input())):
    a, b = map(int, input().split())
    heapq.heappush(h1, (b, a))
    heapq.heappush(h2, (-b, -a))
    problem_seq[(b, a)] = 1
    problems[a] = b

for _ in range(int(input())):
    com = input().rstrip().split()
    if com[0] == "add":
        com[1], com[2] = int(com[1]), int(com[2])
        heapq.heappush(h1, (com[2], com[1]))
        heapq.heappush(h2, (-com[2], -com[1]))
        problems[com[1]] = com[2]
        problem_seq[(com[2], com[1])] = 1

    elif com[0] == "solved":
        com[1] = int(com[1])
        problem_seq[(problems[com[1]], com[1])] = 0

    elif com[0] == "recommend":
        if com[1] == "-1":
            while h1:
                n = heapq.heappop(h1)
                if problem_seq[n] == 0:
                    continue
                else:
                    print(n[1])
                    heapq.heappush(h1, n)
                    break
        elif com[1] == "1":
            while h2:
                n = heapq.heappop(h2)
                n = (-n[0], -n[1])
                if problem_seq[n] == 0:
                    continue
                else:
                    print(n[1])
                    heapq.heappush(h2, (-n[0], -n[1]))
                    break
