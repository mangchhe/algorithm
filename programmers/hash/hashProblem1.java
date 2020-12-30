import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

/**
 * url : https://programmers.co.kr/learn/courses/30/lessons/42576?language=java
 */

public class hashProblem1 {
    public static void main(String[] args) {
        Solution s = new Solution();
        s.solution(new String[]{"leo", "kiki", "eden", "eden"}, new String[]{"eden", "kiki"});
    }
    static class Solution {
        public String solution(String[] participant, String[] completion) {
            /* 방법1
            Map<String, Integer> map = new HashMap<>();

            for(String p : participant){
                if ((map.containsKey(p))) {
                    map.put(p, map.get(p) + 1);
                } else {
                    map.put(p, 1);
                }
            }

            for(String c : completion){
                if(map.containsKey(c)){
                    int n = map.get(c) - 1;
                    if(n == 0){
                        map.remove(c);
                    }else{
                        map.put(c, n);
                    }
                }
            }

            Iterator<Map.Entry<String, Integer>> iterator = map.entrySet().iterator();

            return iterator.next().getKey();*/

            /* 방법2
            String answer = "";
            HashMap<String, Integer> map = new HashMap<>();
            for(String p : participant) map.put(p, map.getOrDefault(p, 0) + 1);
            for(String c : completion) map.put(c, map.get(c) - 1);

            for(String key : map.keySet()){
                if(map.get(key) != 0){
                    answer = key;
                }
            }

            return answer;*/

            /* 방법3
            String answer = "";
            HashMap<String, Integer> map = new HashMap<>();
            for(String p : participant) map.put(p, map.getOrDefault(p, 0) + 1);
            for(String c : completion) map.put(c, map.get(c) - 1);

            return map.entrySet().stream().filter(
                    m -> m.getValue() != 0
            ).iterator().next().getKey();*/

            // 방법4
            String answer = "";
            HashMap<String, Integer> map = new HashMap<>();
            for(String p : participant) map.put(p, map.getOrDefault(p, 0) + 1);
            for(String c : completion) map.put(c, map.get(c) - 1);

            Iterator<Map.Entry<String, Integer>> iterator = map.entrySet().iterator();

            while(iterator.hasNext()){
                Map.Entry<String, Integer> next = iterator.next();
                if(next.getValue() != 0){
                    answer = next.getKey();
                    break;
                }
            }
            return answer;
        }
    }
}