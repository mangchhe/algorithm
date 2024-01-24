## Java.lang.String

- Java.lang package 에서 제공하는 Java 문자열 클래스
- 표준 라이브러리이므로 별도의 import 없이 사용 가능

```java
String strLiteral = "Hello World!";
String strObject = new String("Hello World!");
```

- **immutable object**
- 일부 값 변경은 불가능하지만 아래와 같은 방법으로 변경이 가능하다.

```java
// 1
strLiteral = "Hello World!2";

// 2
char[] charArray = strLiteral.toCharArray();
charArray[3] = 'W';
String strLiteral2 = new String(charArray);

// 3
String strLiteral3 = strLiteral.substring(0, 4) + "w" + strLiteral.substring(5, 7);

// 4
using StringBuilder
```

- **== 비교**
- primitive type은 상관없지만 object 타입의 경우 주소 값을 비교하기 때문에 주의해야 한다.

```java
System.out.println(strLiteral == strObject); // false
```

- **Constant String Pool**
- 리터럴 값으로 생성한 아래 두 값은 이미 값이 존재하기 때문에 상수풀에 동일한 주소 값을 가르키게 된다.
- 하지만, new keyword를 이용해 생성한 경우 heap에 새로운 주소를 가르키고 저장되기 때문에 서로 다른 주소 값을 가르키게 된다.

```java
String strLiteral = "Hello World!";
String strLiteral2 = "Hello World!";
String strObject = new String("Hello World!");
String strObject2 = new String("Hello World!");
```

- equals()
- 비교할 때 이미 오버라이딩 되어 있는 equals를 이용해서 값을 비교하는 것이 좋다.

| method name                    | Big-O    | Description                       |
|--------------------------------|----------|-----------------------------------|
| chatAt                         | O(1)     |                                   |
| length                         | O(1)     |                                   |
| equals                         | O(N)     |                                   |
| equalsIgnoreCase               | O(N)     |                                   |
| compareTo                      |          | 사전 순으로 비교한 결과. 크면 1, 동일 0, 작으면 -1 |
| toCharArray                    | O(N)     |                                   |
| toLowerCase                    | O(N)     |                                   |
| toUpperCase                    | O(N)     |                                   |
| contains                       | O(N)     |                                   |
| replace                        | O(N)     |                                   |
| replaceAll                     |          |                                   |
| split(String regex)            |          |                                   |
| substring                      |          |                                   |
| indexOf(int ch, int fromIndex) | O(N * M) |                                   |