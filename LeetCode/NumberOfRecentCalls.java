import java.util.LinkedList;
import java.util.Queue;

/**
 * url : https://leetcode.com/problems/number-of-recent-calls/
 * 내용 : queue 사용법
 */

public class NumberOfRecentCalls {

}

class RecentCounter {

    Queue<Integer> queue;

    public RecentCounter() {
        this.queue = new LinkedList<>();
    }

    public int ping(int t) {
        this.queue.offer(t);

        while(this.queue.peek() < t - 3000)
            this.queue.poll();

        return this.queue.size();
    }
}
