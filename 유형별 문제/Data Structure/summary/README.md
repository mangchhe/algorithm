## 자료 구조란?

데이터를 원하는 규칙이나 목적에 맞게 저장하기 위한 구조

### 스택(Stack)

- 나중에 넣은 데이터가 먼저 나오는 후입 선출(LIFO) 구조를 가진다.

![stack](https://user-images.githubusercontent.com/50051656/123516559-aafdbb00-d6d7-11eb-8658-4a5095cacfc9.JPG)

### 큐(Queue)

- 먼저 넣은 데이터가 먼저 나오는 선입 선출(FIFO) 구조를 가진다.

![queue](https://user-images.githubusercontent.com/50051656/123516561-ac2ee800-d6d7-11eb-8866-f3533ecf05ea.JPG)

### 덱(Deque)

- 양쪽 모두 넣고 빼는 것이 가능한 구조를 가진다.

![deque](https://user-images.githubusercontent.com/50051656/123516562-ac2ee800-d6d7-11eb-9a46-f408118ccc88.JPG)

### 우선순위 큐(Priority Queue)

- 들어간 순서에 상관없이 우선순위가 높은 데이터가 먼저 나오는 것을 말한다.
- 힙이라는 자료구조를 가지고 구현된다.

### 힙(Heap)

- 최댓값과 최솟값을 찾아내는 연산을 빠르게 하기 위해 고안된 완전이진트리(두 개의 노드를 가지는 왼쪽부터 차례대로 채워진 트리)이다.
- 부모 노드와 자식 노드 사이에 대소관계가 성립한다.
- 힙의 종류에는 최대 힙과 최소 힙이 있다.

![heap](https://user-images.githubusercontent.com/50051656/123549074-63903100-d7a2-11eb-9d58-3d81ecb448a2.JPG)

- 최대 힙
  - 부모 노드의 키 값이 자식 노드의 키 값보다 크거나 같은 완전 이진 트리
- 최소 힙
  - 부모 노드의 키 값이 자식 노드의 키 값보다 작거나 같은 완전 이진 트리