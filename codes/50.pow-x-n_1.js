/*
 * @lc app=leetcode.cn id=50 lang=javascript
 *
 * [50] Pow(x, n)
 */

// @lc code=start
/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
 var myPow = function(x, n) {
    if (n < 0) {
        x = 1 / x;
        n *= -1;
    }
    if (n === 0) return 1;
    if (n === 1) return x;
    half = n / 2 >> 0;
    halfPow = myPow(x, half);
    if (n % 2 === 1) return halfPow * halfPow * x;
    return halfPow * halfPow;
};
// @lc code=end

