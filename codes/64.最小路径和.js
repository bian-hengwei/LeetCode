/*
 * @lc app=leetcode.cn id=64 lang=javascript
 *
 * [64] 最小路径和
 */

// @lc code=start
/**
 * @param {number[][]} grid
 * @return {number}
 */
 var minPathSum = function(grid) {
    // dp for the whole grid
    for (i = 0; i < grid.length; i++) {
        // special case for [0][0]
        if (i === 0) cur = [grid[0][0]];
        // special case for [i][0]
        else cur = [grid[i][0] + last[0]];
        for (j = 1; j < grid[0].length; j++) {
            // special case for [0][j]
            if (i === 0) cur.push(cur[j-1] + grid[i][j])
            // dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
            else cur.push(grid[i][j] + Math.min(cur[j-1], last[j]));
        }
        last = cur;
    }
    return cur[cur.length - 1];
};
// @lc code=end

