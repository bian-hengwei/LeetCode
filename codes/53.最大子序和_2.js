/*
 * @lc app=leetcode.cn id=53 lang=javascript
 *
 * [53] 最大子序和
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */

/*
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/maximum-subarray/solution/zui-da-zi-xu-he-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
*/

// struct of a subtree
// lsum: max sum starting on the left
// rsum: max sum ending on the right
// msum: real max sum
// isum: total sum
function Status(l, r, m, i) {
    this.lSum = l;
    this.rSum = r;
    this.mSum = m;
    this.iSum = i;
}

// build next subtree by initing sums
const pushUp = (l, r) => {
    const iSum = l.iSum + r.iSum;
    const lSum = Math.max(l.lSum, l.iSum + r.lSum);
    const rSum = Math.max(r.rSum, r.iSum + l.rSum);
    const mSum = Math.max(Math.max(l.mSum, r.mSum), l.rSum + r.lSum);
    return new Status(lSum, rSum, mSum, iSum);
}

// binary recursion
const getInfo = (a, l, r) => {
    if (l === r) return new Status(a[l], a[l], a[l], a[l]);
    const m = (l + r) >> 1;
    const lSub = getInfo(a, l, m);
    const rSub = getInfo(a, m + 1, r);
    return pushUp(lSub, rSub);
}

var maxSubArray = function(nums) {
    return getInfo(nums, 0, nums.length - 1).mSum;
};

// @lc code=end

