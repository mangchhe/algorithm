package aa;

import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

class Main {

    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(stk.nextToken());
        int M = Integer.parseInt(stk.nextToken());
        int[] times = new int[N];
        for (int i = 0; i < N; i++) {
            times[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(times);
        long left = 1;
        long right = (long) times[N - 1] * M;

        while (left < right) {
            long mid = (left + right) / 2;
            long cnt = 0;
            for (int i = 0; i < N; i++) {
                cnt += mid / times[i];
            }
            if (cnt < M) {
                left = mid + 1;
            }else {
                right = mid;
            }
        }

        bw.write(right + "");
        bw.flush();
        bw.close();
    }
}