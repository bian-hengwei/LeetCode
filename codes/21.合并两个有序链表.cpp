/*
 * @lc app=leetcode.cn id=21 lang=cpp
 *
 * [21] 合并两个有序链表
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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        // dummy to deal with empty
        ListNode* dummy = new ListNode();
        // current pointer
        ListNode* l3 = dummy;
        while (l1 != nullptr && l2 != nullptr) {
            // append smaller value
            if (l1->val < l2->val) {
                l3->next = new ListNode(l1->val);
                l1 = l1->next;
            } else {
                l3->next = new ListNode(l2->val);
                l2 = l2->next;
            }
            // increment pointer
            l3 = l3->next;
        }
        // add remains and return
        if (l1 != nullptr) l3->next = l1;
        else l3->next = l2;
        return dummy->next;
    }
};
// @lc code=end

