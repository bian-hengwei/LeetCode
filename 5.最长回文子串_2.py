#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串

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

