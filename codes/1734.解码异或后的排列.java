/*
 * @lc app=leetcode.cn id=1734 lang=java
 *
 * [1734] 解码异或后的排列
 */

// @lc code=start
class Solution {
    public int[] decode(int[] encoded) {
        int n = encoded.length + 1, xor1 = 0, xor2 = 0;
        // xor1 = 1 ^ 2 ^ ... ^ n
        for (int i = 1; i <= n; i++) xor1 ^= i;
        // xor2 = encoded[1 ^ 3 ^ 5 ^ 7 ^ ... ^ n - 1]
        // xor2 = perm[1 ^ 2]  ^  [3 ^ 4]  ^  [5 ^ 6]  ^ ... ^ [n - 1 ^ n] 
        for (int i = 1; i < n - 1; i += 2) xor2 ^= encoded[i];
        int[] perm = new int[n];
        // xor1 ^ xor2 = perm[0]
        perm[0] = xor1 ^ xor2;
        // perm[i] = perm[i - 1] ^ encoded[i - 1]
        for (int i = 1; i < n; i++) perm[i] = perm[i - 1] ^ encoded[i - 1];
        return perm;
    }
}
// @lc code=end

