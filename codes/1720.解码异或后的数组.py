#
# @lc app=leetcode.cn id=1720 lang=python3
#
# [1720] 解码异或后的数组

# @lc code=start
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # use rule if a ^ b = c, a = b ^ c
        for i in range(len(encoded)): encoded[i] ^= first if not i else encoded[i - 1]
        return [first] + encoded
# @lc code=end

