/*
 * @lc app=leetcode.cn id=70 lang=javascript
 *
 * [70] 爬楼梯
 */

// @lc code=start
/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    // hard code
    if (n < 3) return n;
    // three pointers
    // pointer -2  pointer -1   temp for swap
    var stair1 = 1, stair2 = 2, temp;
    for (let i = 3; i < n; i++) {
        // dp[i] = dp[i-1] + dp[i-2]
        temp = stair2;
        stair2 += stair1;
        stair1 = temp;
    }
    return stair2;
};
// @lc code=end

