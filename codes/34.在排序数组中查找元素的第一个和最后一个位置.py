#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # default result
        result = [-1, -1]
        if len(nums) == 0: return result

        # first binary search
        i, j = 0, len(nums)-1
        while i <= j:
            mid = i + (j - i) // 2
            if nums[mid] == target:
                # record current first
                result[0] = mid
                # search for first occurence
                j = mid - 1
            elif nums[mid] < target: i = mid + 1
            else: j = mid - 1
        if result[0] == -1: return result
        # second binary search
        i, j = 0, len(nums)-1
        while i <= j:
            mid = i + (j - i) // 2
            if nums[mid] == target:
                # record current last
                result[1] = mid
                # search for last occurence
                i = mid + 1
            elif nums[mid] < target: i = mid + 1
            else: j = mid - 1
        return result
# @lc code=end

