address = input()
address2 = address.split(":")

cnt = 0
blank = -1

for i in range(len(address2)):
    if address2[i]:
        address2[i] = (4 - len(address2[i])) * '0' + address2[i]
        cnt += 1
    else:
        blank = i


if blank != - 1:
    if address2[blank - 1] == "":
        del address2[blank - 1]
        address2[blank - 1] = ':'.join(['0000'] * (8 - cnt))
    else:
        address2[blank] = ':'.join(['0000'] * (8 - cnt))

print(':'.join(address2))

