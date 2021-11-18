words = {'q' : (0, 0), 'w' : (0, 1), 'e' : (0, 2), 'r' : (0, 3), 't' : (0, 4), 'y' : (0, 5), 'u' : (0, 6), 'i' : (0, 7), 'o' : (0, 8), 'p' : (0, 9), 'a' : (1, 0), 's' : (1, 1), 'd' : (1, 2), 'f' : (1, 3), 'g' : (1, 4), 'h' : (1, 5), 'j' : (1, 6), 'k' : (1, 7), 'l' : (1, 8), 'z' : (2, 0), 'x' : (2, 1), 'c' : (2, 2), 'v' : (2, 3), 'b' : (2, 4), 'n' : (2, 5), 'm' : (2, 6)}

l, r = input().split()
l, r = words[l], words[r]
ans = 0

for i in list(input()):
    x, y = words[i][0], words[i][1]
    lDis = abs(l[0] - x) + abs(l[1] - y)
    rDis = abs(r[0] - x) + abs(r[1] - y)
    if (x == 0 and y < 5) or (x == 1 and y < 5) or (x == 2 and y < 4):
        l = (x, y)
        ans += lDis + 1
    else:
        r = (x, y)
        ans += rDis + 1

print(ans)

