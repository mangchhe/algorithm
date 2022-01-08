package problem_21_1_8.최솟값_10868;

import java.io.*;

public class Main {

    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int N;
    static int M;
    static int[] graph;
    static int[] arr;
    static String[] in;

    public static void main(String[] args) throws IOException {
        in = br.readLine().split(" ");
        N = Integer.parseInt(in[0]);
        M = Integer.parseInt(in[1]);
        arr = new int[N];
        graph = new int[N * 4];

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        init(0, N - 1, 1);

        StringBuilder ans = new StringBuilder("");

        for (int i = 0; i < M; i++) {
            in = br.readLine().split(" ");
            int s = Integer.parseInt(in[0]);
            int e = Integer.parseInt(in[1]);
            ans.append(findMinVal(0, N - 1, 1, s - 1, e - 1) + "\n");
        }

        System.out.println(ans);
    }

    static int init(int start, int end, int node) {
        if (start == end)
            return graph[node] = arr[start];
        int mid = (start + end) / 2;

        return graph[node] = Math.min(init(start, mid, node * 2), init(mid + 1, end, node * 2 + 1));
    }

    static int findMinVal(int start, int end, int node, int left, int right) {
        if (start > right || end < left)
            return Integer.MAX_VALUE;
        if (start >= left && end <= right)
            return graph[node];
        int mid = (start + end) / 2;

        return Math.min(findMinVal(start, mid, node * 2, left, right), findMinVal(mid + 1, end, node * 2 + 1, left, right));
    }
}
