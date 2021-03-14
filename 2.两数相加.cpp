/*
 * @lc app=leetcode.cn id=2 lang=cpp
 *
 * [2] 两数相加
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // dummy to store the useless root
        ListNode* dummy = new ListNode();
        ListNode* cur = dummy;
        int sum = 0;
        while (l1 || l2 || sum) {
            // in each iteration first add sum
            if (l1 != nullptr) {
                sum += l1->val;
                l1 = l1->next;
            }
            if (l2 != nullptr) {
                sum += l2->val;
                l2 = l2->next;
            }
            // stores the next dig in new node
            cur->next = new ListNode(sum % 10);
            cur = cur->next;
            // computes the carry out
            sum /= 10;
        }
        return dummy->next;
    }
};
// @lc code=end

