/*
 * @lc app=leetcode.cn id=897 lang=cpp
 *
 * [897] 递增顺序查找树
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
private:
    // dummy node
    TreeNode* current = new TreeNode(-1);
    TreeNode* dummy = current;
public:
    TreeNode* increasingBST(TreeNode* root) {
        // base case
        if (root == nullptr) return nullptr;
        // in order traverse left child
        // set current as left child
        increasingBST(root->left);
        // fix tree
        current->right = root;
        root->left = nullptr;
        current = root;
        // traverse right child
        increasingBST(root->right);
        return dummy->right;
    }
};
// @lc code=end

