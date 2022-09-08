class Solution {
    public boolean isPalindrome(String s) {
        int l=0, r=s.length() - 1;
        s = s.toUpperCase();
        
        while (l < r) {
            while (l < s.length() - 1 && !Character.isLetterOrDigit(s.charAt(l))) {
                l++;
            }
            
            while (r > 0 && !Character.isLetterOrDigit(s.charAt(r))) {
                r--;
            }
            
            if (!Character.isLetterOrDigit(s.charAt(l)) && !Character.isLetterOrDigit(s.charAt(r))) {
                return true;
            }
            
            if (s.charAt(l) != s.charAt(r)) {
                return false;
            }
            
            l++; r--;
        }
        
        return true;
    }
}
