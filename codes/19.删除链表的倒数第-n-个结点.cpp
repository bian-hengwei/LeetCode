/*
 * @lc app=leetcode.cn id=19 lang=cpp
 *
 * [19] 删除链表的倒数第 N 个结点
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (head->next == nullptr) return nullptr;
        ListNode* dummy = new ListNode(0, head);
        ListNode* par = dummy;
        ListNode* cur = head;
        int counter = 0;
        while (cur != nullptr) {
            cur = cur->next;
            if (n == counter) {
                par = par->next;
            } else {
                counter ++;
            }
        }
        par->next = par->next->next;
        return dummy->next;

    }
};
// @lc code=end

