# @before-stub-for-debug-begin
from python3problem486 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=486 lang=python3
#
# [486] 预测赢家
#

# @lc code=start
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        l = len(nums)
        dp = [[0] * l for _ in range(l)]
        for i, n in enumerate(nums):
            dp[i][i] = n
        for j in range(1, l):
            for i in range(j - 1, -1, -1):
                dp[i][j] = max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1])
        # for i in range(l - 2, -1, -1):
        #     for j in range(i + 1, l):
        #         dp[i][j] = max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1])

        return dp[0][l - 1] >= 0

# @lc code=end


# dp[i][j]从分数数组下标i到j区间最优选择后的差值 i<j
# 当前选择左边 nums[i]-dp[i+1][j]
# 当前选择右边 nums[j]-dp[i][j-1]
# dp[i][j] = max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1])


