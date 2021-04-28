/*
 * @lc app=leetcode.cn id=633 lang=cpp
 *
 * [633] 平方数之和
 */

// @lc code=start
#include<math.h>

using namespace std;

class Solution {
public:
    bool judgeSquareSum(int c) {
        // loop all int < sqrt(c)
        for (long a = 0; a * a <= c; a++) {
            double b = sqrt(c - a * a);
            if (b == (int)b) return true;
        }
        return false;
    }
};
// @lc code=end

