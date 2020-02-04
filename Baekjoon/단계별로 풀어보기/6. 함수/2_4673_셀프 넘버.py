# 셀프넘버
# N = 15
# 15 + 1 + 5 = 21
# 21 + 2 + 1 = 24
# 21은 24의 생성자이다.
# 생성자가 존재하지 않는 숫자를 셀프넘버라고 부른다.

def solve():
    N = []
    N2 = set(range(10000))
    for i in range(10000):
        val = i
        while i > 0:
            val += i % 10
            i //= 10
        if val > 10000:
            pass
        else:
            N.append(val)

    N = set(N)
    result = list(N2 - N)
    result.sort()

    return result

result = solve()

for i in result:
    print(i)