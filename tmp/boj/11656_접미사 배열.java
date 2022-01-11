package problem_21_1_11.접미사_배열_11656;

import java.util.*;
import java.io.*;

public class Main {

    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static String s;
    static String[] suffix;

    public static void main(String[] args) throws IOException {
        s = br.readLine();
        suffix = new String[s.length()];
        for (int i = 0; i < s.length(); i++) {
            suffix[i] = s.substring(i);
        }
        Arrays.sort(suffix);
        for (int i = 0; i < suffix.length; i++) {
            System.out.println(suffix[i]);
        }
    }
}
