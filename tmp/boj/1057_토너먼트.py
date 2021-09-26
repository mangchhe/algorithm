# https://www.acmicpc.net/problem/1057

input = __import__('sys').stdin.readline

N, kim, im = map(int, input().split())
rounds = 1

if kim > im:
    kim, im = im, kim

while True:
    if (kim == 1 or kim % 2 == 1) and im - kim == 1:
        print(rounds)
        break
    kim = round(kim / 2 + .1)
    im = round(im / 2 + .1)
    rounds += 1
