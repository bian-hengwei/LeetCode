/*
 * @lc app=leetcode.cn id=79 lang=java
 *
 * [79] 单词搜索
 */

// @lc code=start
class Solution {

    // global variables
    boolean[][] visited;
    char[][] B;
    String W;
    int M, N, S;

    public boolean exist(char[][] board, String word) {
        // store globals
        M = board.length;
        N = board[0].length;
        S = word.length();
        B = board;
        W = word;
        // true if in current recursion
        visited = new boolean[M][N];
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) if (backtrack(i, j, 0)) return true;
        }
        return false;
    }

    private boolean backtrack(int i, int j, int k) {
        // if fail to match return false
        if (W.charAt(k) != B[i][j]) return false;
        // if matches but visited return false
        if (visited[i][j]) return false;
        // finally check if this is the last match
        if (k == S - 1) return true;

        // middle steps
        // first mark as visited
        visited[i][j] = true;
        // up
        if (i != 0     && backtrack(i - 1, j, k + 1)) return true;
        // left
        if (j != 0     && backtrack(i, j - 1, k + 1)) return true;
        // right
        if (j != N - 1 && backtrack(i, j + 1, k + 1)) return true;
        // down
        if (i != M - 1 && backtrack(i + 1, j, k + 1)) return true;
        // unmark
        visited[i][j] = false;
        return false;
    }
}
// @lc code=end

