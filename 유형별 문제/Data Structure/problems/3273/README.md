```java
public static void problem3273() {
    Scanner sc = new Scanner(System.in);
    int ret = 0;
    int N = Integer.parseInt(sc.nextLine());
    int[] nums = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
    int X = Integer.parseInt(sc.nextLine());

    boolean[] isNum = new boolean[1000001];
    for (int num : nums) {
        isNum[num] = true;
    }

    for (int num : nums) {
        if (X - num <= 0 || X - num >= 1000000) {
            continue;
        }
        if(X - num > num && isNum[X - num]) {
            ret++;
        }
    }

    System.out.println(ret);
}
```