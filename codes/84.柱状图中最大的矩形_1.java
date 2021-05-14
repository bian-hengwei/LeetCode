/*
 * @lc app=leetcode.cn id=84 lang=java
 *
 * [84] 柱状图中最大的矩形
 */

// @lc code=start
class Solution {
    public int largestRectangleArea(int[] heights) {
        int n = heights.length, res = 0;
        int[] left = new int[n], right = new int[n];
        Arrays.fill(right, n);
        Deque<Integer> s = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            while (!s.isEmpty() && heights[s.peek()] >= heights[i]) {
                right[s.peek()] = i;
                s.pop();
            }
            left[i] = s.isEmpty() ? -1: s.peek();
            s.push(i);
        }
        for (int i = 0; i < n; i++) res = Math.max(res, (right[i] - left[i] - 1) * heights[i]);
        return res;
    }
}
// @lc code=end

