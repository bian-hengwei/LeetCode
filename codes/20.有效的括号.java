/*
 * @lc app=leetcode.cn id=20 lang=java
 *
 * [20] 有效的括号
 */

// @lc code=start

import java.util.Deque;
import java.util.LinkedList;

class Solution {
    public boolean isValid(String s) {
        // valid len must be even
        int len = s.length();
        if (len % 2 == 1) return false;
        // stack approach
        Deque<Character> stack = new LinkedList<Character>();
        for (int i = 0; i < len; i++) {
            Character cur = s.charAt(i);
            // if left push to stack
            if (cur == '{' || cur == '[' || cur == '(') {
                stack.push(cur);
            }
            else {
                // if right check if match
                if (stack.isEmpty()) return false;
                char last = stack.pop();
                if (cur == '}' && ! (last == '{')) return false;
                else if (cur == ']' && ! (last == '[')) return false;
                else if (cur == ')' && ! (last == '(')) return false;
            }
        }
        // cover cases like "(("
        return stack.isEmpty();
    }
}
// @lc code=end

