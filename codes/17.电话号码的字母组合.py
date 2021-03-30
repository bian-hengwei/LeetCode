#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # {dig : letters}
        nums_dict = {
                    '2' : 'abc', 
                    '3' : 'def', 
                    '4' : 'ghi', 
                    '5' : 'jkl', 
                    '6' : 'mno', 
                    '7' : 'pqrs', 
                    '8' : 'tuv', 
                    '9' : 'wxyz'
                    }
        # init result queue
        result = []
        for dig in digits:
            # append letters for first digit
            if result == []:
                result = [_ for _ in nums_dict[dig]]
            else:
                # for each current combination
                # append new letters
                length = len(result)
                for _ in range(length):
                    comb = result.pop(0)
                    result.extend([comb + _ for _ in nums_dict[dig]])
        return result
# @lc code=end

