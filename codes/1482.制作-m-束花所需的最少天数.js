/*
 * @lc app=leetcode.cn id=1482 lang=javascript
 *
 * [1482] 制作 m 束花所需的最少天数
 */

// @lc code=start
/**
 * @param {number[]} bloomDay
 * @param {number} m
 * @param {number} k
 * @return {number}
 */
 var minDays = function(bloomDay, m, k) {
    n = bloomDay.length;
    // case where not enough flowers
    if (n < m * k) return -1;
    // left and right bounds for binary search
    l = Math.min.apply(null, bloomDay), r = Math.max.apply(null, bloomDay);
    // case where just enough flowers
    if (n === m * k) return r;
    // do binary search for day
    while (l < r) {
        mid = Math.floor((l + r) / 2);
        if (!countBouquets(bloomDay, m, k, mid)) l = mid + 1;
        else r = mid;
    }
    // left bound is the search result
    return l;
};

// helper that checks if m bouquets of k bloom within day
countBouquets = function(bloomDay, m, k, day) {
    row = 0, count = 0;
    for (i = 0; i < bloomDay.length && count < m; i++) {
        row = bloomDay[i] <= day ? row + 1: 0;
        if (row === k) [row, count] = [0, count + 1];
    }
    return count >= m;
}
// @lc code=end

