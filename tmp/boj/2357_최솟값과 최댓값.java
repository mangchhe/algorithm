package problem_21_1_8.최솟값과_최댓값_2357;

import java.io.*;

public class Main {

    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int N;
    static int M;
    static int[] arr;
    static int[] minGraph;
    static int[] maxGraph;
    static String[] in;

    public static void main(String[] args) throws IOException {
        StringBuilder ans = new StringBuilder("");
        in = br.readLine().split(" ");
        N = Integer.parseInt(in[0]);
        M = Integer.parseInt(in[1]);
        arr = new int[N];
        minGraph = new int[N * 4];
        maxGraph = new int[N * 4];

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        minInit(0, N - 1, 1);
        maxInit(0, N - 1, 1);

        for (int i = 0; i < M; i++) {
           in = br.readLine().split(" ");
           int s = Integer.parseInt(in[0]) - 1;
           int e = Integer.parseInt(in[1]) - 1;
           ans.append(findMinVal(0, N - 1, 1, s, e) + " " + findMaxVal(0, N - 1, 1, s, e) + "\n");
        }

        System.out.println(ans);

    }

    static int minInit(int start, int end, int node) {
        if (start == end) {
            return minGraph[node] = arr[start];
        }
        int mid = (start + end) / 2;

        return minGraph[node] = Math.min(minInit(start, mid, node * 2), minInit(mid + 1, end, node * 2 + 1));
    }

    static int maxInit(int start, int end, int node) {
        if (start == end) {
            return maxGraph[node] = arr[start];
        }
        int mid = (start + end) / 2;

        return maxGraph[node] = Math.max(maxInit(start, mid, node * 2), maxInit(mid + 1, end, node * 2 + 1));
    }

    static int findMinVal(int start, int end, int node, int left, int right) {
        if (left > end || right < start)
            return Integer.MAX_VALUE;
        if (start >= left && end <= right)
            return minGraph[node];
        int mid = (start + end) / 2;

        return Math.min(findMinVal(start, mid, node * 2, left, right), findMinVal(mid + 1, end, node * 2 + 1, left, right));
    }

    static int findMaxVal(int start, int end, int node, int left, int right) {
        if (left > end || right < start)
            return Integer.MIN_VALUE;
        if (start >= left && end <= right)
            return maxGraph[node];
        int mid = (start + end) / 2;

        return Math.max(findMaxVal(start, mid, node * 2, left, right), findMaxVal(mid + 1, end, node * 2 + 1, left, right));
    }
}
