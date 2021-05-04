/*
 * @lc app=leetcode.cn id=1011 lang=java
 *
 * [1011] 在 D 天内送达包裹的能力
 */

// @lc code=start
class Solution {
    public int shipWithinDays(int[] weights, int D) {
        // left bound init to max value of weights (min val of capacity)
        // right bound init to sum of all weights (max val of capacity)
        int l = 0, r = 0;
        for (int w : weights) {
            l = l > w ? l : w;
            r += w;
        }
        // binary search according to rule set
        // search for capacity
        // see if days needed is larger or smaller than middle
        while (l < r) {
            int m = (l + r) / 2, day = 1, cur = 0;
            for (int w : weights) {
                if (cur + w > m) {
                    day ++;
                    cur = 0;
                }
                cur += w;
            }
            if (day <= D) r = m;
            else l = m + 1;
        }
        return l;
    }
}
// @lc code=end

