import java.util.HashMap;
import java.util.Map;

/**
 * url : https://leetcode.com/problems/add-two-numbers/
 */
public class LongestSubstringWithoutRepeatingCharacters {
    public int lengthOfLongestSubstring(String s) {
        int size = 0;
        Map<Character, Integer> storage = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            storage.put(s.charAt(i), 1);
            for (int j = i + 1; j < s.length(); j++) {
                if(storage.containsKey(s.charAt(j))){
                    if(storage.size() > size){
                        size = storage.size();
                    }
                    storage.clear();
                    break;
                }
                else{
                    storage.put(s.charAt(j), 1);
                }
            }
            if(storage.size() > size){
                return storage.size();
            }
        }
        return size;
    }
}