package problem_21_1_12.오르막_수_11057;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] dp = new int[10];
        Arrays.fill(dp, 1);
        for (int i = 0; i < N; i++) {
            for (int j = 1; j < 10; j++) {
                dp[j] = (dp[j] + dp[j - 1]) % 10007;
            }
        }
        System.out.println(dp[9]);
    }
}
