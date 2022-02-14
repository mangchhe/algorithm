class MinStack {
    
    Stack<Integer> st;
    Stack<Integer> minSt;

    public MinStack() {
        st = new Stack<>();
        minSt = new Stack<>();
    }
    
    public void push(int val) {
        st.add(val);
        if (minSt.isEmpty() || minSt.peek() >= val) {
            minSt.add(val);
        }
    }
    
    public void pop() {
        int val = st.pop();
        if (minSt.peek() == val) {
            minSt.pop();
        }
    }
    
    public int top() {
        return st.peek();
    }
    
    public int getMin() {
        return minSt.peek();
    }
}
