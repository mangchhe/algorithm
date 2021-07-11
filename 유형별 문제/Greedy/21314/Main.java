import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static StringBuilder min_ans;
    static StringBuilder max_ans;
    static String s;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        min_ans = new StringBuilder("");
        max_ans = new StringBuilder("");

        s = br.readLine();

        int m = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'M') m++;
            else{
                max_ans.append("5");
                for (int j = 0; j < m; j++) {
                    max_ans.append("0");
                }
                if (m != 0) {
                    min_ans.append("1");
                    for (int j = 0; j < m - 1; j++) {
                        min_ans.append("0");
                    }
                }
                min_ans.append("5");
                m = 0;
            }
        }

        if (m != 0) {
            for (int i = 0; i < m; i++) {
                max_ans.append("1");
            }
            min_ans.append("1");
            for (int i = 0; i < m - 1; i++) {
                min_ans.append("0");
            }
        }

        System.out.println(max_ans);
        System.out.println(min_ans);

    }
}
