#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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
        result = []
        for dig in digits:
            if result == []:
                result = [_ for _ in nums_dict[dig]]
            else:
                length = len(result)
                for _ in range(length):
                    comb = result.pop(0)
                    result.extend([comb + _ for _ in nums_dict[dig]])
        return result
# @lc code=end

