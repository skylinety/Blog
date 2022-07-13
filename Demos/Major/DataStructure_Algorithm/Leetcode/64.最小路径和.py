# @before-stub-for-debug-begin
from python3problem64 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        tl = len(grid[0])
        gl = len(grid)
        top = [0] * len(grid[0])

        top[0] = grid[0][0]

        for i in range(1, tl):
            top[i] = grid[0][i] + top[i - 1]

        if gl == 1:
            return top[-1]
        ret = top[0]
        for i in range(1, gl):
            for j in range(tl):
                tmp = ret
                ret = min(tmp, top[j]) + grid[i][j]
                top[j] = ret

        return ret

# @lc code=end

# dp[i][j] 表示以网格对应位置为右下角时所需的最小路径和
# dp[i][j] = min(dp[i][j-1], dp[i+1][j]) + list[i][j]
