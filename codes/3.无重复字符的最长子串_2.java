/*
 * @lc app=leetcode.cn id=3 lang=java
 *
 * [3] 无重复字符的最长子串
 */

// @lc code=start


// Map version (self written), same time complexity but slower with hash map

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        // max and current length, current pointer
        int max_len = 0, cur_len = 0, p = 0, len = s.length();
        // hash map {character : last appearance index}
        Map<Character, Integer> substring = new HashMap<Character, Integer>();
        for (int q = 0; q < len; q++) {
            // if repeat in current substring
            // update length and go to first non-repeated char
            if (substring.containsKey(s.charAt(q)) && substring.get(s.charAt(q)) >= p) {
                p = substring.get(s.charAt(q)) + 1;
                max_len = max_len < cur_len ? cur_len : max_len;
                cur_len = q - p;
            }
            substring.put(s.charAt(q), q);
            cur_len ++;
        }
        // cur_len should be considered (last substring)
        return max_len < cur_len ? cur_len : max_len;
    }
}

// @lc code=end

