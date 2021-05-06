/*
 * @lc app=leetcode.cn id=76 lang=java
 *
 * [76] 最小覆盖子串
 */

// @lc code=start
class Solution {
    // target array stores the count of each ASCII character currently needed
    // for values in t stores t.count(chr) - found chr in current window
    // for values not in t is Integer.MIN_VALUE
    private int[] target = new int[128];

    public String minWindow(String s, String t) {
        if (s.length() < t.length()) return "";
        // initialize target array
        for (int i = 0; i < t.length(); i++) target[t.charAt(i)]++;
        for (int i = 0; i < target.length; i++) if (target[i] == 0) target[i] = Integer.MIN_VALUE;
        // best window, current window, notFound = t.length - valid characters found
        int bestl = -1, bestr = s.length(), l = 0, r = 0, notFound = t.length();
        // sliding window main loop
        while (r < s.length()) {
            // make a step
            // update notFound and target array
            notFound += add(s.charAt(r++), -1, 0);
            // if current window contains t
            while (notFound == 0) {
                // update best as needed
                if (bestr - bestl > r - l) {
                    bestr = r; bestl = l;
                }
                // increment left bound
                // if the window is still valid (e.g. aaab find ab)
                // return to the while loop
                notFound += add(s.charAt(l++), 1, 1);
            }
            // get rid of the garbage characters (e.g. xyzab find ab)
            while (l < r && target[s.charAt(l)] == Integer.MIN_VALUE) l++;
        }
        // if bestl is never updated means t is not included in s
        return bestl == -1 ? "" : s.substring(bestl, bestr);
    }

    // helper for quick update of target
    // dir = -1 if inc right: dec target and dec notFound (and vise versa)
    // bnd = 0 if inc right and = 1 if dec left -> see if notFound needs to be updated
    private int add(char c, int dir, int bnd) {
        if (target[c] != Integer.MIN_VALUE) target[c] += dir;
        return target[c] >= bnd ? dir : 0;
    }
}
// @lc code=end

