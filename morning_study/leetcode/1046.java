class Solution {
    public int lastStoneWeight(int[] stones) {
        Queue<Integer> hq = new PriorityQueue<>(Collections.reverseOrder());
        
        for (int stone: stones)
            hq.offer(stone);
        
        while (hq.size() > 1) {
            int first = hq.poll();
            int second = hq.poll();
            
            if (first != second)
                hq.offer(first - second);
        }
        
        return hq.size() == 1 ? hq.poll() : 0;
    }
}
