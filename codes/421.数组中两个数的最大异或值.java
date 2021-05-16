/*
 * @lc app=leetcode.cn id=421 lang=java
 *
 * [421] 数组中两个数的最大异或值
 */

// @lc code=start
class Solution {
    public int findMaximumXOR(int[] nums) {
        int max = 0;
        for (int num: nums) {
            max = Math.max(max, num);
        }
        int len = 32 - Integer.numberOfLeadingZeros(max);
        Set<Integer> prefix = new HashSet<>();
        int maxXOR = 0;
        for (int i = len - 1; i >= 0; i--) {
            maxXOR <<= 1;
            int curPrefix = maxXOR | 1;
            prefix.clear();
            for (int num: nums) {
                prefix.add(num >> i);
                if (prefix.contains(num >> i ^ curPrefix)) {
                    maxXOR |= 1;
                    break;
                }
            }
        }
        return maxXOR;
    }
}
// @lc code=end

