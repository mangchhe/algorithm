package problem_21_1_9.구간_곱_구하기_11505;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static final int MOD = 1000000007;
    static String[] in;
    static int N;
    static int M;
    static int K;
    static long[] arr;
    static long[] graph;

    public static void main(String[] args) throws IOException {
        in = br.readLine().split(" ");
        N = Integer.parseInt(in[0]);
        M = Integer.parseInt(in[1]);
        K = Integer.parseInt(in[2]);
        arr = new long[N];
        graph = new long[N * 4];
        StringBuilder ans = new StringBuilder("");

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        init(0, N - 1, 1);

        for (int i = 0; i < M + K; i ++) {
            in = br.readLine().split(" ");
            int c = Integer.parseInt(in[0]);
            int a = Integer.parseInt(in[1]);
            int b = Integer.parseInt(in[2]);
            switch (c) {
                case 1:
                    update(0, N - 1, 1, a - 1, b);
                    break;
                case 2:
                    ans.append(mul(0, N - 1, 1, a - 1, b - 1)).append("\n");
                    break;
            }
        }
        System.out.println(ans);
    }

    static long init(int start, int end, int node) {
        if (start == end) {
            return graph[node] = arr[start];
        }
        int mid = (start + end) / 2;
        return graph[node] = init(start, mid, node * 2) * init(mid + 1, end, node * 2 + 1) % MOD;
    }

    static long mul(int start, int end, int node, int left, int right) {
        if (start > right || end < left) {
            return 1;
        }
        if (start >= left && end <= right) {
            return graph[node];
        }
        int mid = (start + end) / 2;
        return mul(start, mid, node * 2, left, right) * mul(mid + 1, end, node * 2 + 1, left, right) % MOD;
    }

    static long update(int start, int end, int node, int idx, int val) {
        if (start > idx || end < idx) {
            return graph[node];
        }
        if (start == end) {
            return graph[node] = val;
        }
        int mid = (start + end) / 2;
        return graph[node] = update(start, mid, node * 2, idx, val) * update(mid + 1, end, node * 2 + 1, idx, val) % MOD;
    }

}
