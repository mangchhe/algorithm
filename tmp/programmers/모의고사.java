package programmers.모의고사;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        solution(new int[]{1, 2, 3, 4, 5, 3, 2, 1});
    }
    public static int[] solution(int[] answers) {
        List<Integer> ans = new ArrayList<>();
        int[] persons = new int[3];
        int[][] person_num = {
                {1, 2, 3, 4, 5},
                {2, 1, 2, 3, 2, 4, 2, 5},
                {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}
        };

        for (int i = 0; i < answers.length; i++) {
            if (person_num[0][i % person_num[0].length] == answers[i]) {
                persons[0]++;
            }
            if (person_num[1][i % person_num[1].length] == answers[i]) {
                persons[1]++;
            }
            if (person_num[2][i % person_num[2].length] == answers[i]) {
                persons[2]++;
            }
        }

        int max = Integer.MIN_VALUE;
        for (int i = 0; i < 3; i++) {
            max = Math.max(max, persons[i]);
        }

        for (int i = 0; i < 3; i++) {
            if (max == persons[i])
                ans.add(i);
        }

        return ans.stream().mapToInt(x -> x + 1).toArray();
    }
}
