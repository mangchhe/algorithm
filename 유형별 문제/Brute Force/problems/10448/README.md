```java
private static void problem10448() {
        Scanner sc = new Scanner(System.in);
    int N = Integer.parseInt(sc.nextLine());

    List<Integer> nums = new ArrayList<>();
    int num = 1;
    for (int i = 2; num < 1001; i++) {
        nums.add(num);
        num += i;
    }

    boolean[] isTriangular = new boolean[1001];
    for (int j = 0; j < nums.size(); j++) {
        for (int k = j; k < nums.size(); k++) {
            for (int l = k; l < nums.size(); l++) {
                int total = nums.get(j) + nums.get(k) + nums.get(l);
                if (total > 1000) {
                    continue;
                }
                isTriangular[total] = true;
            }
        }
    }

    for (int i = 0; i < N; i++) {
        int K = Integer.parseInt(sc.nextLine());
        System.out.println(isTriangular[K] ? 1 : 0);
    }
}
```