/*
 * @lc app=leetcode.cn id=137 lang=cpp
 *
 * [137] 只出现一次的数字 II
 */

// @lc code=start
#include<vector>

using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        // a represents msb 2
        // b represents the other bits
        int a = 0, b = 0;
        for (int n : nums) { b = ~a & (b ^ n); a = ~b & (a ^ n); }
        return b;
    }
};
// @lc code=end

