# @before-stub-for-debug-begin
from python3problem509 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        # if n < 2:
        #     return n
        # return self.fib(n - 1) + self.fib(n - 2)

        if n < 2:
            return n
        pre = 0
        pos = 1
        i = 1

        while i < n:
            temp = pre
            pre = pos
            pos = temp + pos
            i += 1

        return pos 


# @lc code=end


# dp[n] = dp[n - 1] + dp[n - 2]
