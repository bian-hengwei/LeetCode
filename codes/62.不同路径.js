/*
 * @lc app=leetcode.cn id=62 lang=javascript
 *
 * [62] 不同路径
 */

// @lc code=start
/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
 var uniquePaths = function(m, n) {
    // first row
    dp = Array(n).fill(1);
    // ignore first row and first col
    for (i = 1; i < m; i++) {
        for (j = 1; j < n; j++) {
            // update remaining
            dp[j] = dp[j] + dp[j-1];
        }
    }
    return dp[n-1];
};
// @lc code=end

