/*
 * @lc app=leetcode.cn id=15 lang=java
 *
 * [15] 三数之和
 */

// @lc code=start

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // init result array: [[int]]
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if (nums.length < 3) return result;
        // O(nlogn) time complexity O(logn) space complexity
        // sort to use double pointer
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++) {
            // boundry when same dig found
            if (i != 0 && nums[i-1] == nums[i]) continue;
            // init double pointer at j, k to make j + k = -nums[i]
            int target = -nums[i], j = i + 1, k = nums.length - 1;
            while (j < k) {
                if (nums[j] + nums[k] < target || 
                    // detects if j is the same as prev term
                    j != 0 && j != i + 1 && nums[j-1] == nums[j]) {
                    j ++;
                } else if (nums[j] + nums[k] > target) {
                    k --;
                } else {
                    // found
                    List<Integer> lst = Arrays.asList(nums[i], nums[j], nums[k]);
                    result.add(lst);
                    j ++;
                    k --;
                }
            }
        }
        return result;
    }
}
// @lc code=end

