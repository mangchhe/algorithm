import java.util.HashMap;
import java.util.Map;

/**
 * url : https://leetcode.com/problems/add-two-numbers/
 */
public class LongestSubstringWithoutRepeatingCharacters {
    public int lengthOfLongestSubstring(String s) {
        int result = 0, i = 0, j = 0;
        int n = s.length();
        Set<Character> repos = new HashSet<>();
        while(i < n && j < n){
            if(!repos.contains(s.charAt(j))){
                repos.add(s.charAt(j++));
                result = Math.max(result, j - i);
            }else{
                repos.remove(s.charAt(i++));
            }
        }
        return result;
    }
}