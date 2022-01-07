package problem_21_1_7.효율적인_해킹_1325;

import java.io.*;
import java.util.*;

public class Main {

    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;

    static int N;
    static int M;
    static List<Integer>[] vertex;
    static boolean[] visited = new boolean[10001];
    static int[] graph = new int[10001];
    static int[] res = new int[10001];

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        vertex = new ArrayList[N + 1];
        for (int i = 1; i <= N; i++) {
            vertex[i] = new ArrayList<>();
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            vertex[a].add(b);
        }

        for (int i = 1; i < N + 1; i++) {
            visited = new boolean[N + 1];
            if (!visited[i])
                bfs(i);
        }

        int max = Integer.MIN_VALUE;
        for (int i = 1; i < N + 1; i++) {
            max = Math.max(max, res[i]);
        }

        for (int i = 1; i < N + 1; i++) {
            if (max == res[i]) {
                bw.write(i + " ");
            }
        }
        bw.flush();
        bw.close();
        br.close();
    }

    static void bfs(int start) {
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        visited[start] = true;
        while (!q.isEmpty()) {
            int now = q.poll();
            for (int next : vertex[now]) {
                if (visited[next])
                    continue;
                visited[next] = true;
                res[next]++;
                q.add(next);
            }
        }
    }
}
