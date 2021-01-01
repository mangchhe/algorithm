
public class StackProblem1 {
    public static void main(String[] args) {
        Solution solution = new Solution();
        for(Integer i:solution.solution(new int[]{1,2,3,2,3})){
            System.out.println(i);
        }
    }
    static class Solution {
        public int[] solution(int[] prices) {

            /* 방법1
            int len = prices.length;
            int[] answer = new int[len];
            int cnt;
            for (int i = 0; i < len - 1; i++) {
                cnt = 0;
                for (int j = i + 1; j < len; j++) {
                    cnt++;
                    if(prices[i] > prices[j]){
                        answer[i] = cnt;
                        break;
                    }
                    if(j == len - 1){
                        answer[i] = cnt;
                    }
                }
            }
            return answer;*/

            // 방법2
            int len = prices.length;
            int[] answer = new int[len];
            for (int i = 0; i < len - 1; i++) {
                for (int j = i + 1; j < len; j++) {
                    answer[i] ++;
                    if(prices[i] > prices[j]){
                        break;
                    }
                }
            }
            return answer;
        }
    }
}
