import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {

        int N = Integer.parseInt(sc.nextLine());

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(sc.nextLine(), " ");
            String s = st.nextToken();
            String s2 = st.nextToken();
            StringBuilder addS = new StringBuilder("");

            int sLen = s.length() - 1;
            int s2Len = s2.length() - 1;

            int round = 0;

            while (sLen > -1 || s2Len > -1) {
                int a;
                int b;
                if (sLen == -1) {
                    a = 0;
                } else {
                    a = Integer.parseInt(String.valueOf(s.charAt(sLen)));
                    sLen -= 1;
                }

                if (s2Len == -1) {
                    b = 0;
                } else {
                    b = Integer.parseInt(String.valueOf(s2.charAt(s2Len)));
                    s2Len -= 1;
                }

                if (a + b + round == 3) {
                    round = 1;
                    addS.insert(0, 1);
                } else if (a + b + round == 2) {
                    round = 1;
                    addS.insert(0, 0);
                } else if (a + b + round == 1) {
                    round = 0;
                    addS.insert(0, 1);
                } else {
                    addS.insert(0, 0);
                }
            }

            if (round == 1) {
                addS.insert(0, 1);
            }

            while (addS.length() > 1) {
                if (addS.charAt(0) == '0')
                    addS.deleteCharAt(0);
                else
                    break;
            }

            System.out.println(addS);

        }
    }
}
