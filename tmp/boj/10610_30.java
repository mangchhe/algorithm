package problem_21_1_10.삼십번_10610;

import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] nums = br.readLine().toCharArray();
        Arrays.sort(nums);
        if (nums[0] != '0') {
            System.out.println(-1);
            return;
        }
        int total = 0;
        for (int i = 0; i < nums.length; i++) {
            total += nums[i] - '0';
        }
        if (total % 3 != 0) {
            System.out.println(-1);
            return;
        }
        System.out.println(new StringBuilder(String.valueOf(nums)).reverse());
        br.close();
    }
}
