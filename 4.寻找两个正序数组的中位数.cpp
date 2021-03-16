/*
 * @lc app=leetcode.cn id=4 lang=cpp
 *
 * [4] 寻找两个正序数组的中位数
 */

// @lc code=start
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // m is smaller
        int m = nums1.size(), n = nums2.size();
        if (m > n) return findMedianSortedArrays(nums2, nums1);
        int l = 0, r = m;
        // while not perfectly partitioned
        while (l <= r) {
            int i = (l + r) / 2;
            int j = (m + n + 1) / 2 - i;
            // normal cases:
            if (j != 0 && i != m && nums1[i] < nums2[j-1]) {
                l = i + 1;
            } else if (i != 0 && j != n && nums2[j] < nums1[i-1]) {
                r = i - 1;
            } else {
                // base condition
                // max of longer half
                int median;
                if (i == 0) median = nums2[j-1];
                else if (j == 0) median = nums1[i-1];
                else median = nums1[i-1] < nums2[j-1] ? nums2[j-1] : nums1[i-1];
                if ((m + n) % 2) {
                    return median;
                } else {
                    // average with min half of the second half
                    // if even length
                    if (i == m) return (median + nums2[j]) / 2.0;
                    else if (j == n) return (median + nums1[i]) / 2.0;
                    return nums1[i] < nums2[j] ? (median + nums1[i]) / 2.0 : (median + nums2[j]) / 2.0;
                }
            }
        }
        return 0;
    }
};
// @lc code=end

