N = int(input())
divisors = sorted(map(int, input().split()))

print(divisors[-1] * divisors[0])
