package programmers.키패드_누르기;

import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        System.out.println(solution(new int[]{1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5}, "right"));
    }
    public static String solution(int[] numbers, String hand) {
        Map<Integer, Point> points = new HashMap<>();
        points.put(1, new Point(0, 0));
        points.put(2, new Point(0, 1));
        points.put(3, new Point(0, 2));
        points.put(4, new Point(1, 0));
        points.put(5, new Point(1, 1));
        points.put(6, new Point(1, 2));
        points.put(7, new Point(2, 0));
        points.put(8, new Point(2, 1));
        points.put(9, new Point(2, 2));
        points.put(0, new Point(3, 1));

        Point left_hand = new Point(3, 0);
        Point right_hand = new Point(3, 2);
        StringBuilder ans = new StringBuilder();

        for (int i = 0; i < numbers.length; i++) {
            int now = numbers[i];
            if (now == 1 || now == 4 || now == 7) {
                left_hand = points.get(now);
                ans.append("L");
            }
            else if (now == 3 || now == 6 || now == 9) {
                right_hand = points.get(now);
                ans.append("R");
            }
            else {
                Point next_hand = points.get(now);
                int left_distance = Math.abs(left_hand.x - next_hand.x) + Math.abs(left_hand.y - next_hand.y);
                int right_distance = Math.abs(right_hand.x - next_hand.x) + Math.abs(right_hand.y - next_hand.y);
                if (left_distance == right_distance) {
                    if (hand.equals("right")) {
                        right_hand = next_hand;
                        ans.append("R");
                    } else {
                        left_hand = next_hand;
                        ans.append("L");
                    }
                } else if (left_distance > right_distance) {
                    right_hand = next_hand;
                    ans.append("R");
                } else {
                    left_hand = next_hand;
                    ans.append("L");
                }
            }
        }
        return ans.toString();
    }

    static class Point {
        int x;
        int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
