# @before-stub-for-debug-begin
from python3problem494 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        top = sum(nums)
        dp = [0] * (top * 4 + 1)
        dp[top + nums[0]] = dp[top - nums[0]] = 1
        for n in nums:
            pre = dp
            dp = [0] * (top * 4 + 1)
            for t in range(top,-top - 1, -1):
                pos = t + top
                dp[pos] =  pre[pos - n] + pre[pos + n]
        return dp[target]     
# @lc code=end
# dp[i][j]表示前i个数用完可以组合得到j数值的方式
# dp[i][j] = dp[i - 1][j - nums[i]] + dp[i - 1][j + nums[i]]




# solution 1
# dp[i][j]表示前i个数用完可以组合得到j数值的方式
# dp[i][j] = dp[i - 1][j - nums[i]] 解数量 
        #           + dp[i - 1][j + nums[i]] 解数量

# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         inputs = map(lambda n: -n, nums)

#         m = max(nums)

#         top = sum(nums)
#         bottom = - top
#         if target > top or target < bottom:
#             return 0
#         pre = {
#             # nums[0]: 1,
#             # -nums[0]: 1
#         }

#         for n in range(top, bottom - 1, -1):
#             pre[n] = 0
#             # now[n] = 0

#         pre[nums[0]] = 1
#         pre[-nums[0]] = 1
#         if nums[0] == 0:
#             pre[0] = 2

#         for i in range(1, len(nums)):
#             now = {
#             }
#             for j in range(top, bottom - 1, -1):
#                 l = 0
#                 r = 0

#                 if j - nums[i] >= bottom:
#                     l = pre[j - nums[i]]
#                 if j + nums[i] <= top:
#                     r = pre[j + nums[i]]
#                 now[j] = l + r
#             pre = now

#         return pre[target]
