#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def expand(self, s, l, r):
        # expand as far as possible if the two letters are equal
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return l + 1, r - 1

    def longestPalindrome(self, s: str) -> str:
        # start and end of the longest palindrome
        l, r = 0, 0
        for i in range(len(s)):
            # expand at each index
            l1, r1 = self.expand(s, i, i)
            l2, r2 = self.expand(s, i, i + 1)
            if r1 - l1 > r - l:
                l, r = l1, r1
            if r2 - l2 > r - l:
                l, r = l2, r2
        return s[l: r + 1]
# @lc code=end

