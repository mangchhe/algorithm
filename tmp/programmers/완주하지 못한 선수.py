def solution(participant, completion):
    names = {}
    hashTotal = 0
    
    for p in participant:
        names[hash(p)] = p
        hashTotal += hash(p)
        
    for c in completion:
        hashTotal -= hash(c)
        
    return names[hashTotal]
