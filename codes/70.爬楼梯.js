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
    if (n < 3) return n;
    var stair1 = 1, stair2 = 2, temp;
    for (let i = 3; i < n; i++) {
        temp = stair2;
        stair2 += stair1;
        stair1 = temp;
    }
    return stair2;
};
// @lc code=end

