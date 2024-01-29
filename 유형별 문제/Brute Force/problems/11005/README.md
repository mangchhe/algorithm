```java
private static void problem11005() {
    Scanner sc = new Scanner(System.in);

    List<String> replaceText = new ArrayList<>(List.of("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"));
    for(int i=0;i<26;i++) {
        replaceText.add(String.valueOf((char) (i + 65)));
    }

    String[] input = sc.nextLine().split(" ");
    int N = Integer.parseInt(input[0]);
    int B = Integer.parseInt(input[1]);

    System.out.println(cycle(N, B, replaceText));
}

private static String cycle(int value, int mod, List<String> replaceText) {
    if (value < mod) {
        return replaceText.get(value);
    }
    return cycle(value / mod, mod, replaceText) + replaceText.get(value % mod);
}
```