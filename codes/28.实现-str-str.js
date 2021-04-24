/*
 * @lc app=leetcode.cn id=28 lang=javascript
 *
 * [28] 实现 strStr()
 */

// @lc code=start
/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
 var strStr = function(haystack, needle) {
    // KMP search algorithm
    // according to requirement
    if (needle === "") return 0;

    // initialize next array
    next = [-1];
    // current index and next array pointer
    i = 0, j = -1;
    while (i < needle.length - 1) {
        // matching prefix found
        if (j === -1 || needle.charAt(i) === needle.charAt(j)) {
            i ++;
            j ++;
            next.push(j);
        }
        // backtrack
        else j = next[j];
    }

    console.log(next);

    // searching starts here
    // pointer on haystack and needle
    hIdx = 0, nIdx = 0;
    while (hIdx < haystack.length) {
        // matching item found
        // or if nIdx === -1 then non matching
        if (nIdx === -1 || needle.charAt(nIdx) === haystack.charAt(hIdx)) {
            // found a match
            if (nIdx === needle.length - 1) return hIdx - nIdx;
            // go for one step
            else {
                hIdx ++;
                nIdx ++;
            }
        }
        // backtrack needle pointer for one step
        else nIdx = next[nIdx];
    }
    // not found
    return -1;
};
// @lc code=end

