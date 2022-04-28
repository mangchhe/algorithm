def dfs(n, _sum, p):
    if _sum > 100:
        return

    if _sum == 100 and len(p) == 7:
        for i in p: print(i)
        exit()

    for i in range(n, 9):
        p.append(dwarf[i])
        dfs(i + 1, _sum + dwarf[i], p)
        p.pop()
    

dwarf = [int(input()) for _ in range(9)]

dfs(0, 0, [])
