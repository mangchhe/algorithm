class Solution {
    public String addBinary(String a, String b) {
        StringBuilder result = new StringBuilder();
        int aLen = a.length() - 1;
        int bLen = b.length() - 1;
        int plus = 0;

        while (aLen > -2 || bLen > -2) {
            if (aLen > -1 && bLen > -1) {
                int[] val = calculate(a.charAt(aLen) - '0', b.charAt(bLen) - '0', plus);
                plus = val[0];
                result.append(val[1]);
            }
            else if (aLen > -1) {
                int[] val = calculate(a.charAt(aLen) - '0', 0, plus);
                plus = val[0];
                result.append(val[1]);
            }
            else if (bLen > -1) {
                int[] val = calculate(0, b.charAt(bLen) - '0', plus);
                plus = val[0];
                result.append(val[1]);
            }
            else {
                result.append(plus == 1 ? "1" : "");
            }
            aLen--;
            bLen--;
        }
        return result.reverse().toString();
    }

    public int[] calculate(int a, int b, int c) {
        int sum = a + b + c;
        int[] ret = new int[2];
        switch (sum) {
            case 3:
                ret[0] = 1;
                ret[1] = 1;
                return ret;
            case 2:
                ret[0] = 1;
                ret[1] = 0;
                return ret;
            case 1:
                ret[0] = 0;
                ret[1] = 1;
                return ret;
            case 0:
                ret[0] = 0;
                ret[1] = 0;
                return ret;
        }
        return ret;
    }
}

