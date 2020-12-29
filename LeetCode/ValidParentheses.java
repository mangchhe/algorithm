import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

/**
 * url : https://leetcode.com/problems/valid-parentheses/
 * 내용 : stack 사용법
 */

public class ValidParentheses {

    public static boolean isValid(String s) {
        Stack stack = new Stack();
        Map<Character, Character> map = new HashMap<>();
        map.put(')', '(');
        map.put('}', '{');
        map.put(']', '[');

        for (int i = 0; i < s.length(); i++) {
            if(stack.isEmpty()){
                stack.push(s.charAt(i));
            }else if(map.get(s.charAt(i)) == stack.peek()){
                stack.pop();
            }else{
                stack.push(s.charAt(i));
            }
        }

        if(!stack.isEmpty()) {
            return false;
        }else{
            return true;
        }
    }

    public static void main(String[] args) {
        System.out.println(isValid("()[]{}"));
    }
}