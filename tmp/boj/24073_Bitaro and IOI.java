package problem_21_1_11.Bitaro_and_IOI_24073;

import java.io.*;

public class Main {

    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static int N;
    static char[] s;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());
        s = br.readLine().toCharArray();
        int cnt = 0;
        boolean isI = true;
        String ans = "No";
        for (int i = 0; i < N; i++) {
            if (isI && s[i] == 'I') {
                cnt += 1;
                isI = false;
            }
            else if (!isI && s[i] == 'O') {
                cnt += 1;
                isI = true;
            }
            if (cnt == 3) {
                ans = "Yes";
                break;
            }
        }
        System.out.println(ans);
    }
}
