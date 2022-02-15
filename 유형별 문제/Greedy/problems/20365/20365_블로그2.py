input = __import__("sys").stdin.readline

N = int(input())
problems = list(input().rstrip())

before = "S"
cnt = {"B": 0, "R": 0}

for problem in problems:
    if before != problem:
        cnt[problem] += 1
        before = problem

if cnt["R"] > cnt["B"]:
    print(cnt["B"] + 1)
else:
    print(cnt["R"] + 1)
