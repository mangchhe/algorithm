```java
private static int problem1236() {
    Scanner sc = new Scanner(System.in);
    String[] input = sc.nextLine().split(" ");
    int n = Integer.parseInt(input[0]);
    int m = Integer.parseInt(input[1]);

    boolean[][] arr = new boolean[n][m];
    for (int i = 0; i < n; i++) {
        String guards = sc.nextLine();
        for (int j = 0; j < m; j++) {
            arr[i][j] = guards.charAt(j) != '.';
        }
    }

    int rowGuard = 0;
    int columnGuard = 0;
    for (int i = 0; i < n; i++) {
        rowGuard++;
        for (int j = 0; j < m; j++) {
            if (arr[i][j]) {
                rowGuard--;
                break;
            }
        }
    }

    for (int i = 0; i < m; i++) {
        columnGuard++;
        for (int j = 0; j < n; j++) {
            if (arr[j][i]) {
                columnGuard--;
                break;
            }
        }
    }

    return Math.max(rowGuard, columnGuard);
}
```