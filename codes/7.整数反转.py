#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        # rev 0 is 0
        if x == 0: return 0
        # record sign, normalize x, init rev
        sign, x, rev = x // abs(x), abs(x), 0
        # reverse
        while x > 0: rev, x = rev * 10 + x % 10, x // 10
        # find overflow
        limit = 2147483647
        if rev > limit or rev < - limit - 1: return 0
        else: return rev * sign
# @lc code=end

