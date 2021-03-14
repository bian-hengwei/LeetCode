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