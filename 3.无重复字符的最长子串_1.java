/*
 * @lc app=leetcode.cn id=3 lang=java
 *
 * [3] 无重复字符的最长子串
 */

// @lc code=start
class Solution {
    public int lengthOfLongestSubstring(String s) {
        // max length, current start pointer
        int max_len = 0, p = 0, len = s.length();
        // last[i] is ascii character i's last appearance index
        int[] last = new int[128];
        for (int q = 0; q < len; q++) {
            int i = (int)s.charAt(q);
            // update pointer and max
            p = Math.max(p, last[i]);
            max_len = Math.max(max_len, q - p + 1);
            // store this appearance
            last[i] = q+1;
        }
        return max_len;
    }
}
// @lc code=end

