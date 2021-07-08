import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static long ans = 0;
    static int N = 0;
    static long[] loss;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        loss = new long[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            loss[i] = Long.parseLong(st.nextToken());
        }
        Arrays.sort(loss);

        ans = loss[N - 1];

        if (N % 2 == 1){
            for (int i = 0; i < N / 2; i++) {
                ans = Math.max(ans, loss[i] + loss[N - i - 2]);
            }
        }else{
            for (int i = 0; i < N / 2; i++) {
                ans = Math.max(ans, loss[i] + loss[N - i - 1]);
            }
        }

        System.out.println(ans);

    }
}
