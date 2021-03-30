/*
 * @lc app=leetcode.cn id=23 lang=java
 *
 * [23] 合并K个升序链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

import java.util.PriorityQueue;

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {

        // dummy to deal with empty input
        // dummy.next is head
        ListNode dummy = new ListNode();
        ListNode cur = dummy;
        
        if (lists.length == 0) return dummy.next;

        // min heap keeps track of all smallest nodes not dealt with
        PriorityQueue<ListNode> minHeap = new PriorityQueue<ListNode>((x, y) -> x.val - y.val);

        // init min heap
        for (int i = 0; i < lists.length; i++) {
            if (lists[i] != null) {
                minHeap.add(lists[i]);
            }
        }

        // do til all elememts are sorted
        while (!minHeap.isEmpty()) {
            // poll min
            ListNode poll = minHeap.poll();
            // add next if exist
            if (poll.next != null) minHeap.add(poll.next);
            // append to head
            cur.next = new ListNode();
            cur = cur.next;
            cur.val = poll.val;
        }

        return dummy.next;
    }
}

// @lc code=end

