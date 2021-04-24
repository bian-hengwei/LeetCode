/*
 * @lc app=leetcode.cn id=377 lang=cpp
 *
 * [377] 组合总和 Ⅳ
 */

// @lc code=start
#include<vector>

using namespace std;

class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        // dp array for all values smaller than target
        // representing number of choices to achieve i from array
        vector<int> dp(target + 1);
        dp[0] = 1;
        // loop till target is computed
        for (int i = 1; i <= target; i++) {
            // for each element in numbers array
            // we try to see how many combinations add this number reaches target
            for (int j = 0; j < nums.size(); j++) {
                // int max is set as a max limit
                // according to the question
                if (nums[j] <= i && dp[i - nums[j]] < INT_MAX - dp[i]) {
                    dp[i] += dp[i - nums[j]];
                }
            }
        }
        return dp[target];
    }
};
// @lc code=end

