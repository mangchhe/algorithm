class Solution {
    public String[] findRelativeRanks(int[] score) {
        String[] res = new String[score.length];
        PriorityQueue<KeyValue> pq = new PriorityQueue<>();
        
        for (int i=0; i<score.length; i++) {
            pq.offer(new KeyValue(score[i], i));
        }
        
        int ranking = 1;
        String[] medal = {"Gold Medal","Silver Medal","Bronze Medal"};
        while (!pq.isEmpty()) {
            KeyValue curr = pq.poll();
            
            if (ranking < 4) {
                res[curr.value] = medal[ranking - 1];
            } else {
                res[curr.value] = String.valueOf(ranking);
            }
            ranking++;
        }
        
        return res;
    }
    
    class KeyValue implements Comparable<KeyValue> {
        public int key;
        public int value;
        
        public KeyValue(int key, int value) {
            this.key = key;
            this.value = value;
        }
        
        @Override
        public int compareTo(KeyValue keyValue) {
            return keyValue.key - key;
        }
    }
}
