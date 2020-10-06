""" 
    제목 : sorted(reverse) vs reversed vs reverse
    작성일 : 20/10/05
    수정일 : 20/10/06
    reverse > reversed > sorted(reverse) X
    reverse 와 sorted(reverse) 는 전혀 다른 기능이여서 속도 비교가 불가능
    reverse : 단순히 리스트를 뒤집는 함수
    sorted(reverse) : 내림차순으로 리스트를 정렬하는 함수    
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