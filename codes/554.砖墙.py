#
# @lc app=leetcode.cn id=554 lang=python3
#
# [554] 砖墙
#

# @lc code=start
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # deal with width = 1
        edges = {0 : 0}
        for row in wall:
            # counter of position
            ttl = 0
            for col in row[:-1]:
                ttl += col
                # record there is an edge here
                edges[ttl] = edges.get(ttl, 0) + 1
        # find max edges
        return len(wall) - max(edges.values())
# @lc code=end

