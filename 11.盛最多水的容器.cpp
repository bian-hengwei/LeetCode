/*
 * @lc app=leetcode.cn id=11 lang=cpp
 *
 * [11] 盛最多水的容器
 */

// @lc code=start
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
    int maxArea(vector<int>& height) {
        // initialize max, and two pointers from left and right
        int m = 0, i = 0, j = height.size() - 1;
        while (i < j) {
                int area = (j-i) * min(height[i], height[j]);
                if (m < area) m = area;
                // add the smaller one
                height[i] < height[j] ? i++ : j--;
        }
        return m;
    }

};
// @lc code=end

