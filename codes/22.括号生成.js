/*
 * @lc app=leetcode.cn id=22 lang=javascript
 *
 * [22] 括号生成
 */
/**
 * @param {number} n
 * @return {string[]}
 */
 var generateParenthesis = function(n) {
    arr = [];
    backtrack = function(l, r, cur) {
        if (n * 2 == l + r) arr.push(cur);
        else {
            if (l < n) backtrack(l+1, r, cur+"(", arr);
            if (r < l) backtrack(l, r+1, cur+")", arr);
        }
    }
    backtrack(0, 0, "")
    return arr;
};
// @lc code=end

