input = __import__("sys").stdin.readline

s = input().rstrip()

min_ans = ""
max_ans = ""

m = 0
for i in s:
    if i == "M":
        m += 1
    else:
        max_ans += "5" + "0" * m
        if m != 0:
            min_ans += "1" + "0" * (m - 1)
        min_ans += "5"
        m = 0
else:
    if m != 0:
        max_ans += "1" * m
        min_ans += "1" + "0" * (m - 1)


print(int(max_ans))
print(int(min_ans))
