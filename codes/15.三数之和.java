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
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if (nums.length < 3) return result;
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++) {
            if (i != 0 && nums[i-1] == nums[i]) continue;
            int target = -nums[i], j = i + 1, k = nums.length - 1;
            while (j < k) {
                if (nums[j] + nums[k] < target || 
                    j != 0 && j != i + 1 && nums[j-1] == nums[j]) {
                    j ++;
                } else if (nums[j] + nums[k] > target) {
                    k --;
                } else {
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

