/*
 * @lc app=leetcode.cn id=44 lang=cpp
 *
 * [44] 通配符匹配
 */

// @lc code=start
#include<string>
#include<vector>

using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.length(), n = p.length();
        // dp vector storing matching status at dp[i][j]
        vector<bool> dp(n + 1);
        // dp[0][0] = true
        dp[0] = true;
        // dp[0][j] = true if p[0...j] = "*...*"
        for (int j = 0; j < n; j++) {
            if (p[j] == '*') dp[j + 1] = true;
            else break;
        }
        // if p[j] == '*' dp[i][j] = dp[i-1][j] || dp[i][j-1]
        // else dp[i][j] = (s[i] == p[j] || p[j] == '?') && dp[i-1][j-1]
        for (int i = 0; i < m; i++) {
            // store left up element
            bool leftUp = dp[0];
            // dp[i][0] = false
            dp[0] = false;
            for (int j = 0; j < n; j++) {
                if (p[j] == '*') {
                    leftUp = dp[j + 1];
                    dp[j + 1] = dp[j + 1] || dp[j];
                }
                else {
                    bool temp = dp[j + 1];
                    dp[j + 1] = (p[j] == '?' || s[i] == p[j]) && leftUp;
                    leftUp = temp;
                }
            }
        }
        // dp[i][j]
        return dp[n];
    }
};
// @lc code=end

