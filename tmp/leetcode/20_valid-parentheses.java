class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> words = new HashMap<Character, Character>() {{
            put(')', '(');
            put('}', '{');
            put(']', '[');
        }};
        
        for (int i = 0; i < s.length(); i++) {
            char curr = s.charAt(i);
            if (stack.isEmpty()) {
                stack.push(curr);
                continue;
            }
            
            if(stack.peek() == words.get(curr)) {
                stack.pop();
                continue;
            }
            
            stack.push(curr);
        }
        System.out.println(stack);
        if (stack.isEmpty())
            return true;
        
        return false;
    }
}
