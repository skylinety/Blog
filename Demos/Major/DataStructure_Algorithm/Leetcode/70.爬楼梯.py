# @before-stub-for-debug-begin
from python3problem70 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start


class Solution:
    def climbStairs(self, n: int) -> int:
        note = 0
        pre2 = 0
        pre1 = 1
        for i in range(n):
            note = pre1
            pre1 = pre1 + pre2
            pre2 = note
        return pre1

# @lc code=end


# dp[n] 代表到达第n阶对应的方法数
# dp[n] = dp[n - 1] + dp[n - 2]
