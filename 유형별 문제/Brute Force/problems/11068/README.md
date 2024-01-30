```java
private static void problem11068() {
    Scanner sc = new Scanner(System.in);
    int N = Integer.parseInt(sc.nextLine());

    for (int i=0;i<N;i++) {
        int n = Integer.parseInt(sc.nextLine());
        boolean palindrome = false;
        for(int j=2;j<65;j++) {
            palindrome = true;
            List<Integer> mods = new ArrayList<>();
            cycle(n, j, mods);
            for (int k=0;k<mods.size();k++) {
                if (!mods.get(k).equals(mods.get(mods.size() - k - 1))) palindrome = false;
            }
            if (palindrome) {
                break;
            }
        }
        System.out.println(palindrome ? 1 : 0);
    }
}

private static void cycle(int value, int form, List<Integer> mods) {
    if (value < form) {
        mods.add(value);
        return;
    }
    mods.add(value % form);
    cycle(value / form, form, mods);
}
```