#
# @lc app=leetcode.cn id=1473 lang=python3
#
# [1473] 粉刷房子 III

# @lc code=start
'''
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/paint-house-iii/solution/fen-shua-fang-zi-iii-by-leetcode-solutio-powb/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

import math

# records in a dp array best result in the last run
class Entry:
    def __init__(self):
        self.first = math.inf
        self.first_idx = -1
        self.second = math.inf

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # adjust the color array to start from 0
        # -1 color represents not colored 
        houses = [c - 1 for c in houses]

        # init 3d dp array to be positive infinite
        # [m houses * [n colors * [target streets]]]
        dp = [[[math.inf] * target for _ in range(n)] for _ in range(m)]

        # init best 2d dp array
        best = [[Entry() for _ in range(target)] for _ in range(m)]

        # process dp with loop at depth 3
        for i in range(m):
            for j in range(n):
                # preserve inf dp value
                if houses[i] != -1 and houses[i] != j: continue
                # loop through each street case
                for k in range(target):
                    # first row and street
                    if i == 0 and k == 0: dp[i][j][k] = 0

                    else:
                        dp[i][j][k] = dp[i - 1][j][k]
                        if k > 0:
                            # get dp[i][j][k] using best array
                            info = best[i - 1][k - 1]
                            dp[i][j][k] = min(dp[i][j][k], info.second if j == info.first_idx else info.first)

                    # update with cost
                    if dp[i][j][k] != math.inf and houses[i] == -1:
                        dp[i][j][k] += cost[i][j]
                    
                    # update best
                    info = best[i][k]
                    if dp[i][j][k] < info.first:
                        info.second = info.first
                        info.first = dp[i][j][k]
                        info.first_idx = j
                    elif dp[i][j][k] < info.second:
                        info.second = dp[i][j][k]
                        
        # get result which is min value in dp array
        ans = min(dp[m - 1][j][target - 1] for j in range(n))
        return -1 if ans == math.inf else ans
# @lc code=end

