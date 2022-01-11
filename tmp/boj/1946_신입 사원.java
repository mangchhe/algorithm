package problem_21_1_11.신입_사원_1946;

import java.util.*;
import java.io.*;

public class Main {

    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static int T;
    static int N;
    static int[] arr;
    static int standard;
    static StringBuilder ans = new StringBuilder();

    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(br.readLine());

        while (T-- > 0) {
            N = Integer.parseInt(br.readLine());
            arr = new int[N + 1];
            int cnt = 1;
            for (int i = 0; i < N; i++) {
                String[] s = br.readLine().split(" ");
                int a = Integer.parseInt(s[0]);
                int b = Integer.parseInt(s[1]);
                if (a == 1) {
                    standard = b;
                }
                arr[a] = b;
            }
            for (int i = 2; i < N + 1; i++) {
                if (standard > arr[i]) {
                    standard = arr[i];
                    cnt++;
                }
            }
            ans.append(cnt).append("\n");
        }
        System.out.println(ans);
    }
}
