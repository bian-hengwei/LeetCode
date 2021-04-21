/*
 * @lc app=leetcode.cn id=91 lang=javascript
 *
 * [91] 解码方法
 */

// @lc code=start
/* 2021/04/21 每日一题 */
/**
 * @param {string} s
 * @return {number}
 */
 var numDecodings = function(s) {
    // stores last two values in dp array
    secondLast = 0, last = 1, current = 0;
    for (i = 0; i < s.length; i ++) {
        // situation when dp[i-1] should be included
        if (s[i] !== '0') {
            current += last;
        }
        // situation when dp[i-2] should be included
        if (i != 0 && s[i - 1] != '0' && 
            ((s[i - 1] - '0') * 10 + (s[i] - '0') <= 26)) {
            current += secondLast
        }
        // swap and reset dp values
        [secondLast, last, current] = [last, current, 0];
    }
    return last;
};
// @lc code=end

