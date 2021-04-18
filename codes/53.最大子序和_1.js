/*
 * @lc app=leetcode.cn id=53 lang=javascript
 *
 * [53] 最大子序和
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
 var maxSubArray = function(nums) {
    cur = 0;
    res = nums[0];
    // dynamic programming:
    // val[i] = max(nums[i], val[i-1] + nums[i])
    nums.forEach(i => {
        cur = cur > 0 ? cur + i : i;
        res = cur > res ? cur : res;
    });
    return res;
};
// @lc code=end

