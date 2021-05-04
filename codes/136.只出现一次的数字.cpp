/*
 * @lc app=leetcode.cn id=136 lang=cpp
 *
 * [136] 只出现一次的数字
 */

// @lc code=start
#include<vector>

using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int num = 0;
        // as all other number appears twice
        // 0 xor n xor x = 0
        // 0 xor n = n
        for (int i = 0; i < nums.size(); i++) num ^= nums[i];
        return num;
    }
};
// @lc code=end

