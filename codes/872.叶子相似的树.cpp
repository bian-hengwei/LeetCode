/*
 * @lc app=leetcode.cn id=872 lang=cpp
 *
 * [872] 叶子相似的树
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
#include<stack>
#include<vector>
using namespace std;

class Solution {
public:
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        // run iterative dfs on root1 and root2 and return if they are equal
        return iterativeDfs(root1) == iterativeDfs(root2);
    }

    vector<int> iterativeDfs(TreeNode* root) {
        // stack containing recursion info
        stack<TreeNode*> s;
        // leaf nodes array
        vector<int> leafs;
        while (root != nullptr || !s.empty()) {
            // add all left nodes to the stack
            while (root != nullptr) {
                s.push(root);
                root = root->left;
            }
            // do operations on top node
            root = s.top(); s.pop();
            if (root->left == nullptr && root->right == nullptr) leafs.push_back(root->val);
            // change to the right (if exists)
            root = root->right;
        }
        return leafs;
    }
};
// @lc code=end

