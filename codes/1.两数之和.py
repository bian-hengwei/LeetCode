#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # {number : index}
        d = dict()
        for i in range(len(nums)):
            # return if complementary number already iterated
            if target-nums[i] in d:
                return [d[target-nums[i]], i]
            # store in hash map
            d[nums[i]] = i
# @lc code=end

