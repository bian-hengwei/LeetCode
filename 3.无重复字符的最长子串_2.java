/*
 * @lc app=leetcode.cn id=3 lang=java
 *
 * [3] 无重复字符的最长子串
 *
 * https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
 *
 * algorithms
 * Medium (36.64%)
 * Likes:    5117
 * Dislikes: 0
 * Total Accepted:    877.3K
 * Total Submissions: 2.4M
 * Testcase Example:  '"abcabcbb"'
 *
 * 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
 * 
 * 
 * 
 * 示例 1:
 * 
 * 
 * 输入: s = "abcabcbb"
 * 输出: 3 
 * 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
 * 
 * 
 * 示例 2:
 * 
 * 
 * 输入: s = "bbbbb"
 * 输出: 1
 * 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
 * 
 * 
 * 示例 3:
 * 
 * 
 * 输入: s = "pwwkew"
 * 输出: 3
 * 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
 * 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
 * 
 * 
 * 示例 4:
 * 
 * 
 * 输入: s = ""
 * 输出: 0
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 0 
 * s 由英文字母、数字、符号和空格组成
 * 
 * 
 */

// @lc code=start


// Map version (self written), same time complexity but slower with hash map

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

// @lc code=end

