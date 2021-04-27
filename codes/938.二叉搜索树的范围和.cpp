/*
 * @lc app=leetcode.cn id=938 lang=cpp
 *
 * [938] 二叉搜索树的范围和
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int rangeSumBST(TreeNode* root, int low, int high) {
        // recursion base at null nodes
        if (root == nullptr) return 0;
        // dfs recursion (preorder traversal)
        int result = 0;
        if (low <= root->val && root->val <= high) result += root->val;
        if (root->val < high) result += rangeSumBST(root->right, low, high); 
        if (low < root->val)result += rangeSumBST(root->left, low, high);
        return result;
    }
};
// @lc code=end

