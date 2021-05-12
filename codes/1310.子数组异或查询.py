#
# @lc app=leetcode.cn id=1310 lang=python3
#
# [1310] 子数组异或查询

# @lc code=start
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # ttl[i] is the prefix xor accumulate for arr[0] ... arr[i-1]
        ttl = list(accumulate([0] + arr, xor))
        # arr[l] ^ arr[l+1] ^ ... ^ arr[r-1] ^ arr[r]
        # = arr[0] ^ ... ^ arr[l-1]  ^  arr[0] ^ ... ^ arr[r+1 - 1]
        # = ttl[l]                   ^  ttl[r+1]
        return [ttl[l] ^ ttl[r + 1] for l, r in queries]   
# @lc code=end

