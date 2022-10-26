class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] words = new int[26];
        for (int i = 0; i < magazine.length(); i++) {
            words[magazine.charAt(i) - 'a']++;
        }
        for (int i = 0; i < ransomNote.length(); i++) {
            int n = ransomNote.charAt(i) - 'a';
            if (words[n] > 0)
                words[n]--;
            else
                return false;
        }
        return true;
    }
}
