package problem_21_1_6.윷놀이_2490;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    final static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int cnt = 0;

        for (int i = 0; i < 3; i++) {
            st = new StringTokenizer(br.readLine());
            cnt = 0;
            for (int j = 0; j < 4; j++) {
                cnt += Integer.parseInt(st.nextToken());
            }
            if (cnt == 4)
                System.out.println('E');
            else
                System.out.println((char)(68 - cnt));
        }
    }
}
