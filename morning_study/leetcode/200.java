class Solution {
    public int numIslands(char[][] grid) {
        int h = grid.length;
        int w = grid[0].length;

        boolean[][] visited = new boolean[h][w];

        int islands = 0;

        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (grid[i][j] == '1' && !visited[i][j]) {
                    islands++;
                    move(grid, visited, i, j, h, w);
                }
            }
        }

        return islands;
    }

    private void move(char[][] grid, boolean[][] visited, int x, int y, int h, int w) {
        if (visited[x][y]) return;

        visited[x][y] = true;
        if (x + 1 < h && grid[x + 1][y] == '1') move(grid, visited, x + 1, y, h, w);
        if (x - 1 > -1 && grid[x - 1][y] == '1') move(grid, visited, x - 1, y, h, w);
        if (y + 1 < w && grid[x][y + 1] == '1') move(grid, visited, x, y + 1, h, w);
        if (y - 1 > -1 && grid[x][y - 1] == '1') move(grid, visited, x, y - 1, h, w);
    }
}
