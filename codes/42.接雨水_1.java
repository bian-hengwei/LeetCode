/*
 * @lc app=leetcode.cn id=42 lang=java
 *
 * [42] 接雨水
 */

// @lc code=start
class Solution {
    public int trap(int[] height) {
        int result = 0;
        // stack stores last processed index
        Deque<Integer> s = new LinkedList<>();
        for (int i = 0; i < height.length; i++) {
            while ((!s.isEmpty()) && height[s.peek()] < height[i]) {
                int j = s.pop();
                // means cannot trap rain water
                if (s.isEmpty()) break;
                int k = s.peek();
                // calculate rain water trapped at this level
                result += (i - k - 1) * (Math.min(height[i], height[k]) - height[j]);
            }
            s.push(i);
        }
        return result;
    }
}
// @lc code=end

