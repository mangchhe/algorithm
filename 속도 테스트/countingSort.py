""" 
    제목 : 계수 정렬 vs Counter 속도 비교
    작성일 : 20/10/05
    결과 : 속도 : 계수정렬 < Counter
"""

import random
import time
from collections import Counter
import copy

""" 계수 정렬 """

array = [random.randint(0, 9999) for i in range(1000000)]
array2 = copy.copy(array)

start = time.time()

count = [0] * 1000000

for i in range(1000000):
    count[array[i]] += 1

print(time.time() - start)

""" Counter """

start = time.time()

array2 = Counter(array2)

print(time.time() - start)