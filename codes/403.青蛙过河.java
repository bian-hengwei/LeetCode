/*
 * @lc app=leetcode.cn id=403 lang=java
 *
 * [403] 青蛙过河
 */

// @lc code=start
class Solution {
    public boolean canCross(int[] stones) {
        int n = stones.length;
        // quit early if there is a big step
        for (int i = 1; i < n; i++) if (stones[i] - stones[i - 1] > i) return false;
        // dp[i][j] represents if stones[i] is reachable by step k
        boolean[][] dp = new boolean[n][n];
        dp[0][0] = true;
        for (int i = 0; i < n; i++) {
            // loop inversely to find past paths
            for (int j = i - 1; j >= 0; j--) {
                int step = stones[i] - stones[j];
                // quit at not reachable big steps
                if (step - j > 1) break;
                // set true dp[j] is reachable at step +/- 1
                dp[i][step] = dp[j][step - 1] || dp[j][step] || dp[j][step + 1];
                // quit at path found already
                if (i == n - 1 && dp[i][step]) return true;
            }
        }
        return false;
        // workable dfs solution exceeds time limit as binary search not used
        /*
        if (stones[1] != 1) return false;
        else if (stones.length > 2 && stones[2] != 2 && stones[2] != 3) return false;
        int range = stones[stones.length - 1] + 1;
        //if (range > 10000) return false;
        int[] reaches = new int[range];
        for (int i = 0; i < reaches.length; i++)  reaches[i] = Integer.MIN_VALUE;
        for (int stone : stones) reaches[stone] = 0;
        int[][] record = new int[range][stones.length];
        jump(1, 1, reaches, record);
        return reaches[reaches.length - 1] != 0;
        */
    }
    
    /*
    private void jump(int index, int k, int[] reaches, int[][] record) {
        int l = reaches.length;
        if (index <= 0 || k <= 0) return;
        else if (index > l - 1 || reaches[index] < 0) return;
        else if (record[index][k] != 0) return;
        else if (l - 2 <= index + k && index + k <= l) {
            reaches[l - 1] = 1;
            return;
        }
        reaches[index] += 1;
        record[index][k] += 1;
        jump(index + k - 1, k - 1, reaches, record);
        jump(index + k    , k    , reaches, record);
        jump(index + k + 1, k + 1, reaches, record);
    }
    */
}
// @lc code=end

