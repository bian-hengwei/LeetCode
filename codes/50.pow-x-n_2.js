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
    result = 1;
    pow = x;
    while (n > 0) {
        if (n % 2) result *= pow;
        pow *= pow;
        n = n / 2 >> 0;
    }
    return result;
};
// @lc code=end

