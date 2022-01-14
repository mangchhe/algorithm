package programmers.신고_결과_받기;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        solution(new String[]{"muzi", "frodo", "apeach", "neo"}, new String[]{"muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"}, 2);
    }
    public static int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        Map<String, Set<String>> persons = new HashMap<>();
        Map<String, Integer> reportCnt = new LinkedHashMap<>();
        for (int i = 0; i < id_list.length; i++) {
            persons.put(id_list[i], new HashSet<>());
            reportCnt.put(id_list[i], 0);
        }
        for (String r: report) {
            String[] p = r.split(" ");
            persons.get(p[1]).add(p[0]);
        }
        for (Map.Entry<String, Set<String>> person : persons.entrySet()) {
            if (person.getValue().size() < k) {
                continue;
            }
            person.getValue().stream().forEach(x -> reportCnt.put(x, reportCnt.get(x) + 1));
        }
        int i = 0;
        for (Integer value : reportCnt.values()) {
            answer[i++] = value;
        }
        return answer;
    }
}
