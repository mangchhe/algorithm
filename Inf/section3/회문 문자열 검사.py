import sys

# sys.stdin = open('input.txt', 'rt')

# def reverse(txt):
#     result = ''
#     for t in txt:
#         result = t + result
#     return result

# for i in range(int(input())):
#     txt = input()
#     if txt.upper() == reverse(txt).upper():
#         print('#{} {}'.format(i+1, 'YES'))
#     else:
#         print('#{} {}'.format(i+1, 'NO'))

for i in range(int(input())):
    txt = input()
    if txt.upper() == txt[::-1].upper():
        print('#{} {}'.format(i+1, 'YES'))
    else:
        print('#{} {}'.format(i+1, 'NO'))