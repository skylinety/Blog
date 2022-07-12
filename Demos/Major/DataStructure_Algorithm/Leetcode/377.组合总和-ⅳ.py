# @before-stub-for-debug-begin
from python3problem377 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for t in range(1, target + 1):
            for n in nums:
                dp[t] = dp[t] + (dp[t - n] if t - n > -1 else 0)
        
        return dp[target]
# @lc code=end

# dp[i][j] 表示前i个数无序排列得到数值j的组合数
# dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i]]
