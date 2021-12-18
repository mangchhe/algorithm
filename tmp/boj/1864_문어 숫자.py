words = {
    '-' : 0,
    '\\' : 1,
    '(' : 2,
    '@' : 3,
    '?' : 4,
    '>' : 5,
    '&' : 6,
    '%' : 7,
    '/' : -1
}

while True:
    s = input()
    if s == '#':
        break
    ans = 0
    n = len(s)
    for i in range(n):
        ans += words[s[i]] * (8 ** (n - 1 - i))
    
    print(ans)
