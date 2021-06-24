input = __import__("sys").stdin.readline

poli = input().rstrip()
i = 0

while True:
    if i > len(poli):
        break

    if poli[i : i + 4] == "XXXX":
        i = i + 4
        poli = poli.replace("X", "A", 4)
    elif poli[i : i + 2] == "XX":
        i = i + 2
        poli = poli.replace("X", "B", 2)
    elif poli[i] == ".":
        i = i + 1
    else:
        poli = -1
        break

print(poli)
