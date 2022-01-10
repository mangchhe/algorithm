package problem_21_1_10.DFS와_BFS_1260;

import java.util.*;
import java.io.*;

public class Main {

    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static String[] in;
    static Map<Integer, TreeSet<Integer>> graph = new HashMap<>();
    static int N;
    static int M;
    static int V;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        in = br.readLine().split(" ");
        N = Integer.parseInt(in[0]);
        M = Integer.parseInt(in[1]);
        V = Integer.parseInt(in[2]);

        for (int i = 0; i < M; i++) {
            in = br.readLine().split(" ");
            int a = Integer.parseInt(in[0]);
            int b = Integer.parseInt(in[1]);
            graph.put(a, graph.getOrDefault(a, new TreeSet<>()));
            graph.get(a).add(b);
            graph.put(b, graph.getOrDefault(b, new TreeSet<>()));
            graph.get(b).add(a);
        }

        StringBuilder ans = new StringBuilder("");
        visited = new boolean[N + 1];
        dfs(V, ans);
        System.out.println(ans);
        visited = new boolean[N + 1];
        bfs(V);
    }

    static void dfs(int now, StringBuilder ans) {
        if (visited[now])
            return;
        visited[now] = true;
        ans.append(now).append(" ");
        for (int v: graph.getOrDefault(now, new TreeSet<>())) {
            dfs(v, ans);
        }
    }

    static void bfs(int start) {
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        StringBuilder ans = new StringBuilder("");

        while (!q.isEmpty()) {
            int now = q.poll();
            if (visited[now])
                continue;
            visited[now] = true;
            ans.append(now).append(" ");
            q.addAll(graph.getOrDefault(now, new TreeSet<>()));
        }
        System.out.println(ans);
    }
}
