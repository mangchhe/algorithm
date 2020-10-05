""" 
    제목 : sorted(reverse) vs reversed vs reverse
    작성일 : 20/10/05
    결과 : reverse > reversed > sorted(reverse)
"""

import random
import time

array = [random.randint(1, 1000000) for i in range(1000000)]

""" sorted(reverse) """

start = time.time()

a = sorted(array, reverse=True)

print(time.time() - start)

""" reversed """

start = time.time()

b = reversed(array)

print(time.time() - start)

""" reverse """

start = time.time()

array.reverse()

print(time.time() - start)