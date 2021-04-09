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
    // initialize result array
    arr = [];
    // recursion for generating parenthesis
    backtrack = function(l, r, cur) {
        // base when len reaches n
        if (n * 2 == l + r) arr.push(cur);
        else {
            // add a left bracket if available
            if (l < n) backtrack(l+1, r, cur+"(", arr);
            // add a right bracket if available
            if (r < l) backtrack(l, r+1, cur+")", arr);
        }
    }
    // recursion call
    backtrack(0, 0, "")
    return arr;
};
// @lc code=end

