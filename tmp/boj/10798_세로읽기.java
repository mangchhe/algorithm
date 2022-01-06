package problem_21_1_6.세로읽기_10798;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    final static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        char[][] board = new char[15][15];

        for (int i = 0; i < 5; i++) {
            String s = br.readLine();
            for (int j = 0; j < s.length(); j++) {
                board[i][j] = s.charAt(j);
            }
        }

        StringBuilder st = new StringBuilder();

        for (int i = 0; i < 15; i++) {
            for (int j = 0; j < 5; j++) {
                if (board[j][i] != '\u0000') {
                    st.append(board[j][i]);
                }
            }
        }
        System.out.println(st);
    }
}
