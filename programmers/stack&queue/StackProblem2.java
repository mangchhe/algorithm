import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

/**
 * url : https://programmers.co.kr/learn/courses/30/lessons/42586
 */

public class StackProblem2 {
    public static void main(String[] args) {
        Solution solution = new Solution();
        solution.solution(new int[]{93, 30, 55}, new int[]{1, 30 ,5});
    }
    static class Solution {
        public int[] solution(int[] progresses, int[] speeds) {
            Queue<Integer> queue = new LinkedList<>();
            ArrayList<Integer> list = new ArrayList<>();
            int size = 0, cnt = 1;
            int len = progresses.length;
            for (int i = 0; i < len; i++) {
                queue.offer((int) Math.ceil((100.0 - progresses[i]) / speeds[i]));
            }

            while(!queue.isEmpty()){
                size = queue.poll();
                len = queue.size();
                for (int i = 0; i < len; i++) {
                    if(size >= queue.peek()){
                        queue.poll();
                        cnt++;
                    }else{
                        list.add(cnt);
                        cnt = 1;
                        break;
                    }
                }
            }

            if(cnt != 0){
                list.add(cnt);
            }

            int[] answer = new int[list.size()];

            for (int i = 0; i < list.size(); i++) {
                answer[i] = list.get(i);
            }

            return answer;
        }
    }
}
