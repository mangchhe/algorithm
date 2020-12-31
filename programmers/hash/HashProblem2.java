/**
 * url : https://programmers.co.kr/learn/courses/30/lessons/42577
 */

public class HashProblem2 {

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution(new String[]{"4321", "432"}));
    }

    static class Solution {
        public boolean solution(String[] phone_book) {

            int len = phone_book.length;
            for (int i = 0; i < len; i++) {
                String str = phone_book[i] + ".*";
                for (int j = 0; j < len; j++) {
                    if(j != i && phone_book[j].matches(str)){
                        return false;
                    }
                }
            }
            return true;
        }
    }
}
