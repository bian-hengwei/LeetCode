/*
 * @lc app=leetcode.cn id=39 lang=java
 *
 * [39] 组合总和
 */

// @lc code=start
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        // recursively get combinationSum
        recGetSum(result, new ArrayList<>(), candidates, target, 0);
        return result;
    }

    private void recGetSum(List<List<Integer>> res, List<Integer> cur, int[] can, int tar, int lower) {
        // return when target found
        if (tar == 0) {
            res.add(new ArrayList<>(cur));
            return;
        }
        // loop since lower bound
        // eliminates duplicates
        for (int i = lower; i < can.length; i++) {
            // only continues if choice is available
            if (can[i] <= tar) {
                cur.add(can[i]);
                // one more step
                recGetSum(res, cur, can, tar - can[i], i);
                cur.remove(cur.size() - 1);
            }
        }
    }
}
// @lc code=end

