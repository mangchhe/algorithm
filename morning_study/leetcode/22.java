class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        traverse(res, "", n, n);
        return res;
    }
    
    private void traverse(List<String> res, String str, int l, int r) {
        if (l == 0 && r == 0) {
            res.add(str);
        }
        
        if (l > 0) {
            traverse(res, str + "(", l-1, r);
        }
        if (r > 0 && l < r) {
            traverse(res, str + ")", l, r-1);   
        }
    }
}
