```java
private static void problem10250() {
    Scanner sc = new Scanner(System.in);

    int N = Integer.parseInt(sc.nextLine());

    for(int i=0;i<N;i++) {
        String[] input = sc.nextLine().split(" ");
        int H = Integer.parseInt(input[0]);
        int P = Integer.parseInt(input[2]);

        int prefix = P % H == 0 ? H : P % H;
        int suffix = P % H == 0 ? P / H  : P / H + 1;
        System.out.println(prefix + ((suffix < 10) ? "0" + suffix : String.valueOf(suffix)));
    }
}
```