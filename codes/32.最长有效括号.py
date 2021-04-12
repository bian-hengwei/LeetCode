#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # special case
        if s == '': return 0
        # find in two directions
        def findWithDir(direction):
            longest, left, right = 0, 0, 0
            # loop in direction
            for c in s[::direction]:
                if c == '(': left += 1
                else: right += 1
                # if equal then update max
                if left == right: longest = max(longest, left*2)
                # if invalid then start over
                elif right * direction > left * direction: left, right = 0, 0
            return longest
        return max(findWithDir(-1), findWithDir(1))
# @lc code=end

