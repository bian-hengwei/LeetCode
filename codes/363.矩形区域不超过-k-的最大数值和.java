/*
 * @lc app=leetcode.cn id=363 lang=java
 *
 * [363] 矩形区域不超过 K 的最大数值和
 */

// @lc code=start
class Solution {
    public int maxSumSubmatrix(int[][] matrix, int k) {
        int m = matrix.length, n = matrix[0].length;
        int result = Integer.MIN_VALUE;
        // enumerate all start column index
        for (int i = 0; i < n; i++) {
            // array storing sum at each row index
            int[] sum = new int[m];
            // enumerate all end column index
            for (int j = i; j < n; j++) {
                // add each row for this new end column index
                for (int l = 0; l < m; l++) sum[l] += matrix[l][j];
                // total is the sum for all rows in the loop
                int ttl = 0;
                // sums is a collection of processed totals
                TreeSet<Integer> sums = new TreeSet<Integer>();
                sums.add(0);
                // for each new row
                for (int s : sum) {
                    ttl += s;
                    // find if a up bound exists such that
                    // Total(down) - Total(up) <= k
                    Integer sUp = sums.ceiling(ttl - k);
                    // if exists record largest Total(down) - Total(up) value
                    if (sUp != null) result = Math.max(result, ttl - sUp);
                    sums.add(ttl);
                    if (result == k) return k;
                }
            }
        }
        return result;
    }
}
// @lc code=end

