```java
public static void problem10989() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    int N = Integer.parseInt(br.readLine());

    int[] numCnt = new int[10001];

    for (int i=0;i<N;i++) {
        numCnt[Integer.parseInt(br.readLine())]++;
    }

    for (int i = 0; i < numCnt.length; i++) {
        if (N == 0) {
            break;
        }
        for (int j = 0; j < numCnt[i]; j++) {
            bw.write(i + "\n");
            N--;
        }
    }

    bw.flush();
}
```