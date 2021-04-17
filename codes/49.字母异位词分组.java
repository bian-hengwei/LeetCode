/*
 * @lc app=leetcode.cn id=49 lang=java
 *
 * [49] 字母异位词分组
 */

// @lc code=start
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<Long, List<String>> map = new HashMap<>();
        // store according to hash code
        for (String str : strs) {
            long hashCode = primeHash(str);
            List<String> lst = map.getOrDefault(hashCode, new ArrayList<>());
            lst.add(str);
            map.put(hashCode, lst);
        }
        return new ArrayList<List<String>>(map.values()); 
    }

    // 26 primes corresponding to 26 characters
    private int[] primes = {
        2,  3,  5,  7,  11, 13, 17, 19, 23, 29, 31, 37, 41, 
        43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
    };

    //get unique hash code
    private long primeHash(String str) {
        long result = 1;
        for (int i = 0; i < str.length(); i++)
            result *= primes[str.charAt(i) - 'a'];
        return result;
    }
}
// @lc code=end

