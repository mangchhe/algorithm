package programmers.로또의_최고_순위와_최저_순위;

class Main {
    public static void main(String[] args) {

    }
    public int[] solution(int[] lottos, int[] win_nums) {
        int hit = 0;
        int blank = 0;
        for (int i = 0; i < lottos.length; i++) {
            for (int j = 0; j < win_nums.length; j++) {
                if (lottos[i] == 0) {
                    blank++;
                    break;
                }
                if (lottos[i] == win_nums[j]) {
                    hit++;
                    break;
                }
            }
        }
        int low = 0;
        int high = 0;
        if (hit + blank == 0) {
            high = 6;
        } else {
            high = 7 - (hit + blank);
        }
        if (hit < 2) {
            low = 6;
        } else {
            low = 7 - hit;
        }
        int [] answer = {high, low};
        return answer;
    }
}
