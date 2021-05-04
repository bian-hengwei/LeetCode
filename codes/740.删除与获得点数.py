#
# @lc app=leetcode.cn id=740 lang=python3
#
# [740] 删除与获得点数

# @lc code=start
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # do dp for all integers smaller than maxVal
        maxVal = max(nums) + 1
        # count each element
        count = [0] * maxVal
        for num in nums: count[num] += 1
        # improved dp array
        dp1, dp2 = 0, count[1]
        # dp[i] = max(dp[i-2], dp[i-1] + count[i] * i)
        for i in range(2, maxVal): dp1, dp2 = [dp2, max(dp1 + i * count[i], dp2)]
        return dp2
# @lc code=end

