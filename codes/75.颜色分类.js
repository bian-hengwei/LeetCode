/*
 * @lc app=leetcode.cn id=75 lang=javascript
 *
 * [75] 颜色分类
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    // r, w, b means last red, white, blue
    r = -1, w = -1;
    // last element is always blue
    for (b = 0; b < nums.length; b++) {
        // if this is not blue
        if (nums[b] < 2) {
            // swap with last white
            w ++;
            [nums[b], nums[w]] = [nums[w], nums[b]];
            // if it is not white
            if (nums[w] < 1) {
                // swap with last red
                r ++;
                [nums[w], nums[r]] = [nums[r], nums[w]];
            }
        }
    }
};
// @lc code=end

