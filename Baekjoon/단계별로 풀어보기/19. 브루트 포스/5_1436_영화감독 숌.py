n = int(input())

title = 665

while n > 0:

    title += 1

    """ sixCnt = 0

    for word in str(title):
        
        if word == '6':
            sixCnt += 1
        else:
            sixCnt = 0
        
        if sixCnt == 3:
            n -= 1
            break """
    
    if '666' in str(title):
        n -= 1

print(title)