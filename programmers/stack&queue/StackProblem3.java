import java.util.LinkedList;
import java.util.Queue;

public class StackProblem3 {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution(2, 10, new int[]{7,4,5,6}));

    }
    static class Solution {
        public int solution(int bridge_length, int weight, int[] truck_weights) {
            Queue<Integer> truck_weights_queue = new LinkedList<>();
            LinkedList<Integer> bridge_truck = new LinkedList<>();
            LinkedList<Integer> bridge_truck_weight = new LinkedList<>();

            for (int i = 0; i < truck_weights.length; i++) {
                truck_weights_queue.add(truck_weights[i]);
            }

            int answer = 0, currentWeight = 0;

            while(!bridge_truck.isEmpty() || !truck_weights_queue.isEmpty()){
                if(!truck_weights_queue.isEmpty() && currentWeight + truck_weights_queue.peek() <= weight){
                    bridge_truck.add(bridge_length);
                    currentWeight += truck_weights_queue.peek();
                    bridge_truck_weight.add(truck_weights_queue.poll());
                }
                for (int i = 0; i < bridge_truck.size(); i++) {
                    bridge_truck.set(i, bridge_truck.get(i) - 1);
                }
                if(bridge_truck.get(0) == 0) {
                    bridge_truck.removeFirst();
                    currentWeight -= bridge_truck_weight.removeFirst();
                }
                answer += 1;
            }

            return answer + 1;
        }
    }
}
