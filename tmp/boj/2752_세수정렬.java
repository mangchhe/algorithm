package problem_21_1_10.세수정렬_2752;

import java.io.*;
import java.util.*;

public class Main {

    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        String[] in = br.readLine().split(" ");
        int a = Integer.parseInt(in[0]);
        int b = Integer.parseInt(in[1]);
        int c = Integer.parseInt(in[2]);
        List<Integer> arr = Arrays.asList(a, b, c);
        arr.sort((o1, o2) -> o1 - o2);
        arr.stream().forEach(x -> System.out.print(x + " "));
    }
}
