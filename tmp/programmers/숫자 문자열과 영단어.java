package programmers.숫자_문자열_영단어;

import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        System.out.println(solution("one4seveneight"));
    }
    public static int solution(String s) {
        /*
        * 방법 1
        * */
//        StringBuilder ans = new StringBuilder();
//        List<String> alphabets = List.of("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine");
//        StringBuilder tmp = new StringBuilder();
//        for (int i = 0; i < s.length(); i++) {
//            if (s.charAt(i) >= 48 && s.charAt(i) <= 57) {
//                ans.append(s.charAt(i));
//            }
//            else {
//                tmp.append(s.charAt(i));
//                if (alphabets.contains(tmp.toString())) {
//                    ans.append(alphabets.indexOf(tmp.toString()));
//                    tmp = new StringBuilder();
//                }
//            }
//        }
//        return Integer.parseInt(ans.toString());

        /*
        * 방법 2
        * replaceAll 이용
        * */
//        String[] alphabets = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
//
//        for (int i = 0; i < 10; i++) {
//            s = s.replaceAll(alphabets[i], String.valueOf(i));
//        }
//
//        return Integer.parseInt(s);
        /*
        * 방법 3
        * replace 이용
        * */
        String[] alphabets = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

        for (int i = 0; i < 10; i++) {
            s = s.replace(alphabets[i], String.valueOf(i));
        }

        return Integer.parseInt(s);
    }
}
