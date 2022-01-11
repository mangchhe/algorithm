package problem_21_1_11.연결_요소의_개수_11724;

import java.util.*;
import java.io.*;

public class Main {

    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static int N;
    static int M;
    static String[] in;
    static Map<Integer, ArrayList<Integer>> graph;
    static boolean[] visited;
    static int ans = 0;

    public static void main(String[] args) throws IOException {
        in = br.readLine().split(" ");
        N = Integer.parseInt(in[0]);
        M = Integer.parseInt(in[1]);
        graph = new HashMap<>();
        visited = new boolean[N + 1];
        for (int i = 1; i < N + 1; i++) {
            graph.put(i, new ArrayList<>());
        }
        for (int i = 0; i < M; i++) {
            in = br.readLine().split(" ");
            int a = Integer.parseInt(in[0]);
            int b = Integer.parseInt(in[1]);
            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        for (int i = 1; i < N + 1; i++) {
            if (!visited[i]) {
                bfs(i);
                ans++;
            }
        }

        System.out.println(ans);
    }

    static void dfs(int now) {
        if (visited[now])
            return;
        visited[now] = true;
        for (int v: graph.get(now)) {
            dfs(v);
        }
    }

    static void bfs(int start) {
        if (visited[start])
            return;
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        while (!q.isEmpty()) {
            int now = q.poll();
            if (visited[now])
                continue;
            visited[now] = true;
            q.addAll(graph.get(now));
        }
    }
}
