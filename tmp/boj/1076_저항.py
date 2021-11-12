resistance = {
        'black' : ('0', 1),
        'brown' : ('1', 10),
        'red' : ('2', 10 ** 2),
        'orange' : ('3', 10 ** 3),
        'yellow' : ('4', 10 ** 4),
        'green' : ('5', 10 ** 5),
        'blue' : ('6', 10 ** 6),
        'violet' : ('7', 10 ** 7),
        'grey' : ('8', 10 ** 8),
        'white' : ('9', 10 ** 9)
}

print(int(resistance[input()][0] + resistance[input()][0]) * resistance[input()][1])
