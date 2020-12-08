package study;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class ProblemSort3 {

    static final int max = 10001;

    public static void main(String[] args) {

        try {

            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringBuilder sb = new StringBuilder();

            int[] data = new int[max];
            int n = Integer.parseInt(br.readLine());

            for (int i = 0; i < n; i++) {
                data[Integer.parseInt(br.readLine())] += 1;
            }

            for (int i = 0; i < max; i++) {
                for (int j = 0; j < data[i]; j++) {
                    sb.append(i+"\n");
                }
            }

            System.out.println(sb);

        }
        catch (Exception e){}
    }
}
