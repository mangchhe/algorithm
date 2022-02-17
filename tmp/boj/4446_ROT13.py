vowels = 'aiyeou'
consonants = 'bkxznhdcwgpvjqtsrlmf'
ans = ''
while True:
    try:
        text = input()
        for t in text:
            lowerT = t.lower()
            if lowerT in vowels:
                tmp = vowels[(vowels.index(lowerT) + 3) % 6]
                ans += tmp.upper() if t.isupper() else tmp
            elif lowerT in consonants:
                tmp = consonants[(consonants.index(lowerT) + 10) % 20]
                ans += tmp.upper() if t.isupper() else tmp
            else:
                ans += t

        ans += '\n'
    except:
        break

print(ans)
