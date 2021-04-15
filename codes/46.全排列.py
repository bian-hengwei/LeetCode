#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # recursion
        def recPermute():
            # single element base case
            if len(nums) == 1: return [[nums[0],],] # return [[n,],] as 2d array
            res = []
            # for all candidates
            for i in range(len(nums)):
                temp = nums.pop(i)
                # do recursion after remove current
                result = recPermute()
                nums.insert(i, temp)
                for l in result:
                    l.append(temp)
                res.extend(result)
            return res
        return recPermute()
# @lc code=end

