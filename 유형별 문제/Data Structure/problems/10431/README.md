```java
private static void problem10431() {
    Scanner sc = new Scanner(System.in);
    int N = Integer.parseInt(sc.nextLine());
    for (int i = 0; i < N; i++) {
        int ret = 0;
        int[] inputs = Arrays.stream(sc.nextLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        for (int j = 1; j < 21; j++) {
            for (int k = j; k > 0; k--) {
                if (inputs[j] < inputs[k]) ret++;
            }
        }
        System.out.printf("%d %d%n", i + 1, ret);
    }
}
```