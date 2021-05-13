#
# @lc app=leetcode.cn id=1269 lang=python3
#
# [1269] 停在原地的方案数

# @lc code=start
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # MOD: modular constant avoiding integer overflow
        # arrLen: at most steps // 2 + 1 can get back to the origin
        MOD, arrLen = 10 ** 9 + 7, min(arrLen, steps // 2 + 1)
        # dp array with dp[i] representing the i th element of the array
        # extra 0s at the start and end of the array to ease dp
        dp = [1 if i == 1 else 0 for i in range(arrLen + 2)]
        # for each step
        for i in range(steps):
            # the max length of dp conversion is step - i (further elements cannot reach back to origin)
            tmp, arrLen = dp[0], min(arrLen, steps - i)
            # in place sliding window dp
            for j in range(arrLen): dp[j + 1], tmp = (tmp + dp[j + 1] + dp[j + 2]) % MOD, dp[j + 1]
        return dp[1] 
# @lc code=end

