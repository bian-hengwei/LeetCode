/*
 * @lc app=leetcode.cn id=33 lang=javascript
 *
 * [33] 搜索旋转排序数组
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
 var search = function(nums, target) {
    // left and right boundary for binary search
    l = 0;
    r = nums.length - 1;
    while (l <= r) {
        // binary search
        mid = Math.floor(l + (r - l));
        if (nums[mid] === target) {
            return mid;
        }
        // left is sorted
        if (nums[0] <= nums[mid]) {
            if (nums[0] <= target && target < nums[mid])
                r = mid - 1;
            else
                l = mid + 1;
        }
        // right is sorted
        else {
            if (nums[mid] < target && target <= nums[nums.length - 1])
                l = mid + 1;
            else
                r = mid - 1;
        }
    }
    return -1;
};
// @lc code=end

