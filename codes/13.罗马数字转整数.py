#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        # dictionary for different special numbers
        roman_dic = {
            1  : 'I' , 
            4  : 'IV', 5  : 'V', 9  : 'IX', 10  : 'X', 
            40 : 'XL', 50 : 'L', 90 : 'XC', 100 : 'C', 
            400: 'CD', 500: 'D', 900: 'CM', 1000: 'M',
            }
        # add dig by dig from biggest
        for key in sorted(roman_dic, reverse=True):
            while s.startswith(roman_dic[key]): res, s = res + key, s[len(roman_dic[key]):]
        return res
# @lc code=end

