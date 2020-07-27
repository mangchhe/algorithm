'''
날짜 : 7/27
'''

from sys import stdin

hbg = []
side = []

for i in range(3):

    hbg.append(int(stdin.readline()))

for i in range(2):

    side.append(int(stdin.readline()))

print(min(hbg) + min(side) - 50)