class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> cnts = new HashMap<>();
        
        for (int i = 0; i < s.length(); i++) {
            char word = s.charAt(i);
            cnts.put(word, cnts.getOrDefault(word, 0) + 1);
        }
        
        for (int i = 0; i < t.length(); i++) {
            char word = t.charAt(i);
            if(!cnts.containsKey(word)) {
                return false;
            }
            
            cnts.put(word, cnts.get(word) - 1);
            
            if (cnts.get(word) == 0) {
                cnts.remove(word);
            }
        }
        
        if (cnts.isEmpty())
            return true;
        
        return false;
    }
}
