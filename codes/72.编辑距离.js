/*
 * @lc app=leetcode.cn id=72 lang=javascript
 *
 * [72] 编辑距离
 */

// @lc code=start
/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function(word1, word2) {
    m = word1.length, n = word2.length;
    // according to question
    // if either is empty return the len of the other
    if (m * n === 0) return m + n;
    // init dp array with first row initialized
    dp = Array.from(new Array(n + 1).keys()).slice(0)
    // for each row
    for (i = 1; i <= m; i++) {
        // store leftBottom
        [leftBottom, dp[0]] = [dp[0], i];
        for (j = 1; j <= n; j++)
            // dp[i] = min(left+1, bottom+1, leftBottom + 1 if matches)
            [dp[j], leftBottom] =  [Math.min(dp[j - 1] + 1, dp[j] + 1, leftBottom + (word1[i - 1] != word2[j - 1]) >>> 0), dp[j]];
    }
    return dp[n];
};
// @lc code=end

