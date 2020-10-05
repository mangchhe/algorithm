"""
    주제 : sort vs sorted
    작성일 : 20/10/05
    결과 : 성능 동일
"""

import random
import time
import copy

array = [random.randint(1, 1000000) for i in range(1000000)]
array2 = copy.copy(array)

""" sorted """

start = time.time()

sorted(array)

print(time.time() - start)

""" sort """

start = time.time()

array.sort()

print(time.time() - start)