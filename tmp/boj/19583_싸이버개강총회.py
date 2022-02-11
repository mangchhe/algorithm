# 방법 1
input = __import__('sys').stdin.readline

def timeToSecond(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m

start, end, liveEnd = map(timeToSecond, input().split())
students = {}

while True:
    try:
        time, name = input().split()
        if timeToSecond(time) <= start:
            students[name] = 1
        elif end <= timeToSecond(time) <= liveEnd:
            if students.get(name):
                students[name] += 1
    except:
        break

print(len(list(filter(lambda x : x > 1, students.values()))))

# 방법2
# 시간 포맷이 필요가 없었음

s, e, l = input().split()
st = {}

while True:
    try:
        t, name = input().split()
        if t <= s:
            st[name] = 1
        elif e <= t <= l:
            if st.get(name):
                st[name] += 1
    except:
        break

print(len(list(filter(lambda x: x > 1, st.values()))))
