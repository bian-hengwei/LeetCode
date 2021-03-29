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
        int len = s.length();
        if (len % 2 == 1) return false;
        Deque<Character> stack = new LinkedList<Character>();
        for (int i = 0; i < len; i++) {
            Character cur = s.charAt(i);
            if (cur == '{' || cur == '[' || cur == '(') {
                stack.push(cur);
            }
            else {
                if (stack.isEmpty()) return false;
                char last = stack.pop();
                if (cur == '}' && ! (last == '{')) return false;
                else if (cur == ']' && ! (last == '[')) return false;
                else if (cur == ')' && ! (last == '(')) return false;
            }
        }
        return stack.isEmpty();
    }
}
// @lc code=end

