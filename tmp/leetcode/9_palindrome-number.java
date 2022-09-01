class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        
        String str = Integer.toString(x);
        int total = str.length();
        int cnt = 0;
        
        for(int i = 0; i < total / 2; i++) {
            if(str.charAt(i) == str.charAt(total-i-1)) {
                cnt++;
            }
        }
        
        if (total / 2 == cnt) {
            return true;
        }
        
        return false;
    }
}
