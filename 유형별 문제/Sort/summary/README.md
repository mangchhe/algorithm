## 선택 정렬(Selectioin Sort)

- 맨 앞부터 순회하며 가장 작은 값을 찾아서 데이터를 교환하여 앞에서부터 채워나가 정렬한다.

``` python
import random as rd

def selection_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    arr = [rd.randint(1, 50) for _ in range(5)]
    selection_sort(arr)
    print(arr)
```

## 버블 정렬(Bubble Sort)

- 연속되는 두 인덱스를 비교하여 큰 값을 뒤로 넘겨 정렬한다.

``` python
import random as rd

def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == '__main__':
    arr = [rd.randint(1, 50) for _ in range(5)]
    bubble_sort(arr)
    print(arr)
```

## 삽입 정렬(Insertion Sort)

- 2부터 n까지 인덱스를 설정하여 인덱스 앞부분을 순회하며 알맞은 위치에 해당 값을 넣어 정렬한다.

``` python
import random as rd

def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break

if __name__ == '__main__':
    arr = [rd.randint(1, 50) for _ in range(5)]
    insertion_sort(arr)
    print(arr)
```

## 합병 정렬(Merge Sort)

- 정렬할 리스트를 반으로 쪼개나가며 좌측과 우측 리스트를 계속하여 분할한 뒤 리스트 내에서 정렬 후 병합하는 과정으로 정렬한다.

## 퀵 정렬(Quick Sort)

- pivot을 선정하여 pivot 기준으로 좌측과 우측을 나누어 pivot보다 작은 값은 왼쪽, pivot보다 큰 값은 오른쪽으로 재배치하여 계속하여 분할하여 정렬한다.

``` python
import random as rd

def quick_sort_python(arr):
    if len(arr) <= 1:
        return arr

    l, r = [], []
    pivot = arr[0]

    for i in arr[1:]:
        if pivot >= i:
            l.append(i)
        else:
            r.append(i)

    return quick_sort_python(l) + [pivot] + quick_sort_python(r)

def quick_sort_general(arr, start, end):
    if start >= end: return
    pivot = start
    l, r = start + 1, end

    while l <= r:
        while l <= end and arr[l] <= arr[pivot]:
            l += 1
        while r > start and arr[r] >= arr[pivot]:
            r -= 1

        if l <= r:
            arr[l], arr[r] = arr[r], arr[l]
        else:
            arr[pivot], arr[r] = arr[r], arr[pivot]

    quick_sort_general(arr, start, r - 1)
    quick_sort_general(arr, r + 1, end)

if __name__ == '__main__':

    arr = [rd.randint(1, 50) for _ in range(5)]
    print(quick_sort_python(arr))

    arr = [rd.randint(1, 50) for _ in range(5)]
    quick_sort_general(arr, 0, len(arr) - 1)
    print(arr)
```

## 힙 정렬(Heap Sort)

- 힙 자료구조로 만들어졌으며 값을 추가하거나 삭제하였을 때 부모 노드와 비교하여 위치를 찾아 정렬시킨다.
