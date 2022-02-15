import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int N;
    static int[] preList;
    static int[] inList;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            N = Integer.parseInt(br.readLine());
            preList = new int[N];
            inList = new int[N];

            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                preList[j] = Integer.parseInt(st.nextToken());
            }

            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                inList[j] = Integer.parseInt(st.nextToken());
            }

            solve(0, 0, N);

            System.out.println();

        }
    }

    static void solve(int root, int l, int r){

        for (int k = l; k < r; k++) {
            if (preList[root] == inList[k]) {
                solve(root + 1, l, k);
                solve(root + 1 + k - l, k + 1, r);
                System.out.print(preList[root] + " ");
            }
        }
    }
}
