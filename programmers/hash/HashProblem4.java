import java.util.*;

/**
 * url : https://programmers.co.kr/learn/courses/30/lessons/42579
 */

public class HashProblem4 {
    public static void main(String[] args) {
        Solution solution = new Solution();
        solution.solution(new String[]{"classic", "pop", "classic", "classic", "pop"},
        new int[]{500, 600, 150, 800, 2500});
    }
    static class Solution {
        public int[] solution(String[] genres, int[] plays) {
            int[] answer = {};

            ArrayList<Integer> result = new ArrayList<>();

            int len = genres.length;

            Map<String, Integer> genresMap = new HashMap<>();

            for (int i = 0; i < len; i++) {
                genresMap.put(genres[i], genresMap.getOrDefault(genres[i], 0) + plays[i]);
            }

            List<Map.Entry<String, Integer>> list = new LinkedList<>(genresMap.entrySet());

            Collections.sort(list, new Comparator<Map.Entry<String, Integer>>() {
                @Override
                public int compare(Map.Entry<String, Integer> o1, Map.Entry<String, Integer> o2) {
                    return o2.getValue().compareTo(o1.getValue());
                }
            });

            TreeMap<Integer, Integer> treeMap = new TreeMap<>();
            List<Integer> list2 = new ArrayList<>();

            for(Map.Entry<String, Integer> map : list){
                for (int i = 0; i < len; i++) {
                    if(map.getKey().equals(genres[i])){
                        treeMap.put(i, plays[i]);
                        list2.add(plays[i]);
                    }
                }
                list2.sort(Comparator.reverseOrder());
                for (int i = 0; i < list2.size(); i++) {
                    for(Map.Entry<Integer, Integer> map2 :treeMap.entrySet()){
                        if(map2.getValue().equals(list2.get(i))){
                            result.add(map2.getKey());
                            treeMap.remove(map2.getKey());
                            break;
                        }
                    }
                    if(i == 1){
                        break;
                    }
                }
                treeMap.clear();
                list2.clear();
            }

            answer = new int[result.size()];

            for (int i = 0; i < result.size(); i++) {
                answer[i] = result.get(i);
            }

            return answer;
        }
    }
}
