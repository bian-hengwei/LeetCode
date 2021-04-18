/*
 * @lc app=leetcode.cn id=55 lang=javascript
 *
 * [55] 跳跃游戏
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {boolean}
 */
 var canJump = function(nums) {
    // max reach distance from current index
    maxDist = 1;
    for (i = 0; i < nums.length; i++) {
        // cannot jump further
        if (maxDist === 0) return false;
        maxDist --;
        // finished checking
        if (maxDist >= nums.length - i - 1) return true;
        // update
        maxDist = maxDist > nums[i] ? maxDist : nums[i];
    }
    return true;
};
// @lc code=end

