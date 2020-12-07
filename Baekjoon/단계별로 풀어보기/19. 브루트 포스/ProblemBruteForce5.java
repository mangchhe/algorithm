import java.util.Scanner;

public class ProblemBruteForce5 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.nextLine());

        int title = 665;

        while(n > 0) {

            title += 1;

//			int sixCnt = 0;
//
//			for(int i =0; i < (title + "").length(); i++) {
//				if('6' == (title + "").charAt(i)) {
//					sixCnt += 1;
//				}
//				else {
//					sixCnt = 0;
//				}
//				if(sixCnt == 3) {
//					n -= 1;
//					break;
//				}
//			}

            if((""+title).contains("666")) {
                n -= 1;
            }
        }
        System.out.println(title);
    }

}