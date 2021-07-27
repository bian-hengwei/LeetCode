#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # recursive helper method that helps to solve the problem in O(n) complexity
        def recIsValidBST(root, left, right):
            return (
                # base case: Nones
                root is None or (
                    # checks whether current node matches the constraint
                    root.val > left and
                    root.val < right and
                    # checks whether subtrees matches the constraint by lowering the limit
                    recIsValidBST(root.left, left, root.val) and
                    recIsValidBST(root.right, root.val, right)
                )
        )
        # init limits on root run as it can be any value
        return recIsValidBST(root, float('-inf'), float('inf'))
# @lc code=end

