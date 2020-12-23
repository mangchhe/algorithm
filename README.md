# 알고리즘

백준, 코드업과 같은 다양한 사이트에 있는 알고리즘 문제를 통해 문제 해결 능력 키우기

## 입출력

### Python

``` 
import sys

input = sys.stdin.readline

num = int(input())
```
문제 중 입력을 많이 받을 경우 input()으로 그대로 진행하면 시간 초과에 걸릴 것이다

sys.stdin.readline 을 이용하여 문자를 받아서 사용하는 것으로 입출력의 시간을 줄이는 것이 좋다

### Java

```
BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

int num = Integer.parseInt(bufferedReader.readLine());
```

입력이 많을 경우 Scanner 보다 BufferedReader 사용 추천

## 문자열 다루기

### Python

```
str = ''

for i in range(10):
    str += i
    
print(str)
```

### Java

```
StringBuilder stringBuilder = new StringBuilder();

for (int i = 0; i < 10; i++) {
    stringBuilder.append(i);
}

System.out.println(stringBuilder.toString());
```

String 객체를 이용하여 문자를 붙일 경우 새로운 객체를 생성하므로 효율이 좋지 못하다

StringBuilder를 이용하여 append 메소드로 붙이는 것을 추천
