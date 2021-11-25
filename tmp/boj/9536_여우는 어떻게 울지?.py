for _ in range(int(input())):
    sounds = {}
    ans = []
    records = input()

    while True:
        record = input().split()
        if len(record) > 3:
            break
        sounds[record[2]] = 1

    for record in records.split():
        if sounds.get(record) != 1:
            ans.append(record)

    print(*ans)

