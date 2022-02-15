input = __import__("sys").stdin.readline

op = []
ans = []

for i in list(input().rstrip()):

    if i.isalpha():
        ans += i
    else:
        if i == "(":
            op.append("(")
        elif i == ")":
            while op and op[-1] != "(":
                ans += op.pop()
            op.pop()
        elif i in ["*", "/"]:
            while op and op[-1] in ["*", "/"]:
                ans += op.pop()
            op.append(i)
        elif i in ["+", "-"]:
            while op and op[-1] != "(":
                ans += op.pop()
            op.append(i)

while op:
    ans += op.pop()

print("".join(ans))
