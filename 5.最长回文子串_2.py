#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (33.47%)
# Likes:    3343
# Dislikes: 0
# Total Accepted:    508.6K
# Total Submissions: 1.5M
# Testcase Example:  '"babad"'
#
# 给你一个字符串 s，找到 s 中最长的回文子串。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "cbbd"
# 输出："bb"
# 
# 
# 示例 3：
# 
# 
# 输入：s = "a"
# 输出："a"
# 
# 
# 示例 4：
# 
# 
# 输入：s = "ac"
# 输出："a"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 仅由数字和英文字母（大写和/或小写）组成
# 
# 
#

# @lc code=start
# HashMap method (self-written)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # {character: [appearances]}
        d = {}
        for (i, c) in enumerate(s):
            if c not in d:
                d[c] = []
            d[c].append(i)
        best = s[0];
        for (i, c) in enumerate(s):
            # search for palindromes at each index
            for j in range(len(d[c])-1, 0, -1):
                if d[c][j] == i: break;
                elif s[i:d[c][j]+1] == s[i:d[c][j]+1][::-1]:
                    best = s[i:d[c][j]+1] if d[c][j]-i+1 > len(best) else best
        return best
# @lc code=end

