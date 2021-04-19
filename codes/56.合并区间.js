/*
 * @lc app=leetcode.cn id=56 lang=javascript
 *
 * [56] 合并区间
 */

// @lc code=start
/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */ 
 var merge = function(intervals) {
     // sort intervals according to first index
    intervals.sort((a, b) => a[0] - b[0]);
    res = [];
    for (interval of intervals) {
        last = res[res.length - 1]
        // if cannot merge then push new
        if (!res.length || interval[0] > last[1]) res.push(interval);
        // merge otherwise
        else last[1] = interval[1] > last[1] ? interval[1] : last[1];
    }
    return res;
};
// @lc code=end

