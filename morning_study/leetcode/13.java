class Solution {
    public int romanToInt(String s) {
        Map<String, Integer> cache = new HashMap<>(){{
            put("I", 1);
            put("V", 5);
            put("X", 10);
            put("L", 50);
            put("C", 100);
            put("D", 500);
            put("M", 1000);
            put("IV", 4);
            put("IX", 9);
            put("XL", 40);
            put("XC", 90);
            put("CD", 400);
            put("CM", 900);
        }};
        int sum = 0;
        int i = 0;
        
        while (i < s.length()) {
            if (i + 2 < s.length() + 1) {
                String twoNumeral = s.substring(i, i + 2);
                if (cache.containsKey(twoNumeral)) {
                    sum += cache.get(twoNumeral);
                    i = i + 2;
                    continue;
                }
            }
            sum += cache.get(String.valueOf(s.charAt(i++)));
        }
        
        return sum;
    }
}
