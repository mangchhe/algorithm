def solution(enroll, referral, seller, amount):

    enrollDic = {}
    resultDic = {}

    for i in range(len(enroll)):
        resultDic[enroll[i]] = 0
        enrollDic[enroll[i]] = referral[i]

    for i in range(len(seller)):
        money = amount[i] * 100
        name = seller[i]
        while True:
            if enrollDic[name] != '-':
                if money // 10 > 0:
                    resultDic[name] += money - (money // 10)
                else:
                    resultDic[name] += money
                    break
            else:
                if money // 10 > 0:
                    resultDic[name] += money - (money // 10)
                else:
                    resultDic[name] += money
                break

            money = money // 10
            name = enrollDic[name]

    return list(resultDic.values())


print(
    solution(
        ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
        ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
        ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))
