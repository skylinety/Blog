/*
 * @lc app=leetcode.cn id=62 lang=javascript
 *
 * [62] 不同路径
 */

// @lc code=start
/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function (m, n) {
    let top = [0];
    let left = 1;
    let ret = 1;

    for (let i = 1; i < n; i++) {
        for (let j = 1; j < m; j++) {
            ret = (j == 1 ? 1 : left) + (i == 1 ? 1 : top[j])
            left = ret
            top[j] = ret
        }
    }

    return ret
};

// dp[i][j] = dp[i - 1][j] + dp[i][j-1]
// @lc code=end


// @after-stub-for-debug-begin
module.exports = uniquePaths;
// @after-stub-for-debug-end