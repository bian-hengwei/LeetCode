/*
 * @lc app=leetcode.cn id=42 lang=java
 *
 * [42] 接雨水
 */

// @lc code=start
class Solution {
    public int trap(int[] height) {
        // current pointers and max values
        int l = 0, r = height.length - 1, result = 0;
        int left = 0, right = 0;
        while (l < r) {
            if (height[l] < height[r]) {
                // update max value
                left = height[l] > left ? height[l] : left;
                // compute new rain water trapped
                result += left - height[l];
                l ++;
            }
            else {
                right = height[r] > right ? height[r] : right;
                result += right - height[r];
                r --;
            }
        }
        return result;
    }
}
// @lc code=end

