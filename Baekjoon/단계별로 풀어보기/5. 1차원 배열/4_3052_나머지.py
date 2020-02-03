count = 0
val = []
for i in range(10):
    val.append(int(input())%42)

# 1. 알고리즘

for i in range(42):
    try:
        if val.index(i) > -1:
            count += 1
    except ValueError:
        pass

print(count)

# 2. 집합 자료형

val = set(val)
print(len(val))