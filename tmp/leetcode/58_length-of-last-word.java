class Solution {
    public int lengthOfLastWord(String s) {
        int l = 0, r = 0;
        int result = 0;
        
        while (r < s.length()) {
            if(s.charAt(r) == ' ') {
                if (l - r != 0) {
                    result = r - l;
                }
                l = ++r;
                continue;
            }
            
            r++;
        }
        
        if (r - l != 0) {
            return r - l;
        }
        return result;
    }
}
