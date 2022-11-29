class Solution {
    public int[] plusOne(int[] digits) {
        plus(digits, digits.length - 1);
        if (digits[0] == 0) {
            int[] res = new int[digits.length + 1];
            res[0] = 1;
            for (int i = 0; i < digits.length; i++) {
                res[i + 1] = digits[i];
            }
            return res;
        }
        return digits;
    }
    
    private void plus(int[] digits, int idx) {
        if (idx < 0)
            return;
        
        if (++digits[idx] > 9) {
            digits[idx] = 0;
            plus(digits, idx - 1);
        }
    }
}
