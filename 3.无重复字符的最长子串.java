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

// Map version (self written), same time complexity but slower with hash map
/*
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int max_len = 0, cur_len = 0, p = 0, len = s.length();
        Map<Character, Integer> substring = new HashMap<Character, Integer>();
        for (int q = 0; q < len; q++) {
            if (substring.containsKey(s.charAt(q)) && substring.get(s.charAt(q)) >= p) {
                p = substring.get(s.charAt(q)) + 1;
                max_len = max_len < cur_len ? cur_len : max_len;
                cur_len = q - p;
            }
            substring.put(s.charAt(q), q);
            cur_len ++;
        }
        return max_len < cur_len ? cur_len : max_len;
    }
}
*/
// @lc code=end

