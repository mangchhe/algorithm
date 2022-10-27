/*
* https://leetcode.com/problems/flood-fill/
* */

class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int[][] visited = new int[image.length][image[0].length];
        dfs(image, sr, sc, color, visited);
        return image;
    }

    public void dfs(int[][] image, int x, int y, int color, int[][] visited) {
        if (visited[x][y] == 1) {
            return;
        }
        int beforeColor = image[x][y];
        image[x][y] = color;
        visited[x][y] = 1;

        if (x + 1 < image.length && isSameColor(image, x + 1, y, beforeColor)) {
            dfs(image, x + 1, y, color, visited);
        }
        if (x - 1 > -1 && isSameColor(image, x - 1, y, beforeColor)) {
            dfs(image, x - 1, y, color, visited);
        }
        if (y + 1 < image[x].length && isSameColor(image, x, y + 1, beforeColor)) {
            dfs(image, x, y + 1, color, visited);
        }
        if (y - 1 > -1 && isSameColor(image, x, y - 1, beforeColor)) {
            dfs(image, x, y - 1, color, visited);
        }
    }

    public boolean isSameColor(int[][] image, int x, int y, int color) {
        return image[x][y] == color;
    }
}
