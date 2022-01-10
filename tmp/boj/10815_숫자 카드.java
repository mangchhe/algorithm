package problem_21_1_10.숫자_카드_10815;

import java.io.*;
import java.util.*;

public class Main {

    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static int N;
    static int M;
    static int[] arr;
    static StringTokenizer st;
    static StringBuilder ans = new StringBuilder("");

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());
        arr = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);
        M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            if (binary_search(0, N - 1, Integer.parseInt(st.nextToken()))) {
                ans.append(1).append(" ");
            } else {
                ans.append(0).append(" ");
            }
        }
        System.out.println(ans);
    }

    static boolean binary_search(int start, int end, int target) {
        while (start <= end) {
            int mid = (start + end) / 2;

            if (arr[mid] == target)
                return true;
            else if (arr[mid] > target) {
                end = mid - 1;
            }
            else if (arr[mid] < target) {
                start = mid + 1;
            }
        }
        return false;
    }
}
