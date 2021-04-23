/*
 * @lc app=leetcode.cn id=368 lang=cpp
 *
 * [368] 最大整除子集
 */

// @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        // sort to help dp
        sort(nums.begin(), nums.end());
        int dp[nums.size()];
        int maxIndex = 0;
        // dp[i] = max(dp[j] + 1) for all dp[i] % dp[j] before it
        for (int i = 0; i < nums.size(); i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (! (nums[i] % nums[j])) dp[i] = dp[j] >= dp[i] ? dp[j] + 1 : dp[i];
            }
            if (dp[i] > dp[maxIndex]) maxIndex = i;
        }
        vector<int> res;
        res.push_back(nums[maxIndex]);
        int last = dp[maxIndex];
        // push divisor with dp[j] = dp[i] - 1
        for (int i = maxIndex - 1; 0 <= i; i--) {
            if (res.back() % nums[i] == 0 && dp[i] == last - 1) {
                res.push_back(nums[i]);
                last = dp[i];
            }
        }
        return res;
    }
};
// @lc code=end

