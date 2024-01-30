```java
private static void problem3058() {
    Scanner sc = new Scanner(System.in);
    int N = Integer.parseInt(sc.nextLine());

    for(int i=0;i<N;i++) {
        int[] intArray = Arrays.stream(sc.nextLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        int min = Integer.MAX_VALUE;
        int sum = 0;
        for (int val : intArray) {
            if (val % 2 == 0) {
                min = Math.min(min, val);
                sum += val;
            }
        }
        System.out.println(sum + " " + min);
    }
}
```