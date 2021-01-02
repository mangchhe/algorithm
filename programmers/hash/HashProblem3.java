import java.util.HashMap;

/**
 * url : https://programmers.co.kr/learn/courses/30/lessons/42578?language=java
 */

public class HashProblem3 {

    class Solution {
        public int solution(String[][] clothes) {
            int answer = 1;
            HashMap<String, Integer> map = new HashMap<>();
            for (int i = 0; i < clothes.length; i++) {
                map.put(clothes[i][1], map.getOrDefault(clothes[i][1], 0) + 1);
            }
            for(int n : map.values()){
                answer *= n + 1;
            }
            return answer - 1;
        }
    }
}
