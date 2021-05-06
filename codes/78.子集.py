#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ''' recursive approach
        if len(nums) == 1:
            return [[], [nums[0]]]
        else:
            lst = self.subsets(nums[:-1])
            for i in range(len(lst)): lst.append(lst[i].copy() + [nums[-1]])
            return lst
        '''
        # init res with empty set case
        res = [[]]
        # for each new number
        for i in range(len(nums)):
            # duplicate the old result and add to end of each sublist
            for j in range(len(res)): res.append(res[j] + [nums[i]])
        return res
# @lc code=end

