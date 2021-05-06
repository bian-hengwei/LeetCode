/*
 * @lc app=leetcode.cn id=1486 lang=java
 *
 * [1486] 数组异或操作
 */

// @lc code=start
class Solution {
    public int xorOperation(int n, int start) {
        int res = 0;
        // xor nums[i] = start + 2i
        for (int i = 0; i < n; i++) res ^= start + 2 * i;
        return res;
    }
}
// @lc code=end

